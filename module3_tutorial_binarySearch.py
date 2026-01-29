'''
Jeremy Baltazar
M03 Binary Search
'''

arr: list = [0, 1, 2, 3, 4, 5, 6]
k: int = 0
for i in range(len(arr)):
    if arr[i] == k:
        print(f"{k} is in position {i}.")
        break
else:
    print(f"{k} is not present")
    
    