def countOcc(string1, string2):
    place = len(string2)-1
    count = 0
    while place > 0:
        if string1 in string2:
            count += 1
            place -= len(string1)
    return count
    
    

str1 = 'abc'
str2 = 'abcabcabc'

print(countOcc(str1, str2))