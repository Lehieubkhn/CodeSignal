def chessKnight(cell):
    count = 0
    coordinate = [ord(cell[0]) - 96, int(cell[1])]
    possible_move = [[1, 2],[2, 1],[-1, 2],[-2, 1],[1, -2],[2, -1],[-1, -2],[-2, -1]]

    for i in possible_move:
        if 1 <= coordinate[0] + i[0] <= 8 and 1 <= coordinate[1] + i[1] <= 8:
            count += 1
    
    return count
cell = "a1"
print(chessKnight(cell))