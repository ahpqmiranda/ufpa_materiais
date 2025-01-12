#!/usr/bin/env python
# coding: utf-8

# In[13]:


from sympy import symbols, sin, cos, diff, sqrt
from sympy.vector import CoordSys3D
from IPython.display import Image


# In[14]:


Image('12-20.png')


# In[15]:


# Definindo variáveis
t = symbols('t')  # Tempo
i, j, k = symbols('i j k')  # Vetores unitários


# In[16]:


# Função posição vetorial
r = 2 * sin(2 * t) * i + 2 * cos(t) * j - 2 * t**2 * k
r


# In[17]:


# Derivadas para calcular velocidade e aceleração
v = diff(r, t)  # Velocidade
v


# In[18]:


a = diff(v, t)  # Aceleração
a


# In[19]:


# Substituir t = 2 para encontrar os valores numéricos
v_at_2 = v.subs(t, 2)
a_at_2 = a.subs(t, 2)

v_at_2, a_at_2


# In[ ]:




