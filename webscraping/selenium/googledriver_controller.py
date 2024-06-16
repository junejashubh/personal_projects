from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Automatically downloads the appropriate ChromeDriver and gets its path
chrome_driver_path = ChromeDriverManager().install()

# Set up Chrome options if needed
chrome_options = webdriver.ChromeOptions()

# Initialize the WebDriver with the path to ChromeDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.get("https://finance.yahoo.com")