def buildPalindrome(st):
    temp_str = ""
    for i in range(len(st)):
        if isPalindrome(st + temp_str):
            return st + temp_str
        else:
            temp_str = st[i] + temp_str


def isPalindrome(st):
    return st == st[::-1]
st = "abbac"
print(buildPalindrome(st))