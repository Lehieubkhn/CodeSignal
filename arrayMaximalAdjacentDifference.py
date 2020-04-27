def arrayMaximalAdjacentDifference(inputArray):
    maximum = 0
    for i in range(1, len(inputArray)):
        absolute = abs(inputArray[i] - inputArray[i - 1])
        if absolute > maximum:
            maximum = absolute
    return maximum