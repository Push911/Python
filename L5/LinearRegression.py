import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


maxMovies = [10, 100, 1000, 10000, 100000]
mtr = []
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
    if maxMov == 100000:
        plt.scatter(np.arange(1, 16), prediction, label="prediction")
        plt.scatter(np.arange(1, 16), rating[-15:], label="expectation")
        plt.xlabel("Last 15 users of 100000 movies")
        plt.title("Plotting last 15 users of 100000")
        plt.ylabel("Ratings")
        plt.legend()
        # for x in predictionMatrix:
        #     mtr.append(x)
        # m, b = np.polyfit(mtr[:-15], users[:-15], 1)
        # plt.plot(mtr[-15:], m * np.array(mtr[-15:]) + b)
        plt.show()
        print(prediction)
