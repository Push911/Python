import collections

x = int(input("Enter number: "))
factor_list = []


def prime_factors(n):

    while n % 2 == 0:
        factor_list.append(2)
        n = n / 2

    for i in range(3, int(n), 2):
        while n % i == 0:
            factor_list.append(i)
            n = n / i

    if n > 2:
        factor_list.append(int(n))

    counter = collections.Counter(factor_list)
    print(counter.most_common(x))


prime_factors(x)
