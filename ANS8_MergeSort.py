#ANS8 - Submitted by Tatwamasi Mishra, UCSE20040

#this program implements merge sort algorithm

def mergeSort(myList):
    
    #splitting given list into two halves to be sorted
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        #iterators for traversing the two halves
        i = 0
        j = 0
        
        #iterator for the main list
        k = 0
        
        #merging into new list with elements in increasing order
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

#driver code
myList = [8, 26, 15, 17, 77, 9, 44]
print(f"Original list: {myList}")
mergeSort(myList)
print(f"Sorted list: {myList}")