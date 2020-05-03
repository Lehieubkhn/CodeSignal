def isMAC48Address(inputString):
    arr = inputString.split("-")
    if len(arr) != 6:
        return False
    for x in arr:
        if not isCorrectFomat(x):
            return False
    return True

def isCorrectFomat(str):
    if len(str) != 2:
        return False
    for i in str:
        if not ord("0") <= ord(i) <= ord("9") and not ord("A") <= ord(i) <= ord("F"):
            return False
    return True

inputString = "12-34-56-78-9A-"
print(isMAC48Address(inputString))