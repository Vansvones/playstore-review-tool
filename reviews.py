import os
import pandas as pd
from google_play_scraper import Sort, reviews, reviews_all

def allow_load_reviews(filename: str):
    if os.path.exists(filename):
        return True

def get_reviews(app_url: str, thumbsUpConstraint: int = 0) -> pd.DataFrame:
    print("Getting reviews dataframe...")
    filename = f"{app_url}-reviews.csv"
    if allow_load_reviews(filename):
        df = pd.read_csv(filename)
        return df[df["thumbsUpCount"] >= thumbsUpConstraint]
    
    result = reviews_all(app_url)

    df = pd.DataFrame(result)

    # filtering by number of thumbs ups
    df = df[df["thumbsUpCount"] >= thumbsUpConstraint]

    return df

def save_reviews(app_url: str, reviews_dataframe: pd.DataFrame) -> bool:
    print("Attempting to save...")
    try:
        filename = f"{app_url}-reviews.csv"
        if reviews_dataframe[reviews_dataframe["thumbsUpCount"] == 0].shape[0] != 0:
            reviews_dataframe.to_csv(filename)
        else:
            baseReviews = pd.DataFrame(reviews_all(app_url))
            baseReviews.to_csv(filename)

        print(f"Reviews saved to {filename}")
        return True
    except:
        print("Invalid app url or/and review object")
        return False