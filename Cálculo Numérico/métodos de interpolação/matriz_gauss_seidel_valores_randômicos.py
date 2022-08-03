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


dim = 5
x = np.random.randint(1, 100, (dim, dim)) # x será uma matriz tipo ndarray-numpy com valores entre 1 e 100 e tamanho 3x3
y = np.random.randint(1, 100, (dim, 1))
x0 = np.random.randint(1, 100, (dim, 1))
beta = beta_max(x)
if True:
    beta_media = (np.sum(beta))/dim
    if beta_media < 1:
        print('A matriz converge para uma solução por Gauss Seidel\n')
        gsm = gauss_seidel(x, y, x0, 0.0001)
        texto = 'Matriz Randômica: \n{} \n Matriz inicial: \n{}' \
                '\nChute Inicial:\n{}\n Beta: {}\nMatriz Resultados:\n{}'.format(x, y, beta, gsm)
        print(texto)

    else:
        print('A matriz não converge para uma solução por Gauss Seidel\n')
        print('Matriz Randômica: \n{}\n '.format(x))
        print('Matriz inicial: \n{}\n'.format(y))
        print('Chute Inicial:\n{}\n '.format(beta))





