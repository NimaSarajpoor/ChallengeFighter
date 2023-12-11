# link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/?envType=daily-question&envId=2023-12-11
from collections import Counter

def elements_appear_more_than_25percent(arr):
    """
    A sorted array of integers in ASC order. Return 
    the value that occurs more than 25percent of the time
    """
    # list has a method called `count` which can be used to count the number of times
    # an element appear in a list
    out = None
    for key, val in Counter(arr).items():
        if val/len(arr) > 0.25:
            out = key

    return out