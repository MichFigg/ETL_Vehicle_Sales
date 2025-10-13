import pandas as pd


def transform(df):
    text_cols = ['make','model','color','interior']

    df = df.drop(['trim','vin','condition', 'odometer','seller'], axis=1)

    df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce', utc=True)
    df['saledate'] = df['saledate'].dt.strftime('%d-%m-%Y')
    
    for col in text_cols:
        df[col] = df[col].str.lower()
        df[col] = df[col].str.strip()
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True)
    return df
    

    

