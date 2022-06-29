import anastruct.fem.system as afs
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd


def stress_line(force, inertia):
    points = np.linspace(0, 2, 100)
    curve = lambda x: force * (L_spam - x) * (lado / 2) * (1 / I)
    data_points = []
    for point in points:
        data_points.append(curve(point))
    return data_points


E = 205e+9  # [Pa] Modulo de Young do SAE 1020
lado = 100e-3  # [m] Lado da seção da estrutura
A = lado ** 2  # [m^2] Area da seção
I = 1 / 12 * lado ** 4  # [m^4] Momento de Inercia da seção
L_spam = 2  # [m] Comprimento do Vão
load = -8e+3  # [N] Carga do Vão

ss = afs.SystemElements(load_factor=1, EA=E * A, EI=E * I)  # Inicialização do sistema
ss.add_element(location=[[L_spam, 0]])  # "node" do engaste da viga
ss.add_support_fixed(node_id=1)  # suporte da viga é um engaste
ss.point_load(node_id=2, Fy=load)  # carga na extremidade oposta do engaste

ss.solve()
plt.style.use("ggplot")
fig1 = ss.show_structure(show=False, figsize=(12, 5), scale=0.6)
plt.title("Diagrama da Estrutura")
plt.xlabel("metros")
plt.ylabel("metros")
plt.legend(["R: " + str(-load / 1000) + " kN"])
plt.tight_layout()
plt.savefig("estrutura.png")
plt.show()

fig2 = ss.show_bending_moment(show=False, figsize=(12, 5), scale=0.6)
plt.title("Diagrama de Momento de Fletor")
plt.xlabel("metros")
plt.ylabel("metros")
plt.legend(["T: " + str(-load * L_spam / 1000) + " kNm"])
plt.text(0.0, 0.4, "M: " + str(-load * L_spam / 1000) + " kNm")
plt.tight_layout()
plt.savefig("momento.png")
plt.show()

fig3 = ss.show_displacement(show=False, figsize=(12, 10), scale=1)
red_patch = mpatches.Patch(color="red", label="Deformação (m)")
plt.title("Diagrama de deslocamento")
plt.xlabel("metros")
plt.legend(handles=[red_patch])
plt.axis([-0.1, L_spam + 0.1, -1.7, 1])
plt.tight_layout()
plt.savefig("deslocamento.png")
plt.show()

fig4 = ss.show_reaction_force(show=False, figsize=(12, 5), scale=0.6)
plt.title("Diagrama de Força de Reação do Engaste")
plt.xlabel("metros")
plt.ylabel("metros")
plt.legend(["T: " + str(-load * L_spam / 1000) + " kNm", "R: " + str(-load / 1000) + " kN"])
plt.tight_layout()
plt.savefig("reacao.png")
plt.show()


fig5 = ss.show_structure(show=False, figsize=(12, 4), scale=0.6)
y = stress_line(load, I)
y = pd.Series(y) / 1e+7
x = np.linspace(0, L_spam, 100)
red_patch = mpatches.Patch(color="r", label="Sigma max: " + str(load * L_spam * lado / (2e+6 * I)) + " MPa")
plt.plot(x, y, color='r', linestyle='-')
plt.title('Tensão ao longo da barra (MPa/m)')
plt.grid(True)
plt.axis([-0.2, L_spam + 0.2, min(y) - 0.5, max(y) + 5])
plt.legend(handles=[red_patch])
plt.xlabel("metros")
plt.ylabel("10^7 Pa")
plt.tight_layout()
plt.savefig("tensao.png")
plt.show()

