import numpy as np
import random

from transpose_matrix import naive_transpose_matrix, transpose_matrix
from two_sum import naive_two_sum, two_sum
from add_two_numbers import ListNode, convert_linkedlist_to_list, convert_list_to_linkedlist, add_two_numbers


def test_transpose_matrix():
    for n in range(1, 6):
        for m in range(1, 6):
            # n,m are determined
            matrix = np.random.randint(1, 100, size=(n,m)).tolist()
            assert naive_transpose_matrix(matrix) == transpose_matrix(matrix)


def test_two_sum():
    for n in range(2, 20):
        numbers = np.random.choice(list(range(1, 100)), size=n, replace=False)
        i, j = np.random.choice(np.arange(n), size=2, replace=False)
        numbers[j] = -1 * numbers[i]

        if j < i:
            i, j = j, i
            
        assert sorted(naive_two_sum(numbers, 0)) == [i, j]
        assert sorted(naive_two_sum(numbers, 0)) == sorted(two_sum(numbers, 0))


def test_add_two_numbers():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)

    root_1 = convert_list_to_linkedlist([int(x) for x in list(str(num1))[::-1]])
    root_2 = convert_list_to_linkedlist([int(x) for x in list(str(num2))[::-1]])

    total = num1 + num2
    root = convert_list_to_linkedlist([int(x) for x in list(str(total))[::-1]])

    try:
        assert convert_linkedlist_to_list(root) == convert_linkedlist_to_list(add_two_numbers(root_1, root_2))
    except:
        print('num1: ', num1)
        print('num2: ', num2)
        print('total: ', total)
        assert convert_linkedlist_to_list(root) == convert_linkedlist_to_list(add_two_numbers(root_1, root_2))