import os
import pandas as pd 
import numpy as np 
import yfinance as yf
from datetime import datetime
import shutil

def do_yfinance_data_pull(config):
    mappings = pd.read_csv(config['selenium_reqs']['op_path_n_name'])
    mappings.dropna(inplace=True)

    symbol_to_company = dict(zip(mappings['Symbols'],mappings['Company_name']))
    symbol_list = sorted(list(set(mappings['Symbols'])))

    for i in symbol_list:
    # Fetch historical stock price data from inception to current date
        stock_data = yf.download(i, start="1900-01-01", end=datetime.today().strftime('%Y-%m-%d')).reset_index()
        stock_data.to_csv(os.path.join(config['yfinance_reqs']['op_path'],f'{symbol_to_company[i]}.csv'),index=False)

    shutil.rmtree(config['modeling_reqs']['m_input_path'])
    shutil.copytree(config['yfinance_reqs']['op_path'], config['modeling_reqs']['m_input_path'])