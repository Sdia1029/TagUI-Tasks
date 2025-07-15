# 🗂️ Automation Projects Collection

This repository contains **six mini automation projects** developed using **Python**, **TagUI**, **GenAI**, and **RPA tools**.  
Each project demonstrates **practical automation** for real-world tasks — perfect for students, interns, and automation enthusiasts!

---

## 📌 Projects Included

| # | Project | Description | Tools |
|---|---------------------------|--------------------------------------------|----------------------------|
| 1️⃣ | **Job Scraper Bot** | Scrapes jobs, filters with GenAI, emails results | Python, TagUI, Groq API |
| 2️⃣ | **News Scraper Bot** | Searches news topics on Dawn.com | Python, TagUI |
| 3️⃣ | **Data Entry Bot** | Auto-fills forms from Excel or CSV | Python, TagUI, pandas |
| 4️⃣ | **Weather Reporter Bot** | Scrapes weather, GenAI summary, emails it | Python, TagUI, Groq API, PDF |
| 5️⃣ | **Weather Report Generator** | Generates detailed PDF weather report & emails it | Python, TagUI, PDF |
| 6️⃣ | **Quotes Scraper Bot** | Scrapes quotes and authors, saves to CSV | Python, requests, BeautifulSoup, pandas |

---

## 🚀 Projects Details & How to Use

---

### ✅ 1️⃣ Job Scraper Bot

**Description:**  
Scrapes jobs from **Mustakbil.com**, filters using **GenAI**, and emails matching jobs automatically.

**Features:**  
- Web scraping with TagUI  
- Smart filtering using Groq API  
- Emails the filtered jobs

**How to Use:**  
1. Add `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, and `GROQ_API_KEY` in a `.env` file.  
2. Run the script.  
3. Enter:
   - Job title
   - City
   - Recipient email  
4. The bot scrapes, filters, and sends matching jobs to your email.

---

### ✅ 2️⃣ News Scraper Bot

**Description:**  
Searches for news on **Dawn.com** for any topic you enter.

**Features:**  
- Automated search using TagUI  
- Custom topic input

**How to Use:**  
1. Run the script.  
2. Enter your topic.  
3. The bot opens Dawn.com, searches, and displays results for you to check.

---

### ✅ 3️⃣ Data Entry Bot

**Description:**  
Automatically fills out forms on the **RPA Challenge** website using data from an Excel or CSV file.

**Features:**  
- Reads `challenge.xlsx` with pandas  
- Uses TagUI (RPA) to fill and submit forms for each record

**How to Use:**  
1. Place `challenge.xlsx` in the project folder.  
   - Required columns:
     - First Name
     - Last Name
     - Company Name
     - Role in Company
     - Address
     - Email
     - Phone Number  
2. Run the script — the bot will auto-fill and submit the form for each record.

---

### ✅ 4️⃣ Weather Reporter Bot

**Description:**  
Scrapes current weather for your city, generates a friendly weather report using GenAI, and emails it to you.

**Features:**  
- Scrapes weather data with TagUI  
- Uses Groq API for a natural language summary  
- Generates a PDF report  
- Sends weather summary by email

**How to Use:**  
1. Add `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, and `GROQ_API_KEY` to a `.env` file.  
2. Run the script.  
3. Enter:
   - Your city (e.g., Lahore, Karachi, Islamabad)
   - Your email address to receive the report

---

### ✅ 5️⃣ Weather Report Generator

**Description:**  
Fully automated weather report generator — scrapes weather from AccuWeather, creates a professional PDF report, and emails it.

**Features:**  
- Web scraping with TagUI  
- Generates daily, weekly, or monthly forecast in PDF  
- Sends a personalized email with the report attached

**How to Use:**  
1. Add `EMAIL_ADDRESS` and `EMAIL_PASSWORD` in a `.env` file.  
2. Run the script.  
3. Enter:
   - Your city (e.g., Lahore, Karachi, Islamabad)
   - Forecast type (today, daily, monthly)
   - Recipient email address

---

### ✅ 6️⃣ Quotes Scraper Bot

**Description:**  
Scrapes inspirational quotes from **[Quotes to Scrape](http://quotes.toscrape.com)** and saves them to a CSV file.

**Features:**  
- Uses `requests` to fetch HTML  
- Parses quotes & authors with BeautifulSoup  
- Saves results to `quotes.csv` using pandas

**How to Use:**  
1. Install requirements:
   ```bash
   pip install requests beautifulsoup4 pandas
