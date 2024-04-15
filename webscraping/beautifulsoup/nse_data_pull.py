from bs4 import BeautifulSoup
import requests
import os

website = 'https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%2050'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
response = requests.get(website, headers=headers)
#results = requests.get(website)
print('got the website')
contents = response.text
soup = BeautifulSoup(contents,'html.parser')
print(soup)