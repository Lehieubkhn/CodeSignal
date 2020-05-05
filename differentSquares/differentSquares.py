def differentSquares(matrix):
    set1 = set()
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            set1.add((matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]))
    return len(set1)



matrix = [[1,2,1], 
        [2,2,2], 
        [2,2,2], 
        [1,2,3], 
        [2,2,1]]

print(differentSquares(matrix))