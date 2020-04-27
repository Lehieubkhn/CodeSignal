def isIPv4Address(inputString):
    array = inputString.split('.')

    if len(array) != 4:
        return False
    for i in array:
        if i.isdigit() == False or i == "":
            return False
        if int(i) < 10 and len(i) == 2:
            return False
        if int(i) < 0 and int(i) > 255:
            return False
    return True    

inputString = "1.1.1.1a"
print(isIPv4Address(inputString))