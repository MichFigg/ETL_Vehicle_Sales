import pandas as pd
from thefuzz import process

correct_brands = [
    'Abarth', 'Alfa Romeo', 'Alpine', 'Aston Martin', 'Audi', 'Bentley', 'BMW', 'Bugatti', 'Citroën', 'Dacia', 'Ferrari', 'Fiat', 'Jaguar', 'Koenigsegg', 'Lamborghini', 'Lancia', 'Land Rover', 'Lotus', 'Maserati', 'McLaren', 'Mercedes-Benz', 'Mini', 'Opel', 'Pagani', 'Peugeot', 'Polestar', 'Porsche', 'Renault', 'Rolls-Royce', 'Saab', 'SEAT', 'Škoda', 'Smart', 'Spyker', 'Vauxhall', 'Volkswagen', 'Volvo', 'Acura', 'Buick', 'Cadillac', 'Chevrolet', 'Chrysler', 'Dodge', 'Ford', 'GMC', 'Hummer', 'Jeep', 'Lincoln', 'Ram', 'Rivian', 'Tesla', 'BYD', 'Chery', 'Daihatsu', 'Geely', 'Genesis', 'Honda', 'Hyundai', 'Infiniti', 'Isuzu', 'Kia', 'Lexus', 'Mazda', 'Mitsubishi', 'Nissan', 'SsangYong', 'Subaru', 'Suzuki', 'Tata', 'Toyota', 'Wuling', 'XPeng'
]

def clean_make_name(make_name, choices, score_cutoff=80):
    if pd.isna(make_name) or make_name == 'unknown' or make_name == '':
        return 'unknown'
    match = process.extractOne(make_name, choices, score_cutoff=score_cutoff)

    if match:
        return match[0]
    else:
        return make_name


def transform(df):
    text_cols = ['make','model','color','interior']

    #Normalization text fields
    for col in text_cols:
        df[col] = df[col].str.lower()
        df[col] = df[col].str.strip()
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True)
        

    #Removing useless columns
    df = df.drop(['trim','vin','condition', 'odometer','seller'], axis=1)

    #Normalization date
    df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce', utc=True)
    df['saledate'] = df['saledate'].dt.strftime('%d-%m-%Y')

    #Filling null/incorrect values in transmission 
    df['transmission'] = df['transmission'].fillna('manual')
    df['transmission'] = df['transmission'].str.replace('Sedan','manual')

    #Remove incorrect state codes
    df = df[df['state'].str.len().le(2)]

    #Remove fields without saledate
    df = df.dropna(subset=['saledate'])

    #Remove incorrect interior colors
    df['interior'] = df['interior'].replace('â€”', 'unknown')
    df['interior'] = df['interior'].replace('—', 'unknown')

    #Cleaning brands names
    df['make'] = df['make'].apply(lambda x: clean_make_name(x, correct_brands))
    df['make'] = df['make'].str.replace('vw','Volkswagen')

    #Replce value in color from numbers to unknown
    df['color'] = df['color'].str.replace(r'\d+', 'unknown', regex=True)

    
    return df

    
    

    

