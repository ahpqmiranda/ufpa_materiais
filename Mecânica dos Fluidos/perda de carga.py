import numpy as np
import statsmodels as sm
import pandas as pd
import math
import sympy as sp
import matplotlib.pyplot as plt

sp. init_printing(use_latex='png', scale=1.0, order='gr-lex',
                    forecolor='Black', backcolor='White')
x = sp.Symbol('x')

f = np.linspace(0, 200, 1000)
# rugosidade da tubulação
E = 1
# Diâmetro interno da tubulação
D = 1
# nº de reynolds para o fluido em questão
re = 1
# função fator de atrito
h = 1 / np.sqrt(f)
# função de colebroke
g = -2 * np.log((E / (D * 3.7) + (2.51 / (re * f))))

data_dic = {
    'Fator de atrito (chute)': f,
    'função 1/√f': h,
    'função de colebroke': g
}

data = pd.DataFrame(data_dic)


def f(x): return 1 / np.sqrt(x) - 2 * np.log((E / (D * 3.7) + (2.51 / (re * x))))
f(x)


def erro_relativo(m, n):
    erro = math.sqrt(math.pow(m - n, 2) / math.sqrt(math.pow(m, 2))) * 100
    return erro


def bissec(a, b, tolerancia, n):
    i = 1
    limite = math.pow(10, tolerancia)
    criteria = (b - a) / 2
    while i <= n:
        criteria = (b - a) / 2
        s = a + criteria
        fp = f(s)
        print(f(a))
        print(f(b))
        print(f(s))
        i = i + 1
        texto = ' {} | {:10f} | {:10f} | {:10f} | {:10f} | {:10f}\n'.format(i - 1, a, b, s, fp, f(a) * f(s), erro_relativo(a, s))
        print(texto)
        if 0 < np.sign(f(a) * f(s)):
            a = s
        else:
            b = s



p = float(input('digite o limite inferior:\n'))
q = float(input('digite o limite superior:\n'))
r = float(input('digite a ordem da tolerancia:\n'))
N = int(input('digite o numero maximo de iteracoes:\n'))
bissec(p, q, r, N)


