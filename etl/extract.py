import pandas as pd


def extract(filepath):
    df = pd.read_csv(filepath)
    #print(df.head())
    print("Data Extracted Successfully")
    return df
