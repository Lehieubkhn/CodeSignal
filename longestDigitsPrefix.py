def longestDigitsPrefix(inputString):
    result = ""
    for i in inputString:
        if i.isdigit():
            result += i
        else:
            break
    return result