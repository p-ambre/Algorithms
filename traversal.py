#Implementing Inorder, Preorder and Postorder tree traversals.
class Node:
	def __init__(self,notkey):
		self.left = None
		self.right = None
		self.val = notkey
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

root = Node(1)
root.left	 = Node(2)
root.right	 = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("\nInorder traversal of binary tree is")
inorder(root)
print("Preorder traversal of binary tree is")
preorder(root)
print("\nPostorder traversal of binary tree is")
postorder(root)
