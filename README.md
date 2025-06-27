# 🗂️ Automation Projects Collection

This repository contains **three mini automation projects** developed using **Python**, **TagUI**, **GenAI**, and **RPA** tools. Each project demonstrates practical automation for real-world tasks.

---

## 📌 Projects

### 1️⃣ Job Scraper Bot

**Description:**  
Scrapes jobs from [Mustakbil.com](https://www.mustakbil.com), filters results using **GenAI**, and automatically emails the matching jobs.

**Key Features:**  
- Web scraping with TagUI  
- Uses GenAI (Groq API) for smart filtering  
- Sends email with filtered results

**How to Use:**  
1. Add your `EMAIL_ADDRESS`, `EMAIL_PASSWORD` & `GROQ_API_KEY` in a `.env` file.
2. Run the script.
3. Enter:
   - Job title
   - City
   - Recipient email
4. The bot scrapes, filters, and emails the jobs.

---

### 2️⃣ News Scraper Bot

**Description:**  
Searches for news on [Dawn.com](https://www.dawn.com) for any topic you enter.

**Key Features:**  
- Automated search with TagUI  
- Custom topic input

**How to Use:**  
1. Run the script.  
2. Enter the topic to search for.  
3. The bot opens Dawn.com, searches, and waits for you to review the results.

---

### 3️⃣ Data Entry Bot

**Description:**  
Automatically fills out forms on [RPA Challenge](http://www.rpachallenge.com) using data from an Excel or CSV file.

**Key Features:**  
- Reads `challenge.xlsx` with **pandas**  
- Uses TagUI (RPA) to fill & submit the form for each record

**How to Use:**  
1. Place `challenge.xlsx` in the project folder.
2. Make sure the file has:
   - First Name
   - Last Name
   - Company Name
   - Role in Company
   - Address
   - Email
   - Phone Number
3. Run the script and watch it complete the form automatically.

---

## ⚙️ Requirements

- Python 3.x
- Libraries:  
  - `tagui` or `rpa`  
  - `pandas`  
  - `openai`  
  - `python-dotenv`

**Install dependencies:**  
```bash
pip install tagui rpa pandas openai python-dotenv
