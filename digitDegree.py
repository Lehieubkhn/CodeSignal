def digitDegree(n):
    if n < 10:
        return 0
    sum_recur = sum(int(i) for i in str(n))
    return digitDegree(sum_recur) + 1

n = 777
print(digitDegree(n))