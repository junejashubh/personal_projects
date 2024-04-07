from selenium import webdriver
import pandas as pd
import os
from selenium.webdriver.support.ui import Select
import time

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/shubhamjuneja/vscode/personal_projects/webscraping/selenium/chromedriver-mac-x64/chromedriver'

driver = webdriver.Chrome(executable_path=path)
driver.get(website)

button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
button.click()

dropdown_reference = driver.find_element_by_xpath("// select[@id = 'country']")
all_options_in_dropdown = dropdown_reference.find_elements_by_xpath('./option')
all_options_in_dropdown_names = [i.text for i in all_options_in_dropdown]

country_dict = {}
for country_names_ind in range(len(all_options_in_dropdown_names)):
    try:
        req_selection = dropdown_reference.find_element_by_xpath(f"./option[@label='{all_options_in_dropdown_names[country_names_ind]}']")
        req_selection.click()
        time.sleep(5)

        league_dropdown_ref = driver.find_element_by_xpath("// select[@id = 'league']")
        all_league_dd = league_dropdown_ref.find_elements_by_xpath('./option')
        all_league_dd_names = [i.text for i in all_league_dd]
        season_dict = {}
        for league_index in range(len(all_league_dd_names)):
            req_league_selection = league_dropdown_ref.find_element_by_xpath(f"./option[@label='{all_league_dd_names[league_index]}']")
            req_league_selection.click()
            time.sleep(5)

            season_dropdown_ref = driver.find_element_by_xpath("// select[@id = 'season']")
            season_dd = season_dropdown_ref.find_elements_by_xpath('./option')
            season_dd_names = [i.text for i in season_dd]
            season_dict[all_league_dd_names[league_index]] = season_dd_names

        country_dict[all_options_in_dropdown_names[country_names_ind]] = season_dict
    except:
        print(f"issue in {all_options_in_dropdown_names[country_names_ind]} {all_league_dd_names[league_index]}")

driver.quit()
df = pd.DataFrame.from_dict(country_dict, orient='index')

# Stack the DataFrame to move the inner dictionary keys to a column
df = df.stack().reset_index()

# Rename columns
df.columns = ['Country', 'League', 'Season']

# Display the resulting DataFrame

df.to_csv(os.path.join('outputs','teams_leagues_seasons.csv'),index=False)