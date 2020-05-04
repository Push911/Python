import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


maxMovies = [10, 100, 1000, 10000, 100000]
ratingscsv = pd.read_csv("ml-latest-small/ratings.csv")
moviecsv = pd.read_csv("ml-latest-small/movies.csv")

movie1 = ratingscsv.movieId == 1
userid1 = ratingscsv[movie1].eval("userId")
users = userid1.to_numpy()

rat = ratingscsv[movie1].eval("rating")
rating = rat.to_numpy()

movie = moviecsv.eval("movieId")
movies = movie.to_numpy()


def createMatrix(movieid, userids):
    mvs = movies[movies <= movieid]
    movs = ratingscsv["movieId"] <= movieid
    userid = ratingscsv["userId"].isin(userids)
    fltr = movs & userid
    rts = ratingscsv[fltr]
    matrix = rts.pivot(index="userId", columns="movieId", values="rating").reindex(mvs[1:], axis="columns")
    np.nan_to_num(matrix, copy=False)
    return matrix


for maxMov in maxMovies:
    defaultMatrix = createMatrix(maxMov, users[:-15])
    reg = LinearRegression().fit(defaultMatrix, rating[:-15])
    predictionMatrix = createMatrix(maxMov, users[-15:])
    prediction = reg.predict(predictionMatrix)

    plt.scatter(np.arange(1, 16), prediction, label="prediction")
    plt.scatter(np.arange(1, 16), rating[-15:], label="expectation")
    if maxMov == 10:
        plt.xlabel("First 15 users of 15 movies")
        plt.title("Plotting first 15 users")
    elif maxMov == 100:
        plt.xlabel("Last 15 users of 100 movies")
        plt.title("Plotting last 15 users of 100")
    elif maxMov == 1000:
        plt.xlabel("Last 15 users of 1000 movies")
        plt.title("Plotting last 15 users of 1000")
    elif maxMov == 10000:
        plt.xlabel("Last 15 users of 10000 movies")
        plt.title("Plotting last 15 users of 10000")
    else:
        plt.xlabel("Last 15 users of 100000 movies")
        plt.title("Plotting last 15 users of 100000")
    plt.ylabel("Ratings")
    plt.legend()
    plt.show()
