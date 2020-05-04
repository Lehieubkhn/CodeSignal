def longestWord(text):
    temp =""
    for i in text:
        if i.isalpha() or i == " ":
            temp = temp + i
        else:
            temp = temp + " "
    arr = temp.split(" ")
    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)
    for i in arr:
        if len(i) == max_len:
            return i


text = "Ready[[[, steady, go!"
print(longestWord(text))  