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

print(traverse(head)) # 3, 6, 9

# Implement an in-order depth-first traversal for a binary tree using the provided class for a binary tree node.
# the return should be a list of values in the binary tree, based on an in-order (left, current, right) depth-first traversal

# Hint: you can implement DFS either with recursion (using the system call stack) or by manually declaring your own stack data structure. 

# For a quick and easy stack implementation:
# from collections import deque
# stack = deque()
# then stack.append(value) to push and stack.pop(value) to pop