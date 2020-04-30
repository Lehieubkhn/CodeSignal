def circleOfNumbers(n, firstNumber):
    result =  firstNumber + n//2
    if result >= n:
        return result - n
    return result
