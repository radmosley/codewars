def birthdayCakeCandles(ar):
    count = 0
    candles = max(ar)
    for x in ar:
        if x == candles:
            count += 1
    return count

alist = [3, 2, 1, 3]
print(birthdayCakeCandles(alist))