from selenium import webdriver
import pandas as pd
import os
import time

website = 'https://www.audible.com/search?ipRedirectOverride=true&overrideBaseCountry=true&overrideBaseCountry=true&ipRedirectOverride=true&ref_pageloadid=not_applicable&pf_rd_p=ba485dc1-f49f-438a-92e0-9e8cdea09e44&pf_rd_r=196MADHM8HQBJYBTG0ZY&pageLoadId=DPtIsI41SGxMBkVm&creativeId=a2d315be-e6e7-4f3c-849a-e47e680dcd54'
path = '/Users/shubhamjuneja/vscode/personal_projects/webscraping/selenium/chromedriver-mac-x64/chromedriver'

driver = webdriver.Chrome(executable_path=path)
driver.get(website)
container = driver.find_elements_by_xpath('//div[@class="adbl-impression-container "]//li[@aria-label]')

titles = []
subtitles = []
author_label = []
narrator_label = []
series_label = []
run_time_label = []
release_data = []
language_label = []
rating_label = []
final_dict = {'titles' : [],
            'subtitles' : [],
            'author_label' : [],
            'narrator_label' : [],
            'series_label' :[],
            'run_time_label' : [],
            'release_data' : [],
            'language_label' : [],
            'rating_label' : []}

for i in range(0,len(container)):
    try:
        title = container[i].find_element_by_xpath('.//h3[contains(@class,"heading")]').text
        final_dict['titles'].append(title)
    except:
        final_dict['titles'].append('no title')
    try:
        subtitle = container[i].find_element_by_xpath('.//li[contains(@class,"subtitle")]').text
        final_dict['subtitles'].append(subtitle)
    except:
        final_dict['subtitles'].append('no subtitle')
    try:
        author = container[i].find_element_by_xpath('.//li[contains(@class,"author")]').text
        final_dict['author_label'].append(author)
    except:
        final_dict['author_label'].append('no author')
    try:
        narrator = container[i].find_element_by_xpath('.//li[contains(@class,"narrator")]').text
        final_dict['narrator_label'].append(narrator)
    except:
         final_dict['narrator_label'].append('no narrator')
    try:
        series = container[i].find_element_by_xpath('.//li[contains(@class,"series")]').text
        final_dict['series_label'].append(series)
    except:
        final_dict['series_label'].append('no series')
    try:
        run_time = container[i].find_element_by_xpath('.//li[contains(@class,"runtime")]').text
        final_dict['run_time_label'].append(run_time)
    except:
        final_dict['run_time_label'].append('no run_time')
    try:
        release = container[i].find_element_by_xpath('.//li[contains(@class,"release")]').text
        final_dict['release_data'].append(release)
    except:
        final_dict['release_data'].append('no release date')
    try:
        language = container[i].find_element_by_xpath('.//li[contains(@class,"language")]').text
        final_dict['language_label'].append(language)
    except:
        final_dict['language_label'].append('no language')
    try:
        rating = container[i].find_element_by_xpath('.//li[contains(@class,"rating")]//span[contains(@class,"secondary")]').text
        final_dict['rating_label'].append(rating)
    except:
        final_dict['rating_label'].append('no rating')



final_data = pd.DataFrame(final_dict)
final_data.to_csv(os.path.join('outputs','all_ratings.csv'),index=False)

#print(driver.find_element_by_xpath('//div[@class="adbl-impression-container "]//li[@aria-label]//h3[contains(@class,"heading")]').text)
driver.quit()

