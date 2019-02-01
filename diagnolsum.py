def diagonalDifference(arr):
    n = int(input().strip())
    leftsum = 0
    rightsum = 0
    for i in range(n):
        leftsum += int(arr[i][i])
        rightsum += int(arr[i][n-i-1])
    return abs(leftsum - rightsum)

        
