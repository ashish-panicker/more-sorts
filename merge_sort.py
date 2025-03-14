"""
Merge Sort
Divide and conquer algorithm

Algorithm Steps
------------------------------------------------
If the array has 0 or 1 elements, it is already sorted.
Find the middle index of the array.
Recursively apply Merge Sort to the left and right halves.
Merge the sorted halves into a single sorted array.

[8, 4, 7, 3, 1, 5, 9, 2]

Step 1: 
Divide the array into two
Left:   [8, 4, 7, 3]
Right:  [1, 5, 9, 2]

Step 2:
Recursively sort both halves
[8, 4, 7, 3]
Split it into [8,4] and [7,3]
Sort these [4,8] and [3,7]
Merge it into [3,4,7,8]

[1, 5, 9, 2]
Split it into [1,5] and [9,2]
Sort it into [1,5] and [2,9]
Merge it into [1,2,5,9]

Step 3:
Merge the two halves into [1, 2, 3, 4, 5, 7, 8, 9] 
"""

def merge_sort(arr):
  if len(arr) <=1:
    return arr
  
  mid = len(arr) // 2
  # print(arr, mid)
  print(f"Left {arr[:mid]} - Right {arr[mid:]}\n")
  
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  return merge(left, right)

def merge(left, right):
    sorted_array = []
    i = j = 0
    print(f"{left} & {right}")
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    print(f"Sorted array: {sorted_array}")
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    print(f"Sorted array extended: {sorted_array}")
    
    return sorted_array

arr = [8, 4, 7, 3, 1, 5, 9, 2]
print(merge_sort(arr))
