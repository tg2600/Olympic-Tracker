import os
import pandas as pd
import matplotlib.pyplot as plt

from app.shared import process_medal_counts
from app.data_loader import fetch_data
from app.country_utils import correct_country_names

# Fetch the medal counts data
request_url = "https://apis.codante.io/olympic-games/countries"
medal_counts = fetch_data(request_url)

# Process the medal counts into a DataFrame
medal_counts_df = process_medal_counts(medal_counts)

# Function to visualize gold medal counts
def plot_gold_medal_counts(df):
    if df.empty:
        print("No data to plot.")
        return

    # Sort and select the top 20 countries
    df = df.sort_values(by='Gold Medals', ascending=False).head(20)

    # Create the plot
    df.plot(kind='bar', x='Country', y='Gold Medals', color='gold', figsize=(12, 8))
    plt.title('Top 20 Countries by Gold Medals')
    plt.xlabel('Country')
    plt.ylabel('Gold Medals')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Ensure the directory exists
    output_dir = os.path.join('static', 'images')
    os.makedirs(output_dir, exist_ok=True)

    # Save the plot as a PNG file
    output_path = os.path.join(output_dir, 'top_20_gold_medals.png')
    plt.savefig(output_path)
    plt.show()

# Function to get the top 20 countries by gold medals
def get_top_20_gold_medals():
    if medal_counts_df.empty:
        return []
    top_20_gold = medal_counts_df.sort_values(by='Gold Medals', ascending=False).head(20)
    return top_20_gold[['Country', 'Gold Medals']].to_dict(orient='records')

# Plot the gold medal counts
plot_gold_medal_counts(medal_counts_df)