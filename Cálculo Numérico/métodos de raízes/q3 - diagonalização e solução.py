import numpy as np
import time
import pandas as pd

# Questão 3
# Funcao que acha o maior numero entre os valores da coluna passada


def gauss_elimination(number_of_equations, input_equations): # n_equac = numero de equacoes e matrix = matriz de coeficientes
    solution = np.zeros(number_of_equations)
    data = {}
    data['Forward Elimination'] = []
    start = time.perf_counter() * 1000
    # Applying Gauss Elimination
    for i in range(number_of_equations):
        if input_equations[i][i] == 0.0:
            data['status'] = 'Error'
            data['exception'] = ZeroDivisionError
            raise ZeroDivisionError('Divide by zero detected!')

        for j in range(i + 1, number_of_equations):
            ratio = input_equations[j][i] / input_equations[i][i]

            for k in range(number_of_equations + 1):
                input_equations[j][k] = input_equations[j][k] - ratio * input_equations[i][k]

            data['Forward Elimination'].append(np.copy(input_equations))

    # Back Substitution
    solution[number_of_equations - 1] = input_equations[number_of_equations - 1][number_of_equations] / \
                                        input_equations[number_of_equations - 1][number_of_equations - 1]

    for i in range(number_of_equations - 2, -1, -1):
        solution[i] = input_equations[i][number_of_equations]

        for j in range(i + 1, number_of_equations):
            solution[i] = solution[i] - input_equations[i][j] * solution[j]

        solution[i] = solution[i] / input_equations[i][i]
    data['time'] = time.perf_counter() * 1000 - start
    # Displaying solution
    data['solution'] = solution
    data['status'] = 'Good'
    return pd.DataFrame(data)


# a matriz de resposta está embutida como a quarta coluna da matriz de coeficientes
matrix_sistema_de_equacoes = np.array([[7, 3, -2, 15], [1, 4, -2, 6], [2, -2, 6, -4]])
gauss_elimination(3, matrix_sistema_de_equacoes)
print(gauss_elimination(3, matrix_sistema_de_equacoes))

