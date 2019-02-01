def triplets(a,b):
    score = [0,0]
    for x in range(len(a)):
        if a[x] > b[x]:
            score[0] += 1
        if a[x] < b[x]:
            score[1] += 1
    return score

a = [1,2,3]
b = [3,2,1]
a_list = [5, 6, 7,]
b_list = [3,6,10]

print(triplets(a_list,b_list))


#will the list always have an equal number of items in a list?
#will the list ever have duplicates?
