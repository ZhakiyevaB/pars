import requests
from bs4 import BeautifulSoup

url = "https://tengrinews.kz/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

title = soup.find_all('span', class_='tn-main-news-title')

rose = soup.find_all('span', class_='tn-article-title')

for quote in rose:
    print(quote.text)

for quote in title:
    print(quote.text)
