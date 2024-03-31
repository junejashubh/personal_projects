from bs4 import BeautifulSoup
import requests
import os

main_website = 'https://subslikescript.com/'
step1_link = 'movies'
results = requests.get(main_website+step1_link)
contents = results.text
soup = BeautifulSoup(contents,'lxml')

#getting paginations
all_pagination = soup.find('ul',class_='pagination').find_all('li',class_= 'page-item')
num_pages = all_pagination[-2].text

all_titles = []
all_links = []
for i in range(1,int(num_pages)+1)[0:10]:
    step2_link = main_website+step1_link+f'?page={i}'
    print(step2_link)
    page_results = requests.get(step2_link)
    contents = page_results.text
    soup = BeautifulSoup(contents,'lxml')
    root = soup.find('article',class_ = 'main-article').find('ul',class_='scripts-list')
    try:
    # getting all titles displayed
        titles = root.find_all('li')
        titles = [i1.get_text() for i1 in titles]
        all_titles = all_titles+titles
        # get links for all titles getting displayed
        '''
        since href is a link we need to us href get method to extract link from html content
        '''
        links = root.find_all('a',)
        links = [i1.get('href') for i1 in links]
        all_links = all_links+links

        # getting transcripts from the extracted links
        for i2 in range(len(links)):
            try:
                results = requests.get(main_website+links[i2])
                contents = results.text
                soup = BeautifulSoup(contents,'lxml')

                #getting transcripts
                transcript = soup.find('article',class_ = 'main-article').find('div', class_='full-script').get_text()

                with open(os.path.join('outputs',f'{titles[i2]}.txt'),'w') as file:
                    file.write(transcript)
                
                print(f'completed writing {titles[i2]}')
            except:
                print(f'something broke in page {i} for movie {i2}')
    except:
        print(f'something broke in page{i}')
        pass



# getting root object 
root = soup.find('article',class_ = 'main-article').find('ul',class_='scripts-list')