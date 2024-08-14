
# Olympic Games Medal Tracker

## Project Summary

This application is a Python-based Olympic Games medal tracker that fetches and processes data related to the 2024 Olympic Games. The application allows users to:

- Display the top 20 countries by gold medal and total medal counts.
- Visualize medal data using bar charts.
- Provide medal counts for specific countries based on user input.
- Show country flags alongside their medal counts.

## Features

- **Country Flags Display**: Displays the flag of the country next to its medal counts.
- **Medal Winners Lookup**: Allows users to look up medal winners for a specific country.

## Installation

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/yourusername/olympic-medal-tracker.git
   cd olympic-medal-tracker
   ```

2. Install the required dependencies using `pip`:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Fetching and Displaying Medal Data

To fetch and display the top 20 countries by all medal counts, run:

```sh
python -m app.visualize_allmedals
```

To fetch and display the top 20 countries by gold medal counts only, run:

```sh
python -m app.visualize_gold
```

To input country name and receive medal data output, run:

```sh
python -m app.main
```

This will prompt you to enter a country name, and it will display the medal counts along with the flag for that country.

### Example

```
Enter the country name: United States
Flag: 🇺🇸
Gold Medals: 30
Silver Medals: 25
Bronze Medals: 20
Total: 75
```

## Running the Application

You can also explore and run the Olympic Games Medal Tracker application directly from your web browser. Visit the [Olympic Tracker application](https://olympic-tracker-1.onrender.com/) to see the app in action.

## Running Tests

To ensure the integrity of the code, you can run unit tests included in the project. These tests are designed to verify the functionality of key components.

### Running All Tests

To run all tests, navigate to the project's root directory and use the following command:

```sh
pytest
```

## Project Structure

- **`fetch_data.py`**: Contains the function for fetching data from the API.
- **`country_utils.py`**: Contains utility functions related to country names and flags.
- **`medal_counts.py`**: Contains functions to process medal data and retrieve medal counts for specific countries.
- **`main.py`**: The main script that integrates all functionalities and handles user interaction.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Running the Web Application Locally

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if 'export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```
