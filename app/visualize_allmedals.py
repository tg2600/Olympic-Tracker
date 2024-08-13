import pandas as pd
import matplotlib.pyplot as plt  # Make sure this import is added

from app.shared import process_medal_counts  # Import the shared function
from app.data_loader import fetch_data  # Ensure this is fetching the data
from app.country_utils import correct_country_names  # Import this function


# Fetch the medal counts data
request_url = "https://apis.codante.io/olympic-games/countries"
medal_counts = fetch_data(request_url)

# Process the medal counts into a DataFrame
medal_counts_df = process_medal_counts(medal_counts)

# Display the DataFrame
print(medal_counts_df)

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
    plt.show()

# Plot the top 20 countries by total medals
plot_total_medal_counts(medal_counts_df)