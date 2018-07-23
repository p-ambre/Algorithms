#Implementation of Depth First Search Algorithm
from collections import deque

class Node:
	def __init__(self,notkey):
		self.left = None
		self.right = None
		self.val = notkey

def dfs(root):
    queue = deque([])
    queue.append(root)
    while(len(queue) > 0):
        node = queue.pop()
        if (node.right):
            queue.append(node.right)
        if (node.left):
            queue.append(node.left)
        print(node.val)

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.left = two
one.right = three
two.left = four
two.right = Node(5)
four.right = Node(6)
print("Depth First Search path for the given tree is:")
dfs(one)
