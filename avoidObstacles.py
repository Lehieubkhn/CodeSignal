def avoidObstacles(inputArray):
    inputArray.sort()
    last_value = inputArray[len(inputArray) - 1]
    for i in range(1, last_value + 2):
        if all(n % i != 0 for n in inputArray):
            return i
        i += 1
                   

inputArray = [1, 4, 10, 6, 2]
print(avoidObstacles(inputArray))