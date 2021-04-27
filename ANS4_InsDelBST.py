#ANS4 - Submitted by Tatwamasi Mishra, UCSE20040

#this program implements insertion into and deletion from a BST

class Node :
  def __init__(node, data) :
    node.data = data
    node.left = None
    node.right = None
  
  #function to insert nodes into BST
  def insertBST(node, data):
        if node.data:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                else:
                    node.left.insertBST(data)
            elif data > node.data:
                if node.right == None:
                    node.right = Node(data)
                else:
                    node.right.insertBST(data)
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

#function to find min value
def findmin(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

#function to delete node from the BST
def deleteBSTnode(root, item) :
 
    #when item not found 
    if root == None :
      print("Node doesn't exist in the BST.")
      return root
    
    #traversing tree to get to the node to be deleted
    if item < root.data :
        root.left = deleteBSTnode(root.left, item)
    elif item > root.data :
        root.right = deleteBSTnode(root.right, item)

    #reached the node to be deleted
    else:
        #when node is a leaf
        if root.left == None :
          temp = root.right
          root = None
          return temp
 
        elif root.right == None :
          temp = root.left
          root = None
          return temp
 
        #when node has two children
        temp = findmin(root.right) #finding inorder successer
        root.key = temp.data
        root.right = deleteBSTnode(root.right, temp.data)
 
    return root

#function to display BST after deletion of node
def postDeldisplay(root):
    if root != None:
        delDisplay(root.left)
        print(root.data, end=" ")
        delDisplay(root.right)

#driver code
array = [12, 2, 56, 82, 22, 5, 45, 9]
root = Node(array[0])

for node in array[1:]:
  root.insertBST(node)
print("Printing pre-order sequence for the created BST:")
root.Preorder_display()

print("\nPrinting in-order sequence for the created BST:")
root.Inorder_display()

#while loop asking user input for insertion
while True :
  x = int(input("\nDo you want to insert new elements? Type 1 for yes, 0 for no. "))
  if x == 1:
    root.insertBST(int(input("Enter data to be inserted: ")))
  elif x == 0 :
    break
  else :
    print("Invalid input! Try again.")
    continue

print("\nPrinting in-order sequence after insertion:")
root.Inorder_display()

#while loop asking user input for deletion
while True :
  node = int(input("\nEnter node to be deleted: "))
  deleteBSTnode(root, node)
  print(f"\nInorder sequence after deleting {node}: ")
  postDeldisplay(root)

  x = int(input("\nDo you want to delete another element? Type 1 for yes, 0 for no. "))
  if x == 1:
    node = int(input("\nEnter node to be deleted: "))
    deleteBSTnode(root, node)
    print(f"\nInorder sequence after deleting {node}: ")
    postDeldisplay(root)
  elif x == 0 :
    print("\nThank you!")
    break
  else :
    print("Invalid input! Try again.")
    continue