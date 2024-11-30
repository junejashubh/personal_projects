import pandas as pd
import numpy as np
import os
import openpyxl
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

input_data = '/Users/shubhamjuneja/vscode/personal_projects/Induction_motor_fault_detection/Data/singlephase data sets healthy n faulty.xlsx'
workbook = openpyxl.load_workbook(input_data, read_only=True)

# Get all sheet names
sheet_names = pd.DataFrame({'sheetname':workbook.sheetnames})
sheet_names = sheet_names.loc[~sheet_names['sheetname'].str.contains('Sheet'),].reset_index(drop=True)

req_data = pd.DataFrame()
for i in sheet_names['sheetname']: 
    sheet_data = pd.read_excel(input_data,sheet_name=i)
    sheet_data['fault'] = i
    req_data = pd.concat([req_data,sheet_data],axis = 0).reset_index(drop=True)

req_data.drop(columns='S.NO',inplace=True)

label_encoder = LabelEncoder()
req_data['label_encoded'] = label_encoder.fit_transform(req_data['fault'])

idvs = req_data[['IRMS', 'X', 'Y', 'Z', 'TEMP', 'Vrms']]
dv = req_data['label_encoded']

X_train, X_test, y_train, y_test = train_test_split(idvs, dv, test_size=0.3, random_state=42)

# Step 4: Standardize the feature data (Optional but recommended for Logistic Regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Step 6: Predict and Evaluate
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy * 100:.2f}%')

# Optional: Reverse the label encoding for the predictions
predicted_labels = label_encoder.inverse_transform(y_pred)
#print("Predicted Labels:", predicted_labels)

y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

X_train['Actual'] = y_train
X_train['Pred'] = y_train_pred
X_test['Actual'] = y_test
X_test['Pred'] = y_test_pred

final_data = pd.concat([X_train,X_test],axis =0).reset_index(drop=True)
final_data['Actual_label'] = label_encoder.inverse_transform(final_data['Actual'])
final_data['Pred_label'] = label_encoder.inverse_transform(final_data['Pred'])

accuracy = accuracy_score(final_data['Actual'],final_data['Pred'])

print("Accuracy; ",accuracy)
