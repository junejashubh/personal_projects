import pandas as pd 
import numpy as np 
from utils import *
import os
from selenium import webdriver
import shutil
import time

config = read_config('../config/main_config.yml')

website = config['selenium_reqs']['website_path']
driver_path = config['selenium_reqs']['driver_path']
download_dir = config['selenium_reqs']['downloaded_file_location']

before_download = os.listdir(download_dir)
driver = webdriver.Firefox(executable_path=driver_path)
driver.get(website)
# button = driver.find_element_by_xpath('//span[@id="dwldcsv"]')
# button.click()
#time.sleep(10)
#after_download = os.listdir(download_dir)

# Identify the newly downloaded file
#new_file = list(set(after_download) - set(before_download))
#print(new_file)