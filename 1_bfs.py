from collections import deque

class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse(root: node):
    pass

# Test cases:
head = node(6)
head.left = node(3)
head.right = node(9)

print(traverse(head)) # 6, 3, 9

# Implement a level-order breadth-first traversal for a binary tree using the provided class for a binary tree node.
# the return should be a list of values in the binary tree, based on a level-order (searching left to right at each "level") breadth-first traversal

# Hint: implementing BFS requires a queue data structure.
# For a quick and easy queue implementation:
# queue = deque()
# then queue.append(value) to push and queue.popleft(value) to dequeue