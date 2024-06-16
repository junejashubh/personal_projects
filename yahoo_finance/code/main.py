from utils import *
from getting_Nifty_50_symbols_selenium import *
from data_pulling_using_yfinance import *

config = read_config('../config/main_config.yml')

if config['selenium_reqs']['do_scape']:

    get_nifty_symbols(config)
    print('Completed Symbol Scraping')

do_yfinance_data_pull(config)

print('completed data pulling')

