from sqlalchemy import create_engine

def load(df, db_uri, table_name):
    engine = create_engine(db_uri)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    #df.to_csv('testData.csv', index = False)
