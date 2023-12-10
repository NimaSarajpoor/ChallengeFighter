# link https://leetcode.com/problems/transpose-matrix/description/?envType=daily-question&envId=2023-12-10

def naive_transpose_matrix(matrix):
    """
    naive
    matrix : a nested list of lists
    """
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if len(matrix[i]) != m:
            raise ValueError("The lists inside matrix must be of same size")
        
    out = []
    for j in range(m):
        lst = []
        for i in range(n):
            lst.append(matrix[i][j])
        
        out.append(lst)

    return out


def transpose_matrix(matrix):
    import numpy as np

    return np.transpose(np.array(matrix)).tolist()
