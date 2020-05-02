#idea: find the position of "@" in the address. If after "@" is not a character then we need to 
# find another "@" in the other part.
def findEmailDomain(address):
    position = address.find("@")
    print(position)
    if address[position+1] == ".":
        sub_string = address[position + 1:]
        print(sub_string)
        new_position = sub_string.find("@")
        print(new_position)
        return sub_string[new_position + 1:]
    
    return address[position + 1:]


address = "\"very.unusual.@.unusual.com\"@usual.com"
print(findEmailDomain(address))