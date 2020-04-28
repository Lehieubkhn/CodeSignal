def evenDigitsOnly(n):
    str1 = str(n)
    array = list(str1)
    return all((int(x) % 2 == 0) for x in array)


n = 248622
print(evenDigitsOnly(n))