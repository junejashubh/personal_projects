from bs4 import BeautifulSoup
import requests
import os

main_website = 'https://subslikescript.com/'
step1_link = 'movies'
results = requests.get(main_website+step1_link)
contents = results.text
soup = BeautifulSoup(contents,'lxml')

# getting root object 
root = soup.find('article',class_ = 'main-article').find('ul',class_='scripts-list')
# getting all titles displayed
titles = root.find_all('li')
titles = [i.get_text() for i in titles]

# get links for all titles getting displayed
'''
since href is a link we need to us href get method to extract link from html content
'''
links = root.find_all('a')
links = [i.get('href') for i in links]

for i in range(len(links)):
    results = requests.get(main_website+links[i])
    contents = results.text
    soup = BeautifulSoup(contents,'lxml')

    #getting transcripts
    transcript = soup.find('article',class_ = 'main-article').find('div', class_='full-script').get_text()

    with open(os.path.join('outputs',f'{titles[i]}.txt'),'w') as file:
        file.write(transcript)
    
    print(f'completed writing {titles[i]}')