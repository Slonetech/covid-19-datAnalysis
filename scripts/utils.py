def format_number(num):
    return f"{num:,.0f}"

def calculate_death_rate(df):
    return df['total_deaths'] / df['total_cases']
