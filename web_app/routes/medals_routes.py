from flask import Blueprint, request, render_template, redirect
from app.data_loader import fetch_data
from app.shared import process_medal_counts, get_medal_count
from app.country_utils import get_flag

medals_routes = Blueprint("medals_routes", __name__)

@medals_routes.route("/medals/form")
def medals_form():
    return render_template("medals_form.html")

@medals_routes.route("/medals/dashboard", methods=["GET", "POST"])
def medals_dashboard():
    if request.method == "POST":
        country_name = request.form.get("country_name").strip()  # Retrieve and sanitize the country name
    else:
        country_name = request.args.get("country_name", "United States").strip()

    # Fetch and process the medal data
    request_url = "https://apis.codante.io/olympic-games/countries"
    medal_counts = fetch_data(request_url)
    medal_counts_df = process_medal_counts(medal_counts)

    # Get the medal count for the specified country
    medal_count = get_medal_count(medal_counts_df, country_name)

    if medal_count is not None:
        flag = get_flag(country_name)
        return render_template(
            "medals_dashboard.html",
            country_name=country_name,
            flag=flag,
            medal_count=medal_count
        )
    else:
        return render_template(
            "medals_dashboard.html",
            country_name=country_name,
            flag=None,
            error=f"No data found for {country_name}."
        )

@medals_routes.route("/api/medals.json")
def medals_api():
    country_name = request.args.get("country_name", "United States").strip()

    request_url = "https://apis.codante.io/olympic-games/countries"
    medal_counts = fetch_data(request_url)
    medal_counts_df = process_medal_counts(medal_counts)

    medal_count = get_medal_count(medal_counts_df, country_name)

    if medal_count is not None:
        return {"country_name": country_name, "medal_count": medal_count}
    else:
        return {"error": f"No data found for {country_name}."}, 404