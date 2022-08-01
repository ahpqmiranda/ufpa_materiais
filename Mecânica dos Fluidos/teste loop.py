import math

import numpy as np
from scipy import optimize

E = 5.416e-05  # [m] -> Rugosidade da parede interna do duto

Q = 1.9e-3  # [m³/s] -> Vazão no sistema

pi = math.pi

Din = 20.93e-3 # [m] -> Diâmetro interno do duto

A = pi * (Din / 2) ** 2  # [m²] -> Área da secção do tubo

rho = 998 # [kg/m3] -> Densidade do fluido (água)

mu = 1e-3 # [Pa/s] -> Viscosidade dinâmica do fluido (agua)

v = Q / A # [m/s] -> Velocidade do escoamento

Re = rho * Din * v / mu # [] -> n.º de reynolds para o fluido em questão

f0 = 0.009

Lc = 30 * Din
Lt = 20 * Din
Lsec1 = 3  # [m] -> Comprimento da secção 1 do duto
Lsec12 = 12.2  # [m] -> Comprimento da secção 2 do duto
Lsec13 = 6.1  # [m] -> Comprimento da secção 3 do duto

f = 0.026368
fator12 = []
fator13 = []
vazao13 = []
vazao13.append(0.5e-3)
fator12.append(f)
fator13.append(f)
Ltotal12 = Lsec12 + Lc
Ltotal13 = Lsec13 + Lc * 2
i = 0
#%%
while i < 10:
    reynolds13 = rho * Din * vazao13[i] / (A * mu)
    reynolds12 = rho * Din * (1.9/1000 - vazao13[i]) /(A * mu)


    def colebroke12(f, reynolds12=reynolds12):
        return 1 / (f ** 0.5) + 2.0 * np.log10(E / (3.7 * Din) + 2.51 / (reynolds12 * f ** 0.5))


    def colebroke_derivada12(f, reynolds12=reynolds12):
        return -0.5 * f ** (-1.5) - 2.51 * f ** (-1.5) / (reynolds12 * (2.51 * f ** (-0.5) / reynolds12 + 0.27027027027027 * E / Din) * np.log(10))

    def colebroke13(f, reynolds13=reynolds13):
        return 1 / (f ** 0.5) + 2.0 * np.log10(E / (3.7 * Din) + 2.51 / (reynolds13 * f ** 0.5))


    def colebroke_derivada13(f, reynolds13=reynolds13):
        return -0.5 * f ** (-1.5) - 2.51 * f ** (-1.5) / (reynolds13 * (2.51 * f ** (-0.5) / reynolds13 + 0.27027027027027 * E / Din) * np.log(10))


    fator_de_atrito12, results12 = optimize.newton(colebroke12, fator12[i], colebroke_derivada12, full_output=True)
    fator_de_atrito13, results13 = optimize.newton(colebroke13, fator13[i], colebroke_derivada13, full_output=True)


    def resultante2(vazao_sec13, f3=fator_de_atrito13, f2=fator_de_atrito12):
        return Q/((rho * f3 * Ltotal13 + 2078 * Din * A ** 2) / (rho * f2 * Ltotal12) ** (1/2) + 1) - vazao_sec13

    fluxo = optimize.newton(resultante2, vazao13[i])
    fator12.append(fator_de_atrito12)
    fator13.append(fator_de_atrito13)
    vazao13.append(fluxo)
    f12 = fator_de_atrito12
    f13 = fator_de_atrito13
    i += 1