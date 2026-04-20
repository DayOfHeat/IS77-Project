import pandas as pd
import numpy as np

df_raw_fraud_dollars = pd.read_excel(io="data/fraud_raw.xlsx",sheet_name="Table_1",engine="calamine",skiprows=[0,1,2,4,5,11,12,13],nrows=145)
df_raw_fraud_dollars.drop(columns=["Unnamed: 0"], inplace=True)
df_raw_fraud_dollars = df_raw_fraud_dollars.T
df_fraud_dollars = pd.DataFrame()
for i in df_raw_fraud_dollars:
    itemName = df_raw_fraud_dollars[i][' ']
    if pd.isna(itemName):
        continue
    if itemName.startswith("Last measured"):
        continue
    if itemName.startswith("Benefits"):
        continue
    if itemName.strip() == "":
        continue
    itemName = itemName.split("note")[0]
    df_fraud_dollars = df_fraud_dollars.assign(**{itemName+"Fraud":0,itemName+"Claimant Error":0,itemName+"Official Error":0,itemName+"Total":0,itemName+"Expenditure": 0})
found2024 = False
previousRow = map
df_fraud_dollars["Year"] = []
df_fraud_dollars.set_index("Year", inplace=True)
for row in df_raw_fraud_dollars.itertuples():
    yearName = row[0]
    if yearName.startswith("Unnamed:"):
        previousRow = row
        continue
    if yearName.strip() == "":
        previousRow = row
        continue
    yearName = yearName.split(" ")[1].split("\n")[0]
    if yearName == "2024":
        if not found2024:
            found2024 = True
        else:
            continue
    validColumns = []
    for column in previousRow:
        if not (type(column) is int or type(column) is float or column in ["w","x","z"]):
            continue
        if pd.isna(column):
            continue
        if column in ["w","x","z"]:
            column = 0
        validColumns.append(column)
    df_fraud_dollars.loc[int(yearName)] = validColumns
    previousRow = row
df_fraud_dollars.to_csv("data/fraud_dollars_parsed.csv")

df_raw_fraud_percent = pd.read_excel(io="data/fraud_raw.xlsx",sheet_name="Table_2",engine="calamine",skiprows=[0,1,2,4,5,11,12,13],nrows=145)
df_raw_fraud_percent.drop(columns=["Unnamed: 0"], inplace=True)
df_raw_fraud_percent = df_raw_fraud_percent.T
df_fraud_percent = pd.DataFrame()
for i in df_raw_fraud_percent:
    itemName = df_raw_fraud_percent[i][' ']
    if pd.isna(itemName):
        continue
    if itemName.startswith("Last measured"):
        continue
    if itemName.startswith("Benefits"):
        continue
    if itemName.strip() == "":
        continue
    itemName = itemName.split("note")[0]
    if itemName[-1] != ' ':
        itemName += ' '
    df_fraud_percent = df_fraud_percent.assign(**{itemName+"Fraud":0,itemName+"Claimant Error":0,itemName+"Official Error":0,itemName+"Total":0})
found2024 = False
previousRow = map
df_fraud_percent["Year"] = []
df_fraud_percent.set_index("Year", inplace=True)
df_fraud_percent
for row in df_raw_fraud_percent.itertuples():
    
    yearName = row[0]
    if yearName.startswith("Unnamed:"):
        previousRow = row
        continue
    if yearName.strip() == "":
        previousRow = row
        continue
    yearName = yearName.split(" ")[1].split("\n")[0]
    if yearName == "2024":
        if not found2024:
            found2024 = True
        else:
            continue
    validColumns = []
    invalidColumns = []
    for column in previousRow:
        if type(column) is str and '*' in column:
            column = float(column.split(' ')[1]) # fixes issue some have with stray "*" or "*'" instances sometimes being part of the excel formatting and sometimes as part of the field
        if not (type(column) is int or type(column) is float or column in ["w","x","z"]):
            invalidColumns.append(column)
            continue
        if pd.isna(column):
            invalidColumns.append(column)
            continue
        if column in ["x","z"]:
            column = 0
        if column == "w":
            column = np.nan
        validColumns.append(column)
    df_fraud_percent.loc[int(yearName)] = validColumns
    previousRow = row
df_fraud_percent.to_csv("data/fraud_percent_parsed.csv")

df_fraud_percent_no_uc = pd.DataFrame()
df_fraud_percent_no_uc["Benefits Fraud"] = 100*(df_fraud_dollars["All Benefits Fraud"] - df_fraud_dollars["Universal Credit Fraud"])/(df_fraud_dollars["All Benefits Expenditure"] - df_fraud_dollars["Universal Credit Expenditure"])
df_fraud_percent_no_uc.to_csv("data/fraud_percent_no_uc_parsed.csv")