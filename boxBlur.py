def boxBlur(image):
    result = []
    for x in range(0, len(image) - 2):
        line = []
        for y in range(0, len(image[x]) - 2):           
            sum1 = 0
            for a in range(x, x + 3):
                for b in range(y, y + 3):
                    sum1 += image[a][b]
            line.append(sum1 // 9)
        result.append(line)
    return result


image = [[7,4,0,1], 
        [5,6,2,2], 
        [6,10,7,8], 
        [1,4,2,0]]

boxBlur(image)