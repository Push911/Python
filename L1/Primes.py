n = int(input("Enter number: "))


def primes(x):
    for val in range(0, x + 1):
        if val > 1:
            for i in range(2, val):
                if (val % i) == 0:
                    break
            else:
                print(val)


primes(n)
