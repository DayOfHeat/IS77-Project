import pandas as pd
from sklearn.impute import KNNImputer

def mergeYearAndRollingPeriods(df_year, df_rolling, rollingOffset):
    yearStart = df_year.index.min()
    df_merged = df_year.copy()
    for i in range(len(df_year)):
        for column in df_rolling.columns:
            df_merged.loc[yearStart+i,column] = df_rolling.iloc[12*(i+rollingOffset):12*(i+rollingOffset+1)][column].mean()
    return df_merged

df_fraud_dollars = pd.read_csv("data/fraud_dollars_parsed.csv")
df_fraud_percent = pd.read_csv("data/fraud_percent_parsed.csv")
df_fraud_percent_no_uc = pd.read_csv("data/fraud_percent_no_uc_parsed.csv")

df_unemployment = pd.read_csv("data/unemployment_parsed.csv")
df_unemployment.set_index("period",inplace=True)

df_fraud_dollars_unemployment = mergeYearAndRollingPeriods(df_fraud_dollars, df_unemployment, 2006-1971)
df_fraud_percent_unemployment = mergeYearAndRollingPeriods(df_fraud_percent, df_unemployment, 2006-1971)
df_fraud_percent_no_uc_unemployment = mergeYearAndRollingPeriods(df_fraud_percent_no_uc, df_unemployment, 2006-1971)


imputer = KNNImputer(n_neighbors=2,weights="uniform")
for column in df_fraud_percent.columns:
    df_fraud_percent_unemployment[[column]] = imputer.fit_transform(df_fraud_percent_unemployment[[column]])
for column in df_fraud_dollars.columns:
    df_fraud_dollars_unemployment[[column]] = imputer.fit_transform(df_fraud_dollars_unemployment[[column]])
for column in df_fraud_percent_no_uc_unemployment.columns:
    df_fraud_percent_no_uc_unemployment[[column]] = imputer.fit_transform(df_fraud_percent_no_uc_unemployment[[column]])

df_fraud_percent_unemployment.to_csv("data/clean_fraud_percent_unemployment.csv")
df_fraud_dollars_unemployment.to_csv("data/clean_fraud_dollars_unemployment.csv")
df_fraud_percent_no_uc_unemployment.to_csv("data/clean_fraud_percent_no_uc_unemployment.csv")
