# link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/

import statistics

def naive_median_two_sorted_arrays(numbers_A, numbers_B):
    """
    Find median of all numbers in two sorted arrays
    """
    out = []
    out.extend(numbers_A)
    out.extend(numbers_B)
    
    return float(statistics.median(sorted(out)))


def median_two_sorted_arrays(numbers_A, numbers_B):
    """
    performant
    """
    if len(nums1) == 0:
        return statistics.median(nums2)
        
    if len(nums2) == 0:
        return statistics.median(nums1)
        
    n = len(nums1) + len(nums2)
    if n % 2 != 0:
        m = (n + 1) / 2
    else:
        m = n / 2  # consider m and m + 1

    cntr = 0
    i = 0  # pointer for nums1
    j = 0  # pointer for nums2
    prev = None
    curr = None
    for _ in range(n):
        if cntr == m + 1:
            break

        prev = curr
        if i >= len(nums1):
            val_A = float('inf')
        else:
            val_A = nums1[i]
        
        if j >= len(nums2):
            val_B = float('inf')
        else:
            val_B = nums2[j]

        if val_A <= val_B:
            curr = val_A
            i = i + 1
        else:
            curr = val_B
            j = j + 1
        
        cntr = cntr + 1
    
    if n % 2 != 0:
        out = prev
    else:
        out =  (prev + curr) / 2

    return float(out)