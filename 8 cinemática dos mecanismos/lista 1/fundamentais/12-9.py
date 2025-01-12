#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sympy import symbols, diff
from IPython.display import Image


# In[2]:


Image('12-9.png')


# In[3]:


# Função da posição s(t) = 0.5*t^2 para t <= 6, s(t) = 108 para t > 6
t = np.linspace(0, 10, 500)  # Intervalo de tempo de 0 a 10 s
s = np.piecewise(t, [t <= 6, t > 6], [lambda t: 0.5 * t**2, 108])

# Calculando a velocidade v(t)
t_symbol = symbols('t')
s_symbol = 0.5 * t_symbol**2  # Função da posição para t <= 6
v_symbol = diff(s_symbol, t_symbol)  # Derivada de s(t) para t <= 6

# Convertendo para um formato numérico
v = np.piecewise(t, [t <= 6, t > 6], [lambda t: 1 * t, 0])  # v = t para t <= 6, v = 0 para t > 6

# Criando um DataFrame para exibir os dados
data = pd.DataFrame({'Tempo (s)': t, 'Posição (m)': s, 'Velocidade (m/s)': v})
data


# In[4]:


# Exibindo o gráfico
plt.figure(figsize=(10, 6))
plt.plot(t, v, label='v(t)', color='b')
plt.title('Gráfico Velocidade x Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.axvline(x=6, color='r', linestyle='--', label='t = 6 s (mudança)')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




