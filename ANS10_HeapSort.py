#ANS10 - Submitted by Tatwamasi Mishra, UCSE20040

#this program implements heap sort algorithm to sort a given array
#in increasing order

def heapify(array, n, i):
    largest = i
    left = 2 * i + 1     # left = 2*i + 1
    right = 2 * i + 2     # right = 2*i + 2
  
    #checking if left child of root exists and is
    #greater than root
    if left < n and array[i] < array[left]:
        largest = left
  
    #checking if right child of root exists and is
    #greater than root
    if right < n and array[largest] < array[right]:
        largest = right
  
    #changing root and heapifying otherwise
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  
        heapify(array, n, largest)

def buildheap(array) :
  """this function builds a maxheap"""
  n = len(array)
  for i in range(n // 2 - 1, -1, -1):
      heapify(array, n, i)

def heapSort(array):
  """this function sorts the given array"""
  buildheap(array)
  for i in range(len(array)-1, 0, -1):
      array[i], array[0] = array[0], array[i]
      heapify(array, i, 0)
  
#driver code
array = [ 23, 1, 5, 25, 78, 16]
heapSort(array)
n = len(array)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %array[i], end=" ")