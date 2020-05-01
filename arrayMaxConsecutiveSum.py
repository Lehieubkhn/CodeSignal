def arrayMaxConsecutiveSum(inputArray, k):
    max_sum = count = sum(inputArray[:k])
    i = 0
    while i < len(inputArray) - k:
        count = count + inputArray[i + k] - inputArray[i]
        i += 1
        if count > max_sum:
                max_sum = count
    return max_sum


inputArray = [1, 3, 2, 4]
k = 3
print(arrayMaxConsecutiveSum(inputArray, k))