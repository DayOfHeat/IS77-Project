import xlrd
import re
import pandas as pd

wb = xlrd.open_workbook("data/labor_raw.xls")

def xldate_to_str(v, datemode):
    try:
        tup = xlrd.xldate_as_tuple(float(v), datemode)
        if tup[0]:
            return datetime.date(*tup[:3]).isoformat()
    except:
        pass
    try:
        return str(int(float(v)))
    except:
        return str(v).strip()

def is_valid_period(v):
    v = str(v).strip()
    return bool(re.match(
        r"^([A-Za-z]{3}-[A-Za-z]{3}\s+\d{4}"
        r"|[A-Za-z]{3}\s+\d{2,4}"
        r"|[A-Za-z]+\s+\d{4}$"
        r"|\d{4}-\d{2}-\d{2}"
        r"|\d{4}$"
        r"|[A-Z]\d{8,})", v))

def build_col_names(sh, header_rows, ncols):
    raw = []
    for r in header_rows:
        row_vals = [str(sh.cell_value(r, c)).strip() for c in range(ncols)]
        last = ""
        filled = []
        for v in row_vals:
            if v:
                last = v
            filled.append(last)
        raw.append(filled)
    cols = []
    for c in range(ncols):
        parts = []
        for row in raw:
            v = re.sub(r"\s+", " ", row[c]).strip() if c < len(row) else ""
            if v and v not in parts:
                parts.append(v)
        cols.append(" | ".join(parts) if parts else str(c))
    seen = {}
    out = []
    for col in cols:
        if col in seen:
            seen[col] += 1
            out.append(f"{col}_{seen[col]}")
        else:
            seen[col] = 0
            out.append(col)
    return out

def parse_sheet(wb, sheet_name, header_rows, data_start, period_type):
    sh = wb.sheet_by_name(sheet_name)
    cols = build_col_names(sh, header_rows, sh.ncols)
    rows = []
    for r in range(data_start, sh.nrows):
        raw = sh.cell_value(r, 0)
        if period_type == "xldate":
            period = xldate_to_str(raw, wb.datemode)
        elif period_type == "year":
            try:
                period = str(int(float(raw)))
            except:
                period = str(raw).strip()
        else:
            period = str(raw).strip()
        if not is_valid_period(period):
            continue
        rows.append([period] + [sh.cell_value(r, c) for c in range(1, sh.ncols)])
    df = pd.DataFrame(rows, columns=cols)
    df = df.rename(columns={df.columns[0]: "period"})
    df = df.loc[:, (df.columns == "period") | df.notna().any()]
    df = df.set_index("period")
    return df

df_lfs_summary = parse_sheet(wb, "1", [5], 9, "label")
df_lfs_summary.rename(inplace=True,columns={"All aged 16 & over":"16+ Population","Total economically active":"16+ Total Activity Level","Total in employment":"16+ Employment Level","Unemployed":"16+ Unemployment Level","Economically inactive":"16+ Economically Inactive Level","Economic activity":"16+ Economic Activity Rate","Employment":"16+ Employment Rate","Unemployment":"16+ Unemployment Rate","Economic inactivity":"16+ Economic Inactivity Rate","All aged 16 to 64":"16-64 Population","Total economically active_1":"16-64 Total Activity Level","Total in employment_1":"16-64 Employment Level","Unemployed_1":"16-64 Unemployment Level","Economically inactive_1":"16-64 Economically Inactive Level","Economic activity_1":"16-64 Economic Activity Rate","Employment_1":"16-64 Employment Rate","Unemployment_1":"16-64 Unemployment Rate","Economic inactivity_1":"16-64 Economic Inactivity Rate"})
df_lfs_summary.to_csv("data/unemployment_parsed.csv")