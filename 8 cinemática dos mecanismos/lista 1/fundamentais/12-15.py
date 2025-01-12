#!/usr/bin/env python
# coding: utf-8

# In[14]:


from sympy import symbols, integrate, Eq, solve
from IPython.display import Image


# In[17]:


Image('12-15.png', width=200)


# In[9]:


# Definindo as variáveis
t = symbols('t')  # Tempo
x, y = symbols('x y')  # Coordenadas

# Componentes de velocidade
vx = 32 * t  # Velocidade na direção x
vy = 8       # Velocidade na direção y

# Integração para determinar as posições em função do tempo
x_t = integrate(vx, t)  # Posição x(t)
y_t = integrate(vy, t)  # Posição y(t)

# Adicionando condições iniciais: x(0) = 0, y(0) = 0
x_t = x_t + symbols('C1')  # Constante de integração para x
y_t = y_t + symbols('C2')  # Constante de integração para y


# In[10]:


# Determinando as constantes de integração
C1 = solve(Eq(x_t.subs(t, 0), 0), symbols('C1'))[0]
C2 = solve(Eq(y_t.subs(t, 0), 0), symbols('C2'))[0]
C1, C2


# In[11]:


# Substituindo as constantes nas equações
x_t = x_t.subs(symbols('C1'), C1)
y_t = y_t.subs(symbols('C2'), C2)
x_t, y_t


# In[12]:


# Eliminar t para determinar y em função de x
t_in_terms_of_x = solve(Eq(x_t, x), t)[0]  # Resolver t em termos de x
y_in_terms_of_x = y_t.subs(t, t_in_terms_of_x)  # Substituir t na equação de y
t_in_terms_of_x, y_in_terms_of_x


# In[13]:


x_t, y_t, y_in_terms_of_x


# In[ ]:




