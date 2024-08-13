import pandas as pd
import matplotlib.pyplot as plt  # Use the default backend for interactive plotting

from app.shared import process_medal_counts
from app.data_loader import fetch_data

# Fetch the medal counts data
request_url = "https://apis.codante.io/olympic-games/countries"
medal_counts = fetch_data(request_url)

# Process the medal counts into a DataFrame
medal_counts_df = process_medal_counts(medal_counts)

# Function to visualize the total medal counts
def plot_total_medal_counts(df):
    if df.empty:
        print("No data to plot.")
        return
    df = df.sort_values(by='Total Medals', ascending=False).head(20)
    df.plot(kind='bar', x='Country', y='Total Medals', color='skyblue', figsize=(12, 8))
    plt.title('Top 20 Countries by Total Medals')
    plt.xlabel('Country')
    plt.ylabel('Total Medals')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()  # Display the plot in a window

# Function to get the top 20 countries by total medals
def get_top_20_total_medals():
    if medal_counts_df.empty:
        return []
    top_20_total = medal_counts_df.sort_values(by='Total Medals', ascending=False).head(20)
    return top_20_total[['Country', 'Total Medals']].to_dict(orient='records')

# Plot the top 20 countries by total medals
plot_total_medal_counts(medal_counts_df)