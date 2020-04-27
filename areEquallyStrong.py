def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):

    return {yourLeft, yourRight} == {friendsLeft, friendsRight}


yourLeft = 10
yourRight = 15
friendsLeft = 15
friendsRight = 10
print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))