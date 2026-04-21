rule run_all:
    input:
        "graphs/all_programs.png",
        "graphs/total_fraud.png",
        "graphs/no_uc.png",
        "analysis/fraud_dollars_unemployment.txt",
        "analysis/fraud_percent_unemployment.txt",
        "analysis/fraud_percent_no_uc_unemployment.txt"

rule make_graphs:
    input:
        "data/clean_fraud_dollars_unemployment.csv",
        "data/clean_fraud_percent_unemployment.csv",
        "data/clean_fraud_percent_no_uc_unemployment.csv"
    output:
        "graphs/all_programs.png",
        "graphs/total_fraud.png",
        "graphs/no_uc.png"
    shell:
        "python scripts/make_graphs.py"

rule analysis:
    input:
        "data/clean_fraud_dollars_unemployment.csv",
        "data/clean_fraud_percent_unemployment.csv",
        "data/clean_fraud_percent_no_uc_unemployment.csv"
    output:
        "analysis/fraud_dollars_unemployment.txt",
        "analysis/fraud_percent_unemployment.txt",
        "analysis/fraud_percent_no_uc_unemployment.txt"
    shell:
        "python scripts/analysis.py"

rule combine_and_clean_data:
    input:
        "data/fraud_dollars_parsed.csv",
        "data/fraud_percent_parsed.csv",
        "data/unemployment_parsed.csv",
        "data/fraud_percent_no_uc_parsed.csv"
    output:
        "data/clean_fraud_dollars_unemployment.csv",
        "data/clean_fraud_percent_unemployment.csv",
        "data/clean_fraud_percent_no_uc_unemployment.csv"
    shell:
        "python scripts/combine_and_clean_data.py"

rule parse_data_fraud:
    input:
        "data/fraud_raw.xlsx"
    output:
        "data/fraud_dollars_parsed.csv",
        "data/fraud_percent_parsed.csv",
        "data/fraud_percent_no_uc_parsed.csv"
    shell:
        "python scripts/parse_data_fraud.py"

rule parse_data_labor:
    input:
        "data/labor_raw.xls"
    output:
        "data/unemployment_parsed.csv"
    shell:
        "python scripts/parse_data_labor.py"

rule fetch_data:
    output:
        "data/fraud_raw.xlsx",
        "data/labor_raw.xls"
    shell:
        "python scripts/fetch_data.py"