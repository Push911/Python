import pandas as pd
import numpy as np
from numpy import nan_to_num, linalg, dot

ratingscsv = pd.read_csv("ml-latest-small/ratings.csv")
moviescsv = pd.read_csv("ml-latest-small/movies.csv")
movieCount = moviescsv["movieId"].count()

# print(ratingscsv["userId"].count())

movies = moviescsv.loc[moviescsv.movieId < movieCount, ["movieId", "title"]].to_numpy()
movieRatings = ratingscsv.loc[ratingscsv.movieId < movieCount, ["userId", "movieId", "rating"]].to_numpy()

ratings = np.zeros((611, 9019))
for data in movieRatings:
    ratings[int(data[0]), int(data[1])] = data[2]


def recommendation(movies, ratings, users):
    users = nan_to_num(users / linalg.norm(users, axis=0))
    ratings = nan_to_num(ratings / linalg.norm(ratings, axis=0))
    userRating = nan_to_num(dot(ratings, users) / linalg.norm(dot(ratings, users)))
    recommendations = dot(ratings.T, userRating)
    recommended_movies = [(recommendations[movie[0]][0], movie[1]) for movie in movies]
    return sorted(recommended_movies, reverse=True)[:5]


def main():
    userRatings = np.zeros((9019, 1))
    userRatings[3241] = 5
    userRatings[902] = 4
    userRatings[321] = 3
    userRatings[7319] = 2

    recommendations = recommendation(movies, ratings, userRatings)

    print("\t\tTop 5 recommendations")
    print("Recommended\t Title")
    for score, movie in recommendations:
        print(str(round(score * 100, 2)) + "%\t\t", movie)


if __name__ == "__main__":
    main()
