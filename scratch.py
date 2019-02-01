
def Greed(arr):
    for x in range(len(arr)):
        counter = 0
        score = 0
        doubles = []
        if arr[x] in arr[x + 1:len(arr)]:
            counter += 1
        return counter


a_list= [1,1,3,4,5]
print(Greed(a_list))