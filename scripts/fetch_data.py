import os
import requests

fraud_url = "https://assets.publishing.service.gov.uk/media/684a84bc38cd4b88e2c7db57/fraud-and-error-statistics-release-2024-2025-estimates-data-tables.xlsx"

labor_url = "https://www.ons.gov.uk/file?uri=/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/datasets/summaryoflabourmarketstatistics/current/a01mar2026.xls"


if not os.path.exists("data"):
    os.makedirs("data", exist_ok=True)

response = requests.get(fraud_url)
with open("data/fraud_raw.xlsx", "wb") as f:
    f.write(response.content)

response = requests.get(labor_url)
with open("data/labor_raw.xls", "wb") as f:
    f.write(response.content)