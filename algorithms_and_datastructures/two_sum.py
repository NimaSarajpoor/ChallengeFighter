# link: https://leetcode.com/problems/two-sum/

def naive_two_sum(list_of_numbers, target):
    """
    find the indices of the numbers whose sum is `target`
    """
    n = len(list_of_numbers)
    for i in range(n-1):
        for j in range(i+1, n):
            if list_of_numbers[i] + list_of_numbers[j] == target:
                return [i, j]

    return   # according to the problem's assumption, we never reach this part.


def two_sum(list_of_numbers, target):
    """
    performant
    O(nlogn)
    """
    import numpy as np
    IDX = np.argsort(list_of_numbers)
    # using built-in python: 
    # IDX = sorted(range(len(seq)), key=seq.__getitem__)

    i = 0
    j = len(IDX) - 1
    while i < j:
        t = list_of_numbers[IDX[i]] + list_of_numbers[IDX[j]]
        if t == target:
            break
        if t > target:
            j = j - 1
        else: 
            i = i + 1
    
    return [IDX[i], IDX[j]]