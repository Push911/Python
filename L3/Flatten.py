# from matplotlib.cbook import flatten


def flatten(collection):
    for i in collection:
        if isinstance(i, list):
            for x in flatten(i):
                yield x
        else:
            yield i


l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]
print(list(flatten(l)))