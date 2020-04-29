import re
def variableName(name):
    if  name[0].isdigit() == True:
            return False

    patern = "[A-Za-z0-9_]"
    for x in name:
        if re.match(patern, x) == None:
            return False
    return True
        

name = "count?"
print(variableName(name))