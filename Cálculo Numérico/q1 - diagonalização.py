import numpy as np

# Questão 1


def gauss_diagonal(matrix):
    for coluna in range(len(matrix)+1):
        for linha in range(coluna+1, len(matrix)):
            fator = matrix[linha][coluna]/matrix[coluna][coluna]
            for i in range(len(matrix[linha])):
                matrix[linha][i] = matrix[linha][i] - fator*matrix[coluna][i]
    return matrix


# a matriz de resposta está embutida como a quarta coluna da matriz de coeficientes
matrix_sistema_de_equacoes = np.array([[2, 2, -1, 6], [1, 4, -1, 4], [1, -1, 4, -1]])
print(gauss_diagonal(matrix_sistema_de_equacoes))
