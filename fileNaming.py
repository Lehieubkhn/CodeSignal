def fileNaming(names):
    result = []
    for name in names:
        if name not in result:
            result.append(name)
        else:
            k = 1
            new_name = name + "(" +str(k) + ")"
            while new_name in result:
                k += 1
                new_name = name + "(" +str(k) + ")"
            result.append(new_name)
    return result
            
names = ["doc", 
        "doc", 
        "image", 
        "doc(1)", 
        "doc"]
print(fileNaming(names))