#ANS1 - Submitted by Tatwamasi Mishra, UCSE20040

#this program creates and displays a simple binary tree

class Node :
  def __init__(node, data) :
    node.data = data
    node.left = None
    node.right = None
  def display(node):
    if node.left:
      node.left.display()
    print(node.data, end="\t")
    if node.right:
      node.right.display()

#driver code
root = Node(5)
root.left = Node(9)
root.right = Node(12)
root.left.right = Node(6)
print("Printing inorder sequence for the created binary tree:")
root.display()