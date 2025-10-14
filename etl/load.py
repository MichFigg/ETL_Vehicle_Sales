from pathlib import Path

from sqlalchemy import create_engine


def load(df, db_uri, table_name):
    engine = create_engine(db_uri)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    processed_dir = Path("data") / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    output_path = processed_dir / f"{table_name}.csv"
    df.to_csv(output_path, index=False)
    print("File Loaded Successfully!")
