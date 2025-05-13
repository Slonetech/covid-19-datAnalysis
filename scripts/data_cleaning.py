import pandas as pd

def clean_covid_data(filepath, countries):
    df = pd.read_csv(filepath)
    df = df[df['location'].isin(countries)]
    df['date'] = pd.to_datetime(df['date'])
    df.fillna(method='ffill', inplace=True)
    return df
