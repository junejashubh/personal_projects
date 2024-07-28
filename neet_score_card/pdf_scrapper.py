import os
import pandas as pd
print('hi')
import pdfplumber
from joblib import Parallel, delayed
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

folder_path = '/Users/shubhamjuneja/vscode/personal_projects/neet_score_card/files_on_26-07'
files = os.listdir(folder_path)

def pdf_scrapper(file_name):
    c = pd.DataFrame()
    with pdfplumber.open(os.path.join(folder_path,file_name)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            index = text.index('Srlno.')
            new_text = text[index:].split('\n')
            b = [i.split(' ') for i in new_text]
            b = pd.DataFrame(b)
            b.columns = b.iloc[0,]
            b = b.iloc[1:,:]
            unique_cols = b.columns.unique()
            stacked_data = {}

        # Iterate over unique column names
            for col in b.columns.unique():
                # Stack columns with the same name
                stacked_data[col] = pd.concat([b.filter(like=col).iloc[:, i] for i in range(b.filter(like=col).shape[1])], ignore_index=True)

            # Create a new DataFrame from the stacked data
            stacked_df = pd.DataFrame(stacked_data)
            stacked_df = stacked_df.loc[~stacked_df['Srlno.'].isna(),]
            c = pd.concat([c,stacked_df],axis=0).reset_index(drop=True)
            id = file_name.split('.')[0]
            c['center_num'] = id
            c['center_num'] = c['center_num'].astype('int64')
            c = c[['center_num','Srlno.','Marks']]
    return c

final_results = Parallel(n_jobs=8)(delayed(pdf_scrapper)(i) for i in files)
final_df = pd.concat(final_results,axis =0).reset_index(drop=True)
mappings = pd.read_csv('/Users/shubhamjuneja/vscode/personal_projects/neet_score_card/op/all_mapping.csv')

final_df_1 = mappings.merge(final_df,on='center_num',how='left')

print(final_df.dtypes)
print(mappings.dtypes)
print(final_df_1.shape)
final_df_1.to_csv('/Users/shubhamjuneja/vscode/personal_projects/neet_score_card/op/all_neet_marks_2607.csv',index = False)






