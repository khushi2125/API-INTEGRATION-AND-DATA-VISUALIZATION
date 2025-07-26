 #SCRIPT
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fetch COVID-19 data by country
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Convert JSON to DataFrame
    df = pd.DataFrame(data)

    # Select top 10 countries by cases
    top_countries = df.sort_values('cases', ascending=False).head(10)

    # Plotting
    plt.figure(figsize=(12, 6))    # Create a figure with width=12 inches and height=6 inches

    sns.barplot(x='cases', y='country', data=top_countries, palette='Reds_r')
    plt.title('Top 10 Countries by COVID-19 Cases')
    plt.xlabel('Total Cases')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

else:
    print("Failed to fetch data. Status code:", response.status_code)
