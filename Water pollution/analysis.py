
import pandas as pd  

data = pd.read_csv(r'/Users/shubhamjuneja/vscode/personal_projects/Water pollution/water_pollution_dataset.csv')

#print(data.groupby('City')['pH Level'].mean().reset_index().sort_values('pH Level'))

df = data.loc[data['Country']=='USA',]
print(df.groupby('Water Source')['Dissolved Oxygen (mg/L)'].mean().reset_index().sort_values('Dissolved Oxygen (mg/L)',ascending=False))
