from math import sqrt
from collections import defaultdict


def determine_types(args):
    return tuple([type(a) for a in args])


function_table = defaultdict(dict)


def overload(*arg_types):
    def wrap(func):
        named_func = function_table[func.__name__]
        named_func[arg_types] = func

        def call_function_by_signature(*args):
            return named_func[determine_types(args)](*args)
        return call_function_by_signature

    return wrap


@overload(int, int)
def norm(x, y):
    return sqrt(x * x + y * y)


@overload(int, int, int)
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


print(f"norm(2,4) = {norm(2, 4)}")

print(f"norm(2,3,4) = {norm(2, 3, 4)}")

