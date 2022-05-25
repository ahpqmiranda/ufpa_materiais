import numpy as np
import math

import pandas as pd


def vetores_degrees_to_rad(angulos_diretores, mag):
    coss_dir = []
    for index, value in enumerate(angulos_diretores):
        coordinate = math.radians(value)
        coss = np.cos(coordinate)
        coss_dir.append(coss)
    F1_vetorial = np.dot(mag, coss_dir)
    texto = "angulos diretores: {} \n" \
            "magnitude: {} \n" \
            "força vetorial: {} \n" \
            "cossenos diretores: {}".format(pd.Series(angulos_diretores).tolist(), mag, pd.Series(F1_vetorial).tolist(), coss_dir)
    return print(texto)


def vetores_radians_to_degrees(coss_diretores, mag):
    angles = []
    coss = []
    for index, value in enumerate(coss_diretores):
        coss_rad = np.arccos(value)
        degrees = np.degrees(coss_rad)
        angles.append(degrees)
        coss.append(value)
    f1_vetorial = np.dot(mag, coss)
    texto = 'angulos diretores: {}\n' \
            'força vetorial: {}\n' \
            'magnitude da força: {}'.format(angles, f1_vetorial, mag)
    print(texto)

### questão 1
'''
f1_mag = 180
f1_ang_degrees = [60, 135, 60]
print(vetores_degrees_to_rad(f1_ang_degrees,f1_mag))
f2_mag = 50
f2_ang_radians = [0, 7 / 25, -24 / 25]
print(vetores_radians_to_degrees(f2_ang_radians, f2_mag))
'''
### questão 2

gravidade = 9.81
massa = 30
P = massa * gravidade
