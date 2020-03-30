def qsort(lst):
    if not lst:
        return lst
    head, tail = lst[0], lst[1:]
    return qsort(list(filter(lambda x: x <= head, tail))) + [head] + qsort(list(filter(lambda x: x > head, tail)))


l = [1, 23, 4, 56, 73, 2567, 832, 12, 0, 123]
print(qsort(l))


