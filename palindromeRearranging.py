def palindromeRearranging(inputString):
    dict1 = {}
    for i in inputString:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    even = odd = 0
    for i in dict1:
        if dict1[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == len(dict1) or odd == 1:
        return True
    return False


inputString = "zyyzzzzz"
print(palindromeRearranging(inputString))