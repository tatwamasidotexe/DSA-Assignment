#ANS9 - Submitted by Tatwamasi Mishra, UCSE20040

#this program implements quick sort algorithm to sort a given array
#in increasing order

def pivot(array, start, end):
 
    #initializing pivot
    pivot = array[start]
    low = start + 1
    high = end
 
    while True:

        #moving high towards left
        while low <= high and array[high] >= pivot:
          high = high - 1
 
        #moving low towards right 
        while low <= high and array[low] <= pivot:
          low = low + 1
 
        #checking if low and high have crossed
        if low <= high:
          #swapping values to rearrange
          array[low], array[high] = array[high], array[low] 

        #when low > high  
        else:  
          break
 
    #swapping pivot with high so that pivot is at its right position 
    array[start], array[high] = array[high], array[start]
 
    return high #new pivot position

def quick_sort(array, start, end):
    
    if start >= end:
      return
    
    p = pivot(array, start, end)
    
    print("Pivot = ",array[p])
    print("left :", array[start:p])
    print("right :",array[p+1:end+1])
    print("\n")
    
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

#driver code
array = [13, 7, 18, 10, 6, 5, 14, 20]
print(f"Original array: {array}\n")
quick_sort(array, 0, len(array) - 1)
print(f"Sorted array: {array}")