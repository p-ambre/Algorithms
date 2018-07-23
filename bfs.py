#Implementation of Breadth First Search Algorithm without recursion.
from collections import deque

class Node:
	def __init__(self,notkey):
		self.left = None
		self.right = None
		self.val = notkey

def bfs(root):
    queue = deque([])
    queue.append(root)
    while(len(queue) > 0):
        node = queue.popleft()
        if (node.left):
            queue.append(node.left)
        if (node.right):
            queue.append(node.right)
        print(node.val)

one = Node(1)
two = Node(2)
three = Node(3)
one.left = two
one.right = three
two.left = Node(4)
two.right = Node(5)
print("Breadth First Search path for the given tree is:")
bfs(one)
