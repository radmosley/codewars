import math
new_list = []

def mklist(a, n):
    for i in range(0, len(a), n):
        new_list.append(a[i:i + n])

def diagnol():
    for x in range(len(new_list)):
        for y in range(len(new_list[x])):
            if x % len(x)
            


a_list = [11, 2, 4, 4, 5, 6, 10, 8, -12]
mklist(a_list, 3)
print(diagnol())