import os
import pandas as pd 
import numpy as np 
import yfinance as yf
from datetime import datetime

ip_path = r'inputs/input_for_yfinance'
mappings = pd.read_csv(os.path.join(ip_path,'company_to_symbol_mapping.csv'))
mappings.dropna(inplace=True)

symbol_to_company = dict(zip(mappings['Symbols'],mappings['Company_name']))
symbol_list = sorted(list(set(mappings['Symbols'])))

for i in symbol_list:
# Fetch historical stock price data from inception to current date
    stock_data = yf.download(i, start="1900-01-01", end=datetime.today().strftime('%Y-%m-%d')).reset_index()
    stock_data.to_csv(os.path.join(r'inputs/input_for_modeling',f'{symbol_to_company[i]}.csv'),index=False)



