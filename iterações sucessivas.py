import math

import numpy as np
import matplotlib as plt


def f(x, p):
    soma = 0
    for expoente, coeficiente in enumerate(p):
        soma += coeficiente * math.pow(x, expoente)
    return soma


coef = []
while True:
    n = input('Digite os coeficientes dos polinômios do menor para o maior: ao terminar, digite "fim"')
    if n.isnumeric():
        coef.append(n)
    elif n == 'fim':
        break
    else:
        print('Entrada errada, digite o próximo coeficiente ou "fim" para terminar de inserir os coeficientes')
k = float(input('Digite o valor de x da função:\n'))
coef2 = np.array(coef)
resultado = f(k, coef2)
print(resultado)