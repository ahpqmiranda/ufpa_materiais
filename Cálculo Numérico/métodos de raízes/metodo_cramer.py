import numpy as np
from copy import deepcopy


def cramer(matrix_coef, matrix_answers):
    l = matrix_coef.shape[0]
    D = np.linalg.det(matrix_coef)

    det = np.zeros(l)

    for j in range(l):
        complement = deepcopy(matrix_coef)
        for i in range(l):
            complement[i, j] = matrix_answers[i]
        det[j] = np.linalg.det(complement)

    answer = np.zeros(l)
    for i in range(len(det)):
        answer[i] = det[i] / D
    return answer


matrix_coef = np.array([[20, 10, 10, 10], [4, 25, 15, 8], [7, 40, 20, 10], [20, 50, 22, 15]])
matriz_values = np.array([504, 1970, 970, 601])
print(cramer(matrix_coef, matriz_values))
