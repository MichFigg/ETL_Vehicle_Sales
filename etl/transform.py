import pandas as pd


def transform(df):
    text_cols = ['make','model','color','interior']

    df = df.drop(['trim','vin','condition', 'odometer','seller'], axis=1)

    df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce', utc=True)
    df['saledate'] = df['saledate'].dt.strftime('%d-%m-%Y')

    #df['transmission'] = df['transmission'].replace(r'^\s*$', 'manual', regex=True)

    df['interior'] = df['interior'].replace('â€”', 'unknown')

    df['transmission'] = df['transmission'].fillna('manual')
    
    for col in text_cols:
        df[col] = df[col].str.lower()
        df[col] = df[col].str.strip()
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True)
    return df
    

    

