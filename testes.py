import numpy as np


def f(x): return np.exp(x) - 2


a = np.array([1, 2, 3, 4])

b = np.array([[0, 1, 2], [3, 4, 5]])
print(b.ndim)  # ndim devolve a dimensão do array
print(b.shape)  # o comando shape retorna o número de linhas e colunas
# o comando len, utilizado em listas, retorna apenas o tamanho da primeira dimensão de um array, não é recomendado
c = np.arange(0, 99, 3)  # o arange é similar ao range, precisa do (inicio, fim, passo)
print(c)
d = np.linspace(0, 10, 10, endpoint=False) # o quarto parâmetro indica a inclusão do último termo do intervalo,
# no caso o 10
print(d)
# criação de matriz de um
e = np.ones((5, 5))  # precisa ter o argumento como tupla
g = np.zeros((5, 5))  # matriz de zeros
print(e, g)

h = np.random.rand(10, 10)
print(h)

i = np.eye(5)  # cria uma matriz identidade
print(i)
j = np.diag(np.array([1, 2, 3, 4]))  # passa uma matriz diagonal com o array sendo a diagonal principal
print(j)
