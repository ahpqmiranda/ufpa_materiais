import pandas as pd
from numpy.linalg import norm, inv
import numpy as np
from copy import deepcopy

# questão 2


def gauss(matrixcof, answers, x, tol):
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


matrix2 = np.array([[5, 2, 1], [2, 1, -1], [1, -1, -2]])
results2 = np.array([9, 4, -1])
x0 = np.array([2, 3, 4])
u, v = gauss(matrix2, results2, x0, 0.005)
u = pd.Series(u)
texto = 'x1 = {:.3f} x2 = {:.3f} x3 = {:.3f} || n iterações: {}'.format(u[0], u[1], u[2], v)
print(texto)

