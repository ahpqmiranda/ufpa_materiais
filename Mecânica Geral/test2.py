import numpy as np
from sympy import *
from sympy.interactive import init_printing

init_printing(pretty_print=True, use_latex="mathjax")
x, y = var("x y", real=True)
from anastruct.fem.system import SystemElements
import matplotlib.pyplot as plt


def analise_esfor(L_span1, L_span2, q1, q2, load_factor):
    L = L_span1 + L_span2
    q_span1 = load_factor * q1
    q_span2 = load_factor * q2
    q = q_span1 + q_span2

    # E = módulo de young; A = área da secção; I = momento de inércia
    EA = 15000
    EI = 5000

    # Estrutura
    ss = SystemElements(load_factor=load_factor, EA=EA, EI=EI)
    ss.add_element(location=[[0, 0], [L_span1, 0]])  # Vão 1
    ss.add_element(location=[[L_span1, 0], [L, 0]])  # Vão 2

    ss.add_support_hinged(node_id=1)  # Suporte 1
    ss.add_support_hinged(node_id=3)  # Suporte 3
    ss.q_load(element_id=[1], q=-q_span1, direction='element')  # Carga Vão 1
    ss.q_load(element_id=[2], q=-q_span2, direction='element')  # Carga Vão 2

    ss.solve()

    fig = ss.show_structure(show=False,
                            figsize=(12, 5),
                            scale=0.6)
    plt.title("Diagrama da Estrutura")
    plt.xlabel("metros")
    plt.tight_layout()
    plt.show()
    # Apoios Força Vertical, Fy:
    Fy_1 = round(ss.get_node_results_system(node_id=1)["Fy"], 3)
    Fy_2 = round(ss.get_node_results_system(node_id=2)["Fy"], 3)
    Fy_3 = round(ss.get_node_results_system(node_id=3)["Fy"], 3)
    x = var("x", interval=(0, L))

    def func_Fy(x):
        if x == 0:
            return Fy_1 + q_span1 * x
        elif (x > 0) & (x < L_span1):
            return Fy_1 + q_span1 * x
        elif (x == L_span1):
            return Fy_1 + q_span1 * L_span1
        elif (x > L_span1) & (x < L):
            return Fy_1 + q_span1 * L_span1 + q_span2 * (x - L_span1)
        else:
            return 0

    # Dimensão vão 1 para Mmax(+)
    zero = np.max(solve(Eq(func_Fy(x), 0), x))

    # momento máximo negativo:
    M_negativo = round(integrate(func_Fy(x), (x, 0, L_span1)), 2)

    # Dimensão vão 2 para Mmax(+)
    zero_1 = L_span1 + np.max(solve(Eq(func_Fy(L_span1) + q_span2 * x), x))

    # Momento Máximo (+) para vão 2
    M_positivo_2 = round(ss.get_element_results(element_id=2)["Mmin"], 3)

    # Gráfico Momentos
    fig = ss.show_bending_moment(show=False,
                                 offset=(0, -1),
                                 figsize=(12, 5),
                                 scale=0.6,
                                 factor=.01)
    plt.title("Diagrama do Momento Fletor ($M$)")
    plt.xlabel("metros")
    plt.tight_layout()
    plt.text(zero, 0.2, "| {} m".format(round(zero, 3)), fontsize=14)
    plt.text(zero_1, 0.2, "| {} m".format(round(zero_1, 3)), fontsize=14)
    plt.show()
    print("A localização do Momento Máximo positivo para a força 1 "
          "ocorre aos {:.3f} metros e é de {:.3f} kNm".format(zero, (integrate(func_Fy(x), (x, 0, zero)))))
    print("A localização do Momento Máximo positivo da força 2 ocorre aos {:.3f} metros"
          " e é de {:.3f} kNm".format(zero_1, -M_positivo_2))
    print("O Momento máximo do sistema é de {:.3f} kNm".format(M_negativo))
    return None


# Esforços na barra
L = float(input('Digite o tamanho do vão entre os apoios:\n'))
load_factor = float(input('Digite o fator de segurança:\n'))
spam_1 = float(input('Digite a distância do primeiro carregamento:\n'))
q1 = float(input('Digite o valor do carregamento 1:\n'))
spam_2 = float(input('Digite a distância do carregamento 1 para o 2:\n'))
q2 = float(input('Dgite o valor do carregamento 2:\n'))

analise_esfor(spam_1, spam_2, q1, q2, load_factor)
