import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def rating_score_distribution(reviews: pd.DataFrame) -> dict:
    scores = dict(reviews["score"].value_counts().sort_index())

    return scores