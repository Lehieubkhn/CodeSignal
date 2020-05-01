from itertools import permutations as p 

def stringsRearrangement(inputArray):
    possible_permutation = p(inputArray)
    for permu in possible_permutation:
        all_match = True
        for j in range(len(permu) - 1):
            if not is_differ_by_one_char(permu[j], permu[j + 1]):
                all_match = False
                break
        if all_match:
            return True
    return False


def is_differ_by_one_char(arr1, arr2):
    count = 0
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            count += 1
    return count == 1


inputArray = ["abc", 
 "abx", 
 "axx", 
 "abx", 
 "abc"]
print(stringsRearrangement(inputArray))