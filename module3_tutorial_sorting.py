'''
Jeremy Baltazar
M03 Tutorial Sort Array
'''

def quicksort(arr):
    if len(arr) <= 1: # if the array is 0 or 1 element, it is already sorted.
        return arr

    pivot = arr[len(arr) // 2]   # choose middle element as pivot
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + mid + quicksort(right)

newArray: list = [0, 1, 5, 4, 3, 6, 2, 1, 0]
print(quicksort(newArray))