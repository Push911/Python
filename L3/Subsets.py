def subsets(lst):
    if len(lst) == 0:
        return [[]]
    else:
        head = lst[0]
        tail = lst[1:]
        return subsets(tail) + list(map(lambda x: [head, *x], subsets(tail)))


print(subsets([1, 2, 3]))
