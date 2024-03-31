from selenium import webdriver
import pandas as pd
import os

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/shubhamjuneja/vscode/personal_projects/webscraping/selenium/chromedriver-mac-x64/chromedriver'

driver = webdriver.Chrome(executable_path=path)
driver.get(website)

button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
button.click()
all_teams = driver.find_elements_by_xpath('//div[@class="col-lg-3 col-sm-6 col-xs-12 ng-binding"]')
all_teams = [i.text.replace('/', '') for i in all_teams]

final_dict = {}
for i in range(1,len(all_teams)+1):
    req_rows = driver.find_elements_by_xpath(f'//div[@data-ng-repeat="team in :refreshStats:vm.teams"][{i}]//tr')
    date = []
    home = []
    score = []
    away = []
    for i1 in range(len(req_rows)):
        date.append(req_rows[i1].find_element_by_xpath('./td[1]').text)
        home.append(req_rows[i1].find_element_by_xpath('./td[2]').text)
        score.append(req_rows[i1].find_element_by_xpath('./td[3]').text)
        away.append(req_rows[i1].find_element_by_xpath('./td[4]').text)
    
    final_dict[all_teams[i-1]] = pd.DataFrame({'date':date,'home':home,'score':score,'away':away})
    final_dict[all_teams[i-1]].to_csv(os.path.join('outputs',f'{all_teams[i-1]}.csv'),index = False)


driver.quit()