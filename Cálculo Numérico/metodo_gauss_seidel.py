from numpy.linalg import norm, inv
import numpy as np
from copy import deepcopy


def gauss_seidel(matrixcof, answers, x, tol):
    L = np.tril(matrixcof)
    U = matrixcof - L
    i = 0

    while True:
        x_init = deepcopy(x)
        x = np.dot(inv(L), answers - np.dot(U, x))
        i = i + 1

        if i > 2:
            if (norm(x - x_init)) / norm(x) < tol:
                return x, i


def beta_max(coef):
    beta_list = []
    coef = coef.astype('float64')
    n = np.shape(coef)[0]
    beta = 0
    for i in range(n):
        for j in range(n):
            if not i == j:
                beta += pow(coef[i, j], 2) ** (1 / 2)
        beta /= coef[i, i]
        beta_list.append(beta)
        print('linha: {} ; beta {:.3f}'.format(i+1, beta))
    return beta_list


matrix_coef = np.array([[20, 10, 10, 10], [4, 25, 15, 8], [7, 40, 20, 10], [20, 50, 22, 15]])
print(beta_max(matrix_coef))
matriz_values = np.array([504, 1970, 970, 601])
x0 = np.array([9, 10, 12, 10])

print(gauss_seidel(matrix_coef, matriz_values, x0, 0.005))
