import string
def isBeautifulString(inputString):

    r = [inputString.count(i) for i in string.ascii_lowercase]
    print(r)
    
    return r[::-1] == sorted(r)



inputString = "aaabbc"
print(isBeautifulString(inputString))