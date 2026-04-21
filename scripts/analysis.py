import pandas as pd
import os
import statsmodels.api as sm

if not os.path.exists("analysis"):
    os.makedirs("analysis", exist_ok=True)

df_fraud_percent_unemployment = pd.read_csv("data/clean_fraud_percent_unemployment.csv")
df_fraud_percent_unemployment.set_index("Year",inplace=True)

percent_model = sm.OLS(exog=sm.add_constant(df_fraud_percent_unemployment["16+ Unemployment Rate"]),endog=df_fraud_percent_unemployment["All Benefits Fraud"]).fit()
open("analysis/fraud_percent_unemployment.txt","w").write(str(percent_model.summary()))

df_fraud_dollars_unemployment = pd.read_csv("data/clean_fraud_dollars_unemployment.csv")
df_fraud_dollars_unemployment.set_index("Year",inplace=True)

dollars_model = sm.OLS(exog=sm.add_constant(df_fraud_dollars_unemployment["16+ Unemployment Rate"]),endog=df_fraud_dollars_unemployment["All Benefits Fraud"]).fit()
open("analysis/fraud_dollars_unemployment.txt","w").write(str(dollars_model.summary()))

df_fraud_percent_no_uc_unemployment = pd.read_csv("data/clean_fraud_percent_no_uc_unemployment.csv")
df_fraud_percent_no_uc_unemployment.set_index("Year",inplace=True)

percent_no_uc_model = sm.OLS(exog=sm.add_constant(df_fraud_percent_no_uc_unemployment["16+ Unemployment Rate"]),endog=df_fraud_percent_no_uc_unemployment["Benefits Fraud"]).fit()
open("analysis/fraud_percent_no_uc_unemployment.txt","w").write(str(percent_no_uc_model.summary()))