from selenium import webdriver
import pandas as pd
import os
import time

raw_link = 'https://finance.yahoo.com'
initial_link = '/quote/%5ENSEI?.tsrc=fin-srch'
website = f'{raw_link}{initial_link}'
path = '/Users/shubhamjuneja/vscode/personal_projects/webscraping/selenium/chromedriver-mac-x64/chromedriver'

driver = webdriver.Chrome(executable_path=path)
driver.get(website)
button = driver.find_element_by_xpath('//div[@id = "YDC-Lead"]//div[contains(@id,"Lead-6")]//li[@data-test="COMPONENTS"]')
find_href_link = button.find_element_by_xpath('./a').get_attribute("href")
button.click()
time.sleep(10)
driver.get(find_href_link)

all_symbols = driver.find_elements_by_xpath('//tbody//td[contains(@class,"Ta(start)")][1]')
all_symbols = [i.text for i in all_symbols]

all_company_names = driver.find_elements_by_xpath('//tbody//td[contains(@class,"Ta(start)")][2]')
all_company_names = [i.text for i in all_company_names]

driver.quit()
req_df = pd.DataFrame({'Company_name':all_company_names,'Symbols':all_symbols})
req_df.to_csv(os.path.join('inputs','input_for_yfinance','company_to_symbol_mapping.csv'),index=False)
