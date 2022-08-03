import sympy as sy
from IPython.display import display
import scipy as sp
import pandas as pd
import numpy as np

x, y = sy.symbols('x y')
sy.init_printing()


def interpol_lagrange(z, m, lista_x, lista_y):
    """
    Função que calcula a interpolação de Lagrange para um polinômio de grau m.
    """
    # Calcula o polinômio de Lagrange
    f = m + z
    n = m
    polinomio = 0
    for j in range(n, f):
        interpol_L = 1
        for i in range(0, z):
            if m != i:
                interpol_L *= ((x - lista_x[i]) / (lista_x[m] - lista_x[i]))
        polinomio += (interpol_L * (lista_y[j]))
        m = m + 1
    print(polinomio)

    return polinomio

# aquisição de dados da questão 2
file = pd.read_csv('database_questao2.csv', sep=';', index_col=False)
data_df = pd.DataFrame(file)
pesos = data_df.iloc[1:, 0].squeeze()
idades = data_df.iloc[:1, 1:].squeeze()
data_df.drop(data_df.columns[0], axis=1, inplace=True)  # remove a primeira coluna
data_df.drop(data_df.index[0], inplace=True)  # remove a primeira linha


get_age = float(input('Digite a idade: '))
get_weight = float(input('Digite o peso: '))

if get_age < 20 or get_age > 45:
    print('Idade inválida')
    exit()
if get_weight < 50 or get_weight > 110:
    print('Peso inválido')
    exit()
index_rows = round(get_age / 10 - 2)
index_collumns = round(get_weight / 10 - 5)
X = data_df.iloc[index_rows, :].tolist()
Y = data_df.iloc[:, index_collumns].tolist()
u = interpol_lagrange(3, 0, X, Y)
u = sy.expand(u)
print(u)
print(u.subs(x, 30))
