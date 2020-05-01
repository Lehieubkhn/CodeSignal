def extractEachKth(inputArray, k):
    if k > len(inputArray):
        return inputArray

    n = 1
    for i in range(len(inputArray)):
        if i == n*k - 1:
            inputArray[i] = 21
            n += 1
    print(inputArray)
    result = []
    for i in inputArray:
        if i == 21:
            continue
        result.append(i)
    return result

inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(extractEachKth(inputArray, k))
