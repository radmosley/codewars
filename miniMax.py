def miniMaxSum(arr):
    answers = sum(arr)
    minimax = [] 
    for x in arr:
        answers -= x
        minimax.append(answers)
        answers += x
    return '{} {}'.format(min(minimax), max(minimax))


alist = [1,2,3,4,5]
print(miniMaxSum(alist))