from reviews import get_reviews, save_reviews
from processing import rating_score_distribution

revs = get_reviews("com.rover.android")

score_dist = rating_score_distribution(revs)
print(score_dist)

save_reviews("com.rover.android", revs)