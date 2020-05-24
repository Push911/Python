import random
from collections import deque


class Node:
    def __init__(self, data, subtrees, height):
        self.height = height
        self.data = data
        self.subtrees = subtrees

    def __str__(self):
        return f'{self.data} h={self.height} [{", ".join(str(s) for s in self.subtrees)}]'

    def dfs(self):
        if self is None:
            return
        yield self.data
        for st in self.subtrees:
            yield from st.dfs()

    def bfs(self):
        if self is None:
            return
        queue = deque([self])
        while queue:
            st = queue.pop()
            yield st.data
            queue.extend(st.subtrees)


def generate_random_tree(height):
    if height == 0:
        return None
    elif height == 1:
        return Node(random.randint(-(height ** 2), height ** 2), [], 1)

    subtrees_count = random.randint(1, 2)
    highest_subtree_position = random.randrange(0, subtrees_count)
    value = random.randint(-height ** 2, height ** 2)
    subtrees = []
    for i in range(subtrees_count):
        if i != highest_subtree_position:
            tree = generate_random_tree(random.randint(1, height - 1))
        else:
            tree = generate_random_tree(height - 1)
        subtrees.append(tree)
    return Node(value, subtrees, height)


tree = generate_random_tree(5)
print(tree)
print(list(tree.dfs()))
print(list(tree.bfs()))
