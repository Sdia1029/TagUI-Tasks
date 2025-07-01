import os
import tagui as t
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -------------------------------
# 1 SCRAPE WEATHER
# -------------------------------

city = input("Enter your city (lahore, karachi, islamabad): ").strip().lower()
user_email = input("Enter your email to receive the weather report: ").strip()

city_url_part = city.replace(" ", "-")
url = f"https://www.timeanddate.com/weather/pakistan/{city_url_part}"

print(f"\n Fetching weather for: {city.title()}")

t.init()
t.url(url)
t.wait(5)

temperature = t.read('//div[@id="qlook"]/div[@class="h2"]')
condition = t.read('//div[@id="qlook"]/p')

today = datetime.now().strftime("%d %B %Y")

# Save data to file
with open("weather_data.txt", "w", encoding="utf-8") as f:
    f.write(f"Date: {today}\n")
    f.write(f"City: {city.title()}\n")
    f.write(f"Temperature: {temperature}\n")
    f.write(f"Condition: {condition}\n")

t.close()

# -------------------------------
# 2 GENERATE SUMMARY
# -------------------------------

client = Groq(api_key=GROQ_API_KEY)

with open("weather_data.txt", "r", encoding="utf-8") as f:
    data = f.read()

prompt = f"""
{data}

Write a short, clear daily weather report in ENGLISH. Be polite and directly to the point.
Use only the city name given in the data. Include city, temperature, condition, and today's date.

End with:
Best regards,
Sadia Eman
Weather Reporter
"""

response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "system", "content": "You are a professional weather reporter."},
        {"role": "user", "content": prompt}
    ]
)

summary = response.choices[0].message.content

with open("weather_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)

# -------------------------------
# 3 SEND EMAIL
# -------------------------------

msg = EmailMessage()
msg['Subject'] = f"Weather Report - {city.title()} - {today}"
msg['From'] = EMAIL_ADDRESS
msg['To'] = user_email
msg.set_content(summary)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print(f"\nWeather report sent to {user_email} successfully!")
