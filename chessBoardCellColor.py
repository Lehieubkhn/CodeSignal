# Check ascii code for cells: brown if sum is even, otherwise odd

def chessBoardCellColor(cell1, cell2):
    return isBrowncell(cell1) == isBrowncell(cell2)

def isBrowncell(cell):
    num = ord(cell[0]) + ord(cell[1])
    if num % 2 == 0:
        return True
    return False

cell1 = "A1"
cell2 = "C3"
chessBoardCellColor(cell1, cell2)