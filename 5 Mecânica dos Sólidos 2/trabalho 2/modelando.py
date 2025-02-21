import pandas as pd
import numpy as np
from anastruct.fem.system import *
from sympy import symbols, Piecewise, integrate, var, solve, Eq

factor = 1 / 1000  # conversão de N para kN
c = 2  # m (comprimento da secção para análise)
# geometria da viga
b = 30 * 10 ** -2  # m (largura da secção)
h = 100 * 10 ** -2  # m (altura da secção)
I_inertia_moment = b * h ** 3 / 12
A_area = b * h
# propriedades do concreto
E = 200 * 10 ** 9  # Pa (módulo de elasticidade)
G = 80 * 10 ** 9  # Pa (módulo de elasticidade transversal)
rho = 2000  # kg/m³ (massa específica do material)
v = 0.3  # (coeficiente de Poisson)

# forças aplicadas
F1 = -4 * 10 ** 3  # N (força aplicada no ponto 1)
F2 = F1
F3 = -12 * 10 ** 3  # N (força aplicada no ponto 3)

# comprimentos dos vãos para carga pontual
b2 = 1.5  # m (comprimento do vão 2)

# carga distribuída móvel
q_movel = -2 * 10 ** 3  # N/m (carga distribuída)

# carga distribuída de peso próprio
g = 9.81  # m/s² (aceleração da gravidade)
q_peso = -A_area * rho * g  # N/m (massa da secção)

# comprimentos dos vãos
L_spam1 = 8 * c  # m
L_spam2 = 2 * c  # m

# coordenadas dos pontos de análise
coord = [[i, 0] for i in range(0, 12)]

coord_apoios = [[0, 0], [16, 0]]
nomes_apoios = ['Ra', 'Rb']

Ra, Rb, Fr_y, x = symbols('Ra Rb Fr_y x', real=True)

Eq1 = Eq(0, Ra + Rb + q_peso * (L_spam1 + L_spam2) + q_movel * (2 * c) + F1 + F2 + F3)  # equilíbrio de forças
print(Eq1.simplify())
print(q_peso, q_movel, F1, F2, F3)

# análise dos momentos a partir de Ra
Eq2 = Eq(q_peso / 2 * 20 ** 2 + q_movel / 2 * (10 ** 2 - 6 ** 2) + F1 * 6 + F2 * 7.5 + F3 * 9 + Rb * 16,
         0)  # equilíbrio de momentos
print(Eq2.simplify())
apoios = solve([Eq1, Eq2], (Ra, Rb))
print(apoios.keys())
Ra = apoios[Ra]
Rb = apoios[Rb]
print(f'Ra = {Ra:2f}, Rb = {Rb:2f}')


def m(x):
    if 0 <= x < 2:
        return Ra * x + q_peso / 2 * x ** 2
    elif 2 <= x < 6:
        return Ra * x + q_peso / 2 * x ** 2
    elif 6 <= x < 8:
        return Ra * x + q_peso / 2 * x ** 2 + q_movel / 2 * (x - 6) + F1 * (x - 6) + F2 * (x - 7.5)
    elif 8 <= x < 10:
        return Ra * x + q_peso / 2 * x ** 2 + q_movel / 2 * (x - 6) + F1 * (x - 6) + F2 * (x - 7.5) + F3 * (x - 9)
    elif 10 <= x < 12:
        return Ra * x + q_peso / 2 * x ** 2 + q_movel / 2 * (x - 6) + F1 * (x - 6) + F2 * (x - 7.5) + F3 * (x - 9) - q_movel / 2 * (x - 12) ** 2
    elif 12 <= x < 14:
        return Ra * x + q_peso / 2 * x ** 2 + q_movel / 2 * (x - 6) + F1 * (x - 6) + F2 * (x - 7.5) + F3 * (x - 9) - q_movel / 2 * (x - 12) ** 2
    elif 14 <= x < 16:
        return Ra * x + q_peso / 2 * x ** 2 + q_movel / 2 * (x - 6) + F1 * (x - 6) + F2 * (x - 7.5) + F3 * (x - 9) - q_movel / 2 * (x - 12) ** 2 + Ra * (x - 16)
    elif 16 <= x <= 20:
        return Ra * x + q_peso / 2 * x ** 2 + q_movel / 2 * (x - 6) + F1 * (x - 6) + F2 * (x - 7.5) + F3 * (x - 9) - q_movel / 2 * (x - 12) ** 2 + Ra * (x - 16)
    else:
        return 0


import matplotlib.pyplot as plt

x = np.linspace(0, 20, 100)
y = [m(xi) for xi in x]
plt.grid(True)
plt.plot(x, y)
plt.savefig('teste.png')
# plt.show()
