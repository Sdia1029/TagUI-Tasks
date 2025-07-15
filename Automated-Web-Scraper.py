import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'http://quotes.toscrape.com'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('div', class_='quote')

all_quotes = []
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    all_quotes.append({'quote': text, 'author': author})

df = pd.DataFrame(all_quotes)
df.to_csv('quotes.csv', index=False)

print("Quotes saved to quotes.csv")
