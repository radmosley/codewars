""" 
Given an array A of N elements. The task is to complete the function 
which returns true if triplets exists in array A whose sum is zero else 
returns false.
"""

def findTriplets(arr, n):
    a = 1
    b = n - 1

    for x in range(n):
        if a > b:
            if arr[x] + arr[a] + arr[b] == 0:
                return 1

alist = [0, -1, 2, -3, 1]
print(findTriplets(alist, len(alist)))