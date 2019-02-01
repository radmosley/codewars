def tick(start, end):
    middle = []
    while start == end:
        return start, end
    else:
        return start, middle, end

            


print(tick([1,1], [1,3]))