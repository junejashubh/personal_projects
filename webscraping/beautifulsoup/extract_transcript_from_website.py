from bs4 import BeautifulSoup
import requests
import os

website = 'https://subslikescript.com/movie/Titanic-46435'
results = requests.get(website)
contents = results.text
soup = BeautifulSoup(contents,'lxml')
# getting title of the movie
title = soup.find('article',class_ = 'main-article').find('h1').get_text()

#getting transcript
transcript = soup.find('article',class_ = 'main-article').find('div', class_='full-script').get_text()

with open(os.path.join('outputs',f'{title}.txt'),'w') as file:
    file.write(transcript)
