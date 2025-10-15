from pathlib import Path
from sqlalchemy import create_engine


def load(df, db_string, table_name):

    #Creating processed folder
    processed_dir = Path("data") / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)
    
    db_path = processed_dir / "vehicle_sales.sqlite"
    db_string = f'sqlite:///{db_path}'

    engine = create_engine(db_string)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    output_path = processed_dir / f"{table_name}.csv"
    df.to_csv(output_path, index=False)

    print("File Loaded Successfully!")
