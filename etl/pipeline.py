from extract import extract
from transform import transform
from load import load

import os

#csv file path
filepath = "data/raw/car_prices.csv"


db_uri = "sqlite:///vehicle_sales.db"

def main():
    df = extract(filepath)
    df = transform(df)
    load(df, db_uri, "vehicle_sales")

if __name__ == "__main__":
    main()
