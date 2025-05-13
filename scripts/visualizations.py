import matplotlib.pyplot as plt

def plot_total_cases(df, countries, output_path):
    plt.figure(figsize=(10,6))
    for country in countries:
        data = df[df['location'] == country]
        plt.plot(data['date'], data['total_cases'], label=country)
    plt.title("Total COVID-19 Cases")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.savefig(output_path)
    plt.close()
