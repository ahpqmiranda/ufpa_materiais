import numpy as np
import os
import pandas as pd
# resolveu o bug do read_excel instalando o 'openpyxl' via conda forge

file = pd.read_excel('arrecadacao-da-receita-administrada-pela-rfb-por-municipio-2019.xlsx',
                     index_col=None,
                     header=None
                     )
print(file)

def f(x, p):
    result = 0
    for expoente, coeficientes in enumerate(p):
        result += coeficientes * x ** expoente
    return result


lista_coeficientes = []

grau = int(input('Digite o grau do polinômio'))
k = float(input('digite o valor do x\n'))
for i in range(grau):
    n = float(input("Digite o valor para o coeficiente de grau"))
    lista_coeficientes.append(n)
    print(lista_coeficientes)

polinomio = np.poly(lista_coeficientes)
print(polinomio)
print(f(k, polinomio))
