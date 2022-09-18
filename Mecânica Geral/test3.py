import numpy as np
from sympy import *
from sympy.interactive import init_printing

init_printing(pretty_print=True, use_latex="mathjax")
x, y = var("x y", real=True)
from anastruct.fem.system import SystemElements
import matplotlib.pyplot as plt


def anastructs():
    q1_load = 2 # kN/m
    load_factor = 1
    momentum = 6
    L = 2
    # valores escolhidos para a utilização da biblioteca anastruct
    EI = 5000  # EI e EA referentes ao material aplicado
    EA = 15000
    qq = SystemElements(load_factor=load_factor, EI=EI, EA=EA)
    qq.add_element(location=[[0, 0], [L, 0]])  # apenas um fixador par viga em balanço (engastamento da barra)
    qq.add_element(location=[[0, 0], [L, 0]])  # momento fletor no final da barra
    qq.add_element(location=[[0, 0], [L, 0]])  # carregamento distribuido
    qq.add_support_fixed(node_id=1)  # o engastamento da barra é fixo
    qq.moment_load(node_id=2, Ty=-momentum)
    qq.q_load(-q1_load, element_id=3, direction='y')

    qq.solve()
    fig = qq.show_structure(show=False,
                            figsize=(12, 5),
                            scale=0.6)
    plt.title("Diagrama da Estrutura")
    plt.xlabel("x: m")
    plt.ylabel('y: N (0.6 scale)')
    plt.tight_layout()

    plt.savefig('Diagrama_de_Estrutura_(escala_0.6).png')
    plt.show()
    fig2 = qq.show_reaction_force(show=False,
                            figsize=(12, 5),
                            scale=0.6)
    plt.title("Diagrama de Reações (escala 0.6)")
    plt.xlabel("x: m")
    plt.ylabel('y: N (0.6 scale)')
    plt.tight_layout()

    plt.savefig("Diagrama_de_Reações_(escala_0.6).png")
    plt.show()
    fig3 = qq.show_results(show=False,
                            figsize=(12, 12),
                            scale=0.6)
    plt.title("Tabela de resultados")
    plt.xlabel("x: metros")
    plt.ylabel('y: graph')
    plt.tight_layout()
    plt.savefig("Tabela_de_resultados.png")
    plt.show()
    #  qq.show_displacement()
    #  qq.show_shear_force()

    return None


anastructs()
