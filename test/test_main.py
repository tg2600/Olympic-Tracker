import pytest
import pandas as pd
from app.country_utils import correct_country_names, get_flag, fetch_data, process_medal_counts, get_medal_count

def test_correct_country_names():
    assert correct_country_names("EUA") == "USA"
    assert correct_country_names("Grã-Bretanha") == "United Kingdom"
    assert correct_country_names("Alemanha") == "Germany"
    assert correct_country_names("Unknown Country") == "Unknown Country"

def test_get_flag():
    assert get_flag("United States") == "🇺🇸"
    assert get_flag("Brazil") == "🇧🇷"
    assert get_flag("Nonexistent Country") == ""

def test_fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Using a public test API
    data = fetch_data(url)
    assert data is not None
    assert "userId" in data

def test_process_medal_counts():
    mock_medal_counts = {
        "data": [
            {"name": "EUA", "gold_medals": 10, "silver_medals": 5, "bronze_medals": 2, "total_medals": 17},
            {"name": "Alemanha", "gold_medals": 8, "silver_medals": 4, "bronze_medals": 6, "total_medals": 18},
        ]
    }

    df = process_medal_counts(mock_medal_counts)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 5)
    assert df.iloc[0]["Country"] == "USA"
    assert df.iloc[1]["Country"] == "Germany"
    assert df.iloc[0]["Total Medals"] == 17

def test_get_medal_count():
    mock_data = {
        "Country": ["USA", "Germany"],
        "Gold Medals": [10, 8],
        "Silver Medals": [5, 4],
        "Bronze Medals": [2, 6],
        "Total Medals": [17, 18]
    }
    df = pd.DataFrame(mock_data)
    
    result = get_medal_count(df, "USA")
    assert result["Country"] == "USA"
    assert result["Gold Medals"] == 10
    
    result = get_medal_count(df, "Germany")
    assert result["Country"] == "Germany"
    assert result["Silver Medals"] == 4
    
    assert get_medal_count(df, "France") is None

if __name__ == "__main__":
    pytest.main()
    