import pandas as pd
from google_play_scraper import Sort, reviews, reviews_all, app

def get_reviews(app_url: str) -> pd.DataFrame:
    result = reviews_all(app_url)

    df = pd.DataFrame(result)
    return df

def save_reviews(app_url: str, reviews_dataframe: pd.DataFrame, file_type: str = "csv") -> bool:
    try:
        app_info = app(app_url)
        match (file_type):
            case "csv":
                reviews_dataframe.to_csv(f"{app_info["title"]}-reviews.csv")
            case "json":
                reviews_dataframe.to_json(f"{app_info["title"]}-reviews.json")
            case default:
                print("hi")
                raise ValueError("Invalid file type")
        print(f"Reviews saved to \'{app_info["title"]-reviews.csv}\'")
        return True
    except:
        print("Invalid app url or/and review object")
        return False