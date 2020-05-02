#idea: check the color of bishop and pawn first: if they have difference color return False
#check the row and column of bishop and pawn. If they have the same column or row, return False
#otherwise return True
def bishopAndPawn(bishop, pawn):
    if isSameColor(bishop) != isSameColor(pawn):
        return False
    if isSameRow(bishop) == isSameRow(pawn):
        return False
    if isSameColumn(bishop) == isSameColumn(pawn):
        return False
    return True


def isSameColor(arr):
    color = ord(arr[0]) + ord(arr[1])
    if color % 2 == 0:
        return True
    return False

def isSameRow(arr):
    return ord(arr[1])

def isSameColumn(arr):
    return ord(arr[0])

bishop = "c1"
pawn = "c3"
print(bishopAndPawn(bishop, pawn))