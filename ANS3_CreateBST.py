#ANS3 - Submitted by Tatwamasi Mishra, UCSE20040

#this program creates a BST from a given list of numbers

class Node :
  def __init__(node, data) :
    node.data = data
    node.left = None
    node.right = None
  
  #function to create Binary Search Tree
  def createBST(node, data):
        if node.data:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                else:
                    node.left.createBST(data)
            elif data > node.data:
                if node.right == None:
                    node.right = Node(data)
                else:
                    node.right.createBST(data)
        else:
            node.data = data

  def Preorder_display(node):
    
    print(node.data, end="\t")   
    if node.left:
      node.left.Preorder_display()    
    if node.right:
      node.right.Preorder_display()
  
  def Inorder_display(node):
    if node.left:
      node.left.Inorder_display()
    print(node.data, end="\t")
    if node.right:
      node.right.Inorder_display()

#driver code
array = [12, 2, 56, 82, 22, 5, 45, 9]
root = Node(array[0])

for node in array[1:]:
  root.createBST(node)
print("Printing pre-order sequence for the created BST:")
root.Preorder_display()

print("\nPrinting in-order sequence for the created BST:")
root.Inorder_display()