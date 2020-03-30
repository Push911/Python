x = int(input("Enter the amount of lines: "))


def pascal(i):
    r = 2 * i - 2
    for i in range(0, i):
        for k in range(0, r):
            print(end="  ")
        r -= 1
        for j in range(0, i + 1):
            print(binom(i, j), "  ", end="")
        print()


def binom(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    return res


pascal(x)
