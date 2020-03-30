import math

x = int(input("Enter number: "))


def fraczero(n):
    if n in range(100001):
        i = math.factorial(n)
        print(i)
        s = str(i)
        print(len(s) - len(s.rstrip('0')))


fraczero(x)
