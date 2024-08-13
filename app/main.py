import pandas as pd
from app.data_loader import fetch_data
from app.shared import process_medal_counts, get_medal_count
from app.country_utils import get_flag

# Request URL for the Codante.io API
request_url = "https://apis.codante.io/olympic-games/countries"

# Fetch and process medal counts data
medal_counts = fetch_data(request_url)
medal_counts_df = process_medal_counts(medal_counts)

# Example usage
country_name = input("Enter the country name: ")
medal_count = get_medal_count(medal_counts_df, country_name)
if medal_count is not None:
    flag = get_flag(country_name)
    # Handle potential encoding issues for the flag
    try:
        print(f"Flag: {flag}")
    except UnicodeEncodeError:
        print(f"Flag: Unable to display flag emoji")
    
    for key, value in medal_count.items():
        print(f"{key}: {value}")
