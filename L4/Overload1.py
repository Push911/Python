from math import sqrt

function_table = {}


def overload(function):

    function_table[(function.__name__, function.__code__.co_argcount)] = function

    def wrap(*args):
        return function_table[(function.__name__, len(args))](*args)
    return wrap


@overload
def norm(x, y):
    return sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


print(f"norm(2,4) = {norm(2,4)}")
print(f"norm(2,3,4) = {norm(2,3,4)}")
