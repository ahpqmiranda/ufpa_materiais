import numpy as np
import matplotlib.pyplot as plt

# Definição dos pontos da viga
distancia_viga = np.linspace(0, 12, 100)  # Viga de 12 metros
distribuida = 2  # Carga distribuída de 2 tf/m
carga_pontual = [(3, 20), (6, 10), (9, 20)]  # (posição, força)

# Função para calcular o esforço cortante
def esforco_cortante(x, distribuida, cargas):
    V = -distribuida * x  # Esforço cortante devido à carga distribuída
    for pos, carga in cargas:
        if x >= pos:
            V -= carga
    return V

# Função para calcular o momento fletor
def momento_fletor(x, distribuida, cargas):
    M = -0.5 * distribuida * x**2  # Momento devido à carga distribuída
    for pos, carga in cargas:
        if x >= pos:
            M -= carga * (x - pos)
    return M

# Cálculo dos esforços cortantes e momentos fletores
esforcos_cortantes = [esforco_cortante(x, distribuida, carga_pontual) for x in distancia_viga]
momentos_fletores = [momento_fletor(x, distribuida, carga_pontual) for x in distancia_viga]

# Plot dos diagramas
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(distancia_viga, esforcos_cortantes, label="Esforço Cortante", color='b')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.title("Diagrama de Esforço Cortante")
plt.xlabel("Distância (m)")
plt.ylabel("Cortante (tf)")
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(distancia_viga, momentos_fletores, label="Momento Fletor", color='r')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.title("Diagrama de Momento Fletor")
plt.xlabel("Distância (m)")
plt.ylabel("Momento (tf.m)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
