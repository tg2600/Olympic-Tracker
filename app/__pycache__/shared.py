import pandas as pd
from app.country_utils import correct_country_names

def process_medal_counts(medal_counts):
    if not medal_counts:
        return pd.DataFrame()
    medals_list = []
    for country in medal_counts.get('data', []):
        corrected_country_name = correct_country_names(country['name'])
        medals_list.append({
            'Country': corrected_country_name,
            'Gold Medals': country['gold_medals'],
            'Silver Medals': country['silver_medals'],
            'Bronze Medals': country['bronze_medals'],
            'Total Medals': country['total_medals']
        })
    return pd.DataFrame(medals_list)

def get_medal_count(medal_counts_df, country_name):
    if medal_counts_df.empty:
        print("No data available.")
        return None
    
    country_name_corrected = correct_country_names(country_name)
    country_data = medal_counts_df[medal_counts_df['Country'].str.lower() == country_name_corrected.lower()]
    
    if not country_data.empty:
        return country_data.iloc[0].to_dict()
    else:
        print(f"No data found for {country_name}.")
        return None
