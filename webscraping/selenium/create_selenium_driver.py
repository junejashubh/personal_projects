from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/shubhamjuneja/vscode/personal_projects/webscraping/selenium/chromedriver-mac-x64/chromedriver'

driver = webdriver.Chrome(executable_path=path)
driver.get(website)

driver.quit()