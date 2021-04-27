#ANS2 - Submitted by Tatwamasi Mishra, UCSE20040

#this program implements all three tree traversal techniques

class Node :
  def __init__(node, data) :
    node.data = data
    node.left = None
    node.right = None

  #function to display preorder sequence
  def Preorder_display(node):
    
    print(node.data, end="\t")   
    if node.left:
      node.left.Preorder_display()    
    if node.right:
      node.right.Preorder_display()
  
  #function to display inorder sequence
  def Inorder_display(node):
    if node.left:
      node.left.Inorder_display()
    print(node.data, end="\t")
    if node.right:
      node.right.Inorder_display()
  
  #function to display postorder sequence
  def Postorder_display(node):
    if node.left:
      node.left.Postorder_display()
    if node.right:
      node.right.Postorder_display()
    print(node.data, end="\t")

#driver code
root = Node(5)
root.left = Node(9)
root.right = Node(12)
root.left.right = Node(6)
print("Printing pre-order sequence for the created binary tree:")
root.Preorder_display()

print("\nPrinting in-order sequence for the created binary tree:")
root.Inorder_display()

print("\nPrinting post-order sequence for the created binary tree:")
root.Postorder_display()