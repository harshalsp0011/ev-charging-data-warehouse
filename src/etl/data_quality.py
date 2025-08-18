import pandas as pd

def validate_csv_not_empty(csv_path):
    df = pd.read_csv(csv_path)
    if df.empty:
        raise ValueError(f"{csv_path} is empty")
    print(f"{csv_path}: {len(df)} records validated")

def validate_columns(csv_path, expected_columns):
    df = pd.read_csv(csv_path, nrows=0)
    missing = set(expected_columns) - set(df.columns)
    if missing:
        raise ValueError(f"{csv_path} missing columns: {missing}")
    print(f"{csv_path}: all expected columns present")
