from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI(title="HSN Code Validation Agent", version="1.0.0")

# Data Handling
df = pd.read_excel("HSN_SAC.xlsx", engine='openpyxl')
df.columns = df.columns.str.strip()  # Removing whitespace/newlines
df['HSNCode'] = df['HSNCode'].astype(str).str.strip()
valid_codes = set(df['HSNCode'])

# Hierarchical check
def check_hierarchy(hsn_code, code_set):
    levels = [hsn_code[:i] for i in range(2, len(hsn_code), 2)]
    missing = [lvl for lvl in levels if lvl not in code_set]
    return {"parent_levels_missing": missing} if missing else {}

@app.get("/")
def read_root():
    return {"message": "HSN Code Validator is running"}

@app.get("/validate/")
def validate_hsn(codes: str = Query(..., description="Comma-separated HSN codes")):
    result = []

    for code in codes.split(","):
        code = code.strip()

        if not code.isdigit() or not (2 <= len(code) <= 8):
            result.append({
                "hsn_code": code,
                "valid": False,
                "reason": "Invalid format: must be numeric and 2–8 digits long"
            })
        elif code in valid_codes:
            desc = df[df['HSNCode'] == code]['Description'].values[0]
            item = {
                "hsn_code": code,
                "valid": True,
                "description": desc
            }

            # Add hierarchy check for codes longer than 4 digits
            if len(code) > 4:
                item.update(check_hierarchy(code, valid_codes))

            result.append(item)
        else:
            result.append({
                "hsn_code": code,
                "valid": False,
                "reason": "Code not found in master data"
            })

    return {"results": result}
