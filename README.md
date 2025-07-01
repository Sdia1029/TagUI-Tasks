# 🗂️ Automation Projects Collection

This repository contains **four** mini automation projects developed using **Python**, **TagUI**, **GenAI**, and **RPA** tools. Each project shows practical automation for real-world tasks.

---

## 📌 Projects

### 1️⃣ Job Scraper Bot

**Description:**  
Scrapes jobs from [Mustakbil.com](https://www.mustakbil.com), filters results using GenAI, and automatically emails the matching jobs.

**Features:**
- Web scraping with TagUI
- Uses GenAI (Groq API) for smart filtering
- Sends email with filtered results

**How to Use:**
1. Add `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, and `GROQ_API_KEY` in a `.env` file.
2. Run the script.
3. Enter:
   - Job title
   - City
   - Recipient email
4. The bot scrapes, filters, and sends the jobs by email.

---

### 2️⃣ News Scraper Bot

**Description:**  
Searches for news on [Dawn.com](https://www.dawn.com) for any topic you enter.

**Features:**
- Automated search using TagUI
- Custom topic input

**How to Use:**
1. Run the script.
2. Enter your topic.
3. The bot opens Dawn.com, searches, and waits for you to check the results.

---

### 3️⃣ Data Entry Bot

**Description:**  
Automatically fills out forms on [RPA Challenge](https://rpachallenge.com) using data from an Excel or CSV file.

**Features:**
- Reads `challenge.xlsx` with pandas
- Uses TagUI (RPA) to fill & submit forms for each record

**How to Use:**
1. Place `challenge.xlsx` in the project folder.
2. Make sure it has columns:
   - First Name
   - Last Name
   - Company Name
   - Role in Company
   - Address
   - Email
   - Phone Number
3. Run the script — the bot will fill and submit the form automatically.

---

### 4️⃣ Weather Reporter Bot

**Description:**  
Scrapes the current weather for your city, generates a friendly weather report using GenAI, and emails it to you.

**Features:**
- Scrapes weather data with TagUI
- Uses GenAI (Groq API) for natural language report
- Sends weather summary by email

**How to Use:**
1. Add `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, and `GROQ_API_KEY` in a `.env` file.
2. Run the script.
3. Enter:
   - Your city (Lahore, Karachi, or Islamabad)
   - Your email address to receive the report
4. The bot fetches the weather, generates a report, and emails it to you.

---

## ⚙️ Requirements

- Python 3.x

**Install Dependencies:**
```bash
pip install tagui rpa pandas openai python-dotenv
