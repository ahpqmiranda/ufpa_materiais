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


matrix1 = np.array([[2, 2, -1], [1, 4, -1], [1, -1, 4]])
matrix2 = np.array([[5, 2, 1], [2, 1, -1], [1, -1, -2]])
matrix3 = np.array([[7, 3, -1], [1, 4, -1], [2, -2, 6]])
results = np.array([6, 4, -1])
results2 = np.array([9, 4, -1])
results3 = np.array([15, 6, -4])
print(beta_max(matrix2))
matriz_values = np.array([6, 4, -1])
x0 = np.array([9, 10, 12])

print(gauss_seidel(matrix1, results, x0, 0.005))
