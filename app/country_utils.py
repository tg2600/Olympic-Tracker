import pycountry

def correct_country_names(country_name):
    corrections = {
        "EUA": "USA",
        "Grã-Bretanha": "United Kingdom",
        "Alemanha": "Germany",
        "França": "France",
        "Japão": "Japan",
        "República da Coréia": "South Korea",
        "Países Baixos": "Netherlands",
        "Austrália": "Australia",
        "Canadá": "Canada",
        "Itália": "Italy",
        "Suécia": "Sweden",
        "Hungria": "Hungary",
        "República Dominicana": "Dominican Republic",
        "África do Sul": "South Africa",
        "Nova Zelândia": "New Zealand",
        "Brasil": "Brazil",
        "Argentina": "Argentina",
        "México": "Mexico",
        "Egito": "Egypt",
        "Espanha": "Spain",
        "Quênia": "Kenya",
        "Noruega": "Norway",
        "Irlanda": "Ireland",
        "Uzbequistão": "Uzbekistan"
        # May add more corrections as necessary
    }
    return corrections.get(country_name, country_name)

def get_flag(country_name):
    try:
        country_code = pycountry.countries.lookup(country_name).alpha_2
        flag_emoji = chr(127462 + ord(country_code[0]) - ord('A')) + chr(127462 + ord(country_code[1]) - ord('A'))
        return flag_emoji
    except LookupError:
        return ""
