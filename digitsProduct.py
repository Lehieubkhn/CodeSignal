from functools import reduce
def digitsProduct(product):
    if product == 1: 
        return 1
    for x in range(1, 10000):
        if reduce(lambda a, b: int(a) * int(b), str(x), 1) == product:
            return x
    else:
        return -1