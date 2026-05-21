from google_play_scraper import reviews
import pandas as pd
import os

# App config: mapping short names to (Google Play ID, Full App Name)
APP_CONFIG = {
    "CBE": {
        "app_id": "com.combanketh.mobilebanking",
        "full_name": "Commercial Bank of Ethiopia Mobile"
    },
    "BOA": {
        "app_id": "com.boa.boaMobileBanking",
        "full_name": "Bank of Abyssinia Mobile"
    },
    "Dashen": {
        "app_id": "com.dashen.dashensuperapp",
        "full_name": "Dashen Bank SuperApp"
    }
}

# Scrape reviews and return cleaned DataFrame
def scrape_reviews(app_id, full_app_name, count=400):
    all_reviews = []
    continuation_token = None

    while len(all_reviews) < count:
        result, continuation_token = reviews(
            app_id,
            lang='en',
            country='us',
            count=200,
            continuation_token=continuation_token
        )
        all_reviews.extend(result)
        if continuation_token is None:
            break

    df = pd.DataFrame(all_reviews)

    df_cleaned = pd.DataFrame({
        "Review Text": df["content"],
        "Rating": df["score"],
        "Date": pd.to_datetime(df["at"]).dt.date,
        "Bank/App Name": full_app_name,
        "Source": "Google Play"
    })

    return df_cleaned

# Scrape all apps and save to individual CSVs
def scrape_all(output_dir="../data/raw/"):
    os.makedirs(output_dir, exist_ok=True)

    for short_name, config in APP_CONFIG.items():
        print(f"Scraping {short_name}...")
        df = scrape_reviews(config["app_id"], config["full_name"])
        output_file = os.path.join(output_dir, f"{short_name.lower()}_reviews.csv")
        df.to_csv(output_file, index=False)
        print(f"Saved {short_name} reviews to {output_file}")
