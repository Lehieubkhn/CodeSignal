def deleteDigit(n):
    max_number = 0
    arr = list(str(n))
    print(arr)
    for i in range(len(arr)):
        temp = arr.pop(i)
        cur_number = int("".join(arr))
        if cur_number > max_number:
            max_number = cur_number
        arr.insert(i, temp)
    return max_number
    
n = 152
print(deleteDigit(n))