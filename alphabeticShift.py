def alphabeticShift(s):
    #convert to ascii code
    array = [ord(x) + 1 for x in s]

    result = ""
    for i in array:
        if i > 122:
            i = 97
        result += chr(i)
    return result

              
s = "az"
print(alphabeticShift(s))