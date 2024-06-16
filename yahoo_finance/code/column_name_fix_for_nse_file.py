import pandas as pd

a = pd.read_csv("/Users/shubhamjuneja/vscode/personal_projects/yahoo_finance/outputs/output_from_webscrape/MW-NIFTY-50-16-Jun-2024.csv")
modified_words = [word.replace(' \n', '') for word in a.columns]
modified_words = [word.capitalize() for word in modified_words]
print(modified_words)
a.columns = modified_words

a.rename(columns={'Symbol':'Symbols'},inplace=True)

a.to_csv("/Users/shubhamjuneja/vscode/personal_projects/yahoo_finance/outputs/output_from_webscrape/MW-NIFTY-50-16-Jun-2024.csv",index = False)