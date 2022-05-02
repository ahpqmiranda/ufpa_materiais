import numpy as np


def funcao(x):
    y = x ** 2 - 3
    return y


def cordas():
    a = float(input('Digite o limite inferior:\n'))
    b = float(input('Digite o limite superior:\n'))
    repeat = int(input('Digite o número de repetições/interações:\n'))
    i = 0

    while i < repeat:
        x = (funcao(b) * a - funcao(a) * b) / (funcao(b) - funcao(a))
        signal_test = 0 > np.sign(funcao(x))

        if signal_test:
            a = x
        else:
            b = x

        i = i + 1
        texto = '{} | {} | {} | {} | {}\n'.format(i, a, b, funcao(a), funcao(b))
        print(texto)

    return None


cordas()
