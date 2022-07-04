from __future__ import division
import numpy as np

Data_type = object


def fun_jacobi(A, B, x_init, tol, N):
    A = A.astype('double')
    B = B.astype('double')
    x_init = x_init.astype('double')

    n = np.shape(A)[0]
    x = np.zeros(n, dtype=Data_type)
    k = 1
    while k < N:
        for i in np.arange(n):
            x[i] = B[i]
            for j in [np.arange(i, 0), np.arange(0, i + 1)]:
                x[i] -= np.matmul(A[i, j], x_init[j])
            u = A[i, j]
            x[i] /= u
            u = 0

        if np.linalg.norm((x - x_init) / x) < tol:
            break
        x_init = np.copy(x)

    erro = np.linalg.norm((x - x_init) / x)
    texto = 'solução {}\n erro associado: {}'.format(x, erro)
    return texto


matrix_coef = np.array([[20, 10, 10, 10], [4, 25, 15, 8], [7, 40, 20, 10], [20, 50, 22, 15]])
matriz_values = np.array([504, 1970, 970, 601])
x0 = np.array([9, 10, 12, 10])

print(fun_jacobi(matrix_coef, matriz_values, x0, 0.00003, 50))
