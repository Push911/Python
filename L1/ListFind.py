import random

x = input("Enter the pattern: ")
key_list = []
find_list = []
roflan_list = []


def randomString():
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    for i in range(20):
        key_list.append(''.join(random.choice(list(dictionary.keys())) for i in range(8)))


def find(n):
    randomString()
    print(key_list)
    k = 0
    for i in n:
        k += 1
        if i != "*":
            find_key(i, k)
            roflan_list.append(k)


def find_key(r, t):
    for s in key_list:
        # print(s, s.find(r, t - 1, t))
        if s.find(r, t - 1, t) == -1:
            find_list.append(s)

    for st in find_list:
        if st in key_list:
            key_list.remove(st)


find(x)
print(key_list)
