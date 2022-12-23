import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import scipy.constants as sc
import sympy as sp
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

sp.init_printing(use_latex='png', scale=1.0, order='grlex',
                 forecolor='Black', backcolor='White')
E = 1.5e-4  # [m] -> Rugosidade da parede interna do duto

Din = 1.22  # [m] -> Diâmetro interno do duto

re = 1.7e+5  # n.º de reynolds para o fluido em questão

rho = 998  # [kg/m3] -> Densidade do fluido (agua)

mu = 1e-3  # [Pa/s] -> Viscosidade dinâmica do fluido (agua)

v = 1.0  # [m/s] -> Velocidade média do escoamento

Re = rho * Din * v / mu  # [] -> Numero de Reynolds
# (função) fator de atrito
g = sc.g
start = 1
end = 100
spaces = 100
dispersion = 1
x_lst = []
f_lst = []
fd_list = []
c = 0.009
tolerancia = 1.00e-08


x = sp.Symbol('x')
f = np.linspace(0, 200, 1000)
# rugosidade da tubulação
E = 1.5e-4
# Diâmetro interno da tubulação
Din = 1.22
# nº de reynolds para o fluido em questão
Re = rho * Din * v / mu
# função fator de atrito
h = 1 / np.sqrt(f)
# função de colebroke
g = -2 * np.log((E / (Din * 3.7) + (2.51 / (Re * f))))

data_dic = {
    'Fator de atrito (chute)': f,
    'função 1/√f': h,
    'função de colebroke': g
}

data = pd.DataFrame(data_dic)

data.to_csv('colebroke.csv')

def f(x): return 1 / np.sqrt(x) - 2 * np.log((E / (Din * 3.7) + (2.51 / (Re * x))))
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


'''
def colebroke(f):
    return 1 / (f ** 0.5) + 2.0 * np.log10(E / (3.7 * Din) + 2.51 / (Re * f ** 0.5))


def deriv_colebroke(f):
    return -0.5 * f ** (-1.5) - 2.51 * f ** (-1.5) / (
            Re * (2.51 * f ** (-0.5) / Re + 0.27027027027027 * E / Din) * np.log(10))


while dispersion > tolerancia:
    f = c - ((colebroke(c)) / (deriv_colebroke(c)))
    dispersion = abs(f - c)
    x_lst.append(f)
    f_lst.append(colebroke(f))
    fd_list.append(deriv_colebroke(f))
    c = f

data_df = pd.DataFrame(list(zip(x_lst, f_lst, fd_list)),
                       columns=['fi', 'g(f)', 'g\'(f)'])

plt.style.use('seaborn-bright')
fig = plt.figure(figsize=(10, 6))

m1 = np.array(data_df['fi'], dtype=float)
m2 = np.array(data_df['g(f)'], dtype=float)
m3 = np.array(data_df['g\'(f)'], dtype=float)
x = np.array(range(len(m1)))

plt.plot(x, m1, 'r')
plt.plot(x, m2, 'g')
plt.legend(["fator de atrito", "eq. colebroke"])
plt.axis([0, len(m1), 0, max([max(m1), max(m2)])])
plt.xlabel('Iterações')
plt.ylabel('Aproximações')
plt.title('Método de Newton Raphson')
plt.grid(True)
plt.show()


rugosidade = lambda f: 1 / (f ** 0.5) + 2.0 * np.log10(E / (3.7 * Din) + 2.51 / (Re * f ** 0.5))
list_rugosidade = []

for x in np.linspace(start, end, spaces):
    list_rugosidade.append(rugosidade(x))

x_interval = np.log(np.linspace(start, end, spaces))
xdic = {'X': np.exp(x_interval)}
ydic = {'Y': np.exp(list_rugosidade)}

X = pd.DataFrame.from_dict(xdic)
Y = pd.DataFrame.from_dict(ydic)

x_SEQ = np.linspace(X.min(), X.max(), spaces).reshape(-1, 1)

value = 4  # grau do polinômio

polynomial_regression = make_pipeline(PolynomialFeatures(value), LinearRegression())
polynomial_regression.fit(X, Y)

plt.figure(figsize=(10, 6))
plt.scatter(X, Y)
plt.plot(x_SEQ, polynomial_regression.predict(x_SEQ), color='hotpink')
plt.title('Regressão Polinomial (log x log) de ordem: ' + str(value))
plt.grid(True)
plt.legend(["Dados amostrais", "Interpolador Polinomial"])
plt.xlabel("Rugosidade")
plt.ylabel("Perda de Carga")
plt.show()

# equação de Darcy-Weisbach
L = float(input('Digite o comprimento da tubulação'))
f = data_df['fi'].iloc[-1]
lw = f * L * (v ** 2) / (2 * Din * g)
print(lw)

'''
