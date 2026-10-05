import re
import unicodedata

import pandas as pd


def normalize_city(city: str) -> str:
    city = city.strip().lower()

    city = unicodedata.normalize("NFKD", city)
    city = "".join(c for c in city if not unicodedata.combining(c))

    city = city.replace("'", " ")
    city = city.replace("-", " ")
    city = " ".join(city.split())

    return city


import re
import pandas as pd


STATE_CODES = {
    "ac",
    "al",
    "ap",
    "am",
    "ba",
    "ce",
    "df",
    "es",
    "go",
    "ma",
    "mt",
    "ms",
    "mg",
    "pa",
    "pb",
    "pr",
    "pe",
    "pi",
    "rj",
    "rn",
    "rs",
    "ro",
    "rr",
    "sc",
    "sp",
    "se",
    "to",
}


def remove_state_suffix(city):
    if pd.isna(city):
        return city

    city = city.strip()

    # ex: "pinhais/pr", "lages - sc", "andira-pr"
    city = re.sub(
        r"\s*[-/]\s*(ac|al|ap|am|ba|ce|df|es|go|ma|mt|ms|mg|pa|pb|pr|pe|pi|rj|rn|rs|ro|rr|sc|sp|se|to)$",
        "",
        city,
    )

    # ex: "brasilia df", "sao paulo sp"
    city = re.sub(
        r"\s+(ac|al|ap|am|ba|ce|df|es|go|ma|mt|ms|mg|pa|pb|pr|pe|pi|rj|rn|rs|ro|rr|sc|sp|se|to)$",
        "",
        city,
    )

    return city.strip()


def normalize_city_v2(city):
    if pd.isna(city):
        return city

    city = str(city).strip().lower()

    # Normalisation Unicode
    city = unicodedata.normalize("NFKD", city)
    city = "".join(c for c in city if not unicodedata.combining(c))

    # Espaces multiples
    city = re.sub(r"\s+", " ", city)

    # Apostrophes
    city = city.replace("´", "'")

    return city
