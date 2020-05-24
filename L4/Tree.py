import random
from collections import deque


def generateTree(height):
    if height == 0:
        return None
    data = random.randint(-(height ** 2), height ** 2)
    randomTree = generateTree(random.randint(0, height - 1))
    newTree = generateTree(height - 1)
    return [data, newTree, randomTree]


def dfs(tree):
    if tree is not None:
        yield tree[0]
        yield from dfs(tree[1])
        yield from dfs(tree[2])


def bfs(tree):
    if tree is not None:
        deq = deque([tree])
        while deq:
            array = deq.pop()
            if array is not None:
                yield array[0]
                deq.append(array[1])
                deq.append(array[2])


tree = generateTree(5)
print(tree)
print(list(dfs(tree)))
print(list(bfs(tree)))
