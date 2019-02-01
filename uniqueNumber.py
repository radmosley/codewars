def unique(a_list):
    pointer = 0
    while pointer <= len(a_list) + 1:
        for x in a_list:
            print(x)
            pointer += 1

alist = [1,1,1,2,1,1]
print(unique(alist))