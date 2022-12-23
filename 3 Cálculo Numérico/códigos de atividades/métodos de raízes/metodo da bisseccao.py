import numpy as np


def funcao(x):
    y = x ** np.e - x - 2
    return y


def iteracoes():
    a = float(input('Digite o limite inferior:\n'))
    b = float(input('Digite o limite superior:\n'))
    tolerancia = float(input('digite o valor de erro mínimo: \n'))
    iteracoes_max = int(input('Numero máximo de iterações: \n'))
    x = (a + b) / 2
    i = 0

    while i < iteracoes_max:

        logical_test = 0 > np.sign(funcao(x) * funcao(a))

        if logical_test:
            b = x
            x = (a + b) / 2

        else:
            a = x
            x = (a + b) / 2

        i = i + 1
        texto = '{} | {} | {} | {} | {}\n'.format(i, a, b, funcao(a), funcao(b))
        print(texto)

    return

iteracoes()
