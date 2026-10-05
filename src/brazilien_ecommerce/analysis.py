def normalize_V2(city):
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
