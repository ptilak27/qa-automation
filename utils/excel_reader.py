# utils/excel_reader.py
import pandas as pd


def read_users_from_excel(path):
    df = pd.read_excel(path)
    # convert rows to dicts
    return df.to_dict(orient="records")
