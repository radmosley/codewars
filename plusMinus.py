# def plusminus(arr):
#     sums = [0,0,0]
#     for i in range(n):
#         if arr[i] > 0:
#             sums[0] += 1
#         elif arr[i] == 0:
#             sums[2] += 1
#         else:
#             sums[1] += 1
#     return sums.split()

# def helper(sums):
#     for i in range(sums):
#         return n/sums[i]

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
# def plusMinus(arr):
#     sums = [0,0,0]
#     for i in range(n):
#         if arr[i] > 0:
#             sums[0] += 1
#         elif arr[i] == 0:
#             sums[2] += 1
#         else:
#             sums[1] += 1
#     def domath(x):
#         return x/n

#     x = map(domath, sums)
#     return list(x)
    

# if __name__ == '__main__':
#     n = int(input())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)

def plusMinus(arr):
    sums = [0,0,0]

    for i in range(n):
        if arr[i] > 0:
            sums[0] += 1
        elif arr[i] == 0:
            sums[2] += 1
        else:
            sums[1] += 1

    def domath(x):
        return x/n

    x = list(map(domath, sums))
    for nums in x:
        print(nums)

n = 6
a_list = [-4, 3, -9, 0, 4, 1]
print(plusMinus(a_list))