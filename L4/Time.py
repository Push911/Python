import timeit


def timer(func):
    start = timeit.default_timer()
    func()
    time = timeit.default_timer() - start
    print("Function:", func.__name__, "was completed in", time, "seconds")


@timer
def f():
    for _ in range(0, 10000000):
        pass
