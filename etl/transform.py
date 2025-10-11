import pandas as pd

def transform(df):
    df = df.drop_duplicates()
    df.columns = [c.lower().replace(' ','_') for c in df.columns]
    df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce')
    return df
