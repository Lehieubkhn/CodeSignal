def absoluteValuesSumMinimization(a):
    result = []
    for i in a:
        sum = 0
        for j in a:
            sum += abs(j - i)
        result.append(sum)
    
    min_element = min(result)
    return a[result.index(min_element)]


a = [2, 4, 7]
print(absoluteValuesSumMinimization(a))