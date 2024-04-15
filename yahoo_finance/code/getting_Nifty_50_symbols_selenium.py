import pandas as pd 
import numpy as np 
from utils import *
import os
from selenium import webdriver
import shutil
import time

def get_nifty_symbols(config):
    raw_link = config['selenium_reqs']['website_path']
    initial_link = '/quote/%5ENSEI?.tsrc=fin-srch'
    website = f'{raw_link}{initial_link}'
    path = config['selenium_reqs']['driver_path']

    driver = webdriver.Chrome(executable_path=path)
    driver.get(website)
    ref_1 = driver.find_element_by_xpath('//ul[@class="nav-list svelte-1o7i3hz"]')
    find_href_link = ref_1.find_element_by_xpath('.//a[@category="components"]').get_attribute("href")
    button = ref_1.find_element_by_xpath('.//a[@category="components"]')
    button.click()
    time.sleep(10)
    driver.get(find_href_link)

    all_symbols = driver.find_elements_by_xpath('//td[@class="cell  svelte-1xjtgc3"][1]')
    all_symbols = [i.text for i in all_symbols]

    all_company_names = driver.find_elements_by_xpath('//td[@class="cell  tw-text-left svelte-1xjtgc3"][1]')
    all_company_names = [i.text for i in all_company_names]

    driver.quit()
    req_df = pd.DataFrame({'Company_name':all_company_names,'Symbols':all_symbols})
    req_df.to_csv(os.path.join(config['selenium_reqs']['op_path_n_name']),index=False)

    shutil.copy2(config['selenium_reqs']['op_path_n_name'], config['yfinance_reqs']['input_path'])

if __name__ == "__main__":
    config = read_config('../config/main_config.yml')
    get_nifty_symbols(config)
