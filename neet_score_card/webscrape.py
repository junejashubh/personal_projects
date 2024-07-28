import pandas as pd 
import numpy as np 
import os
from selenium import webdriver
import shutil
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math

website = 'https://neet.ntaonline.in/frontend/web/common-scorecard/index'
chrome_driver_path = ChromeDriverManager().install()

    # Set up Chrome options if needed
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option('prefs', {
   "download.default_directory": '/Users/shubhamjuneja/vscode/personal_projects/neet_score_card/files_on_26-07',  # Change default directory for downloads
    "download.prompt_for_download": False,       # To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True   # It will not show PDF directly in chrome
})

# Initialize the WebDriver with the path to ChromeDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.get(website)

dd = driver.find_element_by_xpath('//select[@name = "scorecardData_length"]/option[@value="500"]')
dd.click()
time.sleep(5)
#print(driver.find_element_by_xpath('//tr[@class="odd"][1]/td[2]').text)
all_centers_odd = driver.find_elements_by_xpath('//tr[@class="odd"]')
all_centers_even = driver.find_elements_by_xpath('//tr[@class="even"]')
#time.sleep(10)
errored_path = []
i = 1
a = 1
all_state = []
center_city = []
all_center_name = []
all_center_num =[]

while i <= 4750:
    
    try: 
        wait = WebDriverWait(driver, 100)
        if a%2 == 0:
            path = f'//tr[@class="even"][{a/2}]/td[6]/a[@target="_blank"]'
            state = driver.find_element_by_xpath(f'//tr[@class="even"][{a/2}]/td[2]').text
            city = driver.find_element_by_xpath(f'//tr[@class="even"][{a/2}]/td[3]').text
            center_name = driver.find_element_by_xpath(f'//tr[@class="even"][{a/2}]/td[4]').text
            center_num = driver.find_element_by_xpath(f'//tr[@class="even"][{a/2}]/td[5]').text

        else:
            path = f'//tr[@class="odd"][{math.ceil(a/2)}]/td[6]/a[@target="_blank"]'
            state = driver.find_element_by_xpath(f'//tr[@class="odd"][{math.ceil(a/2)}]/td[2]').text
            city = driver.find_element_by_xpath(f'//tr[@class="odd"][{math.ceil(a/2)}]/td[3]').text
            center_name = driver.find_element_by_xpath(f'//tr[@class="odd"][{math.ceil(a/2)}]/td[4]').text
            center_num = driver.find_element_by_xpath(f'//tr[@class="odd"][{math.ceil(a/2)}]/td[5]').text

        all_state.append(state)
        center_city.append(city)
        all_center_name.append(center_name)
        all_center_num.append(center_num)
       
        element = wait.until(EC.presence_of_element_located((By.XPATH, path)))
        element = wait.until(EC.visibility_of_element_located((By.XPATH, path)))

    # Scroll the element into view
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, path)))

    # # Click the button using JavaScript
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)

    except:
        print(i)
        time.sleep(5)
        errored_path.append(path)

    if i%500 ==0:
        print('try_next')
        next_button = driver.find_element_by_xpath('//li[@class="paginate_button page-item next"]/a[@class = "page-link"]')
        next_button.click()
        time.sleep(10)
        a = 1
    else:
        a = a+1
    
    i = i+1

final_df = pd.DataFrame({'state':all_state,'city':center_city,
                         'center_name':all_center_name,'center_num':all_center_num})

final_df.to_csv('/Users/shubhamjuneja/vscode/personal_projects/neet_score_card/op/all_mapping.csv',index=False)
print('after 1st try')
for i in errored_path:
    try: 
        path = i
        print(path)
        button = driver.find_element_by_xpath(path)
        time.sleep(5)
        button.click()
    except:
        print(i)

    
    

