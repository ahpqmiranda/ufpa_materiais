#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Redefinindo variáveis e corrigindo o cálculo
from sympy import symbols, Eq, diff, solve, sqrt
from IPython.display import Image


# In[16]:


Image('12-17.png')


# In[2]:


# Variáveis
t = symbols('t')  # Tempo
x = 4 * t**4  # Posição em x
y = symbols('y')  # Coordenada y


# In[3]:


# Equação da trajetória
trajectory = Eq(y**2, 4 * x)
trajectory


# In[6]:


# Derivadas para x
vx = diff(x, t)  # Velocidade em x
vx


# In[7]:


ax = diff(vx, t)  # Aceleração em x
ax


# In[8]:


# Substituindo x na equação da trajetória para encontrar y em função do tempo
y_in_terms_of_t = solve(trajectory.subs(x, 4 * t**4), y)[0]
y_in_terms_of_t


# In[9]:


# Derivadas para y em relação ao tempo
vy = diff(y_in_terms_of_t, t)  # Velocidade em y
vy


# In[10]:


ay = diff(vy, t)  # Aceleração em y
ay


# In[11]:


# Intensidade da velocidade
v_magnitude = sqrt(vx**2 + vy**2)
v_magnitude


# In[12]:


# Intensidade da aceleração
a_magnitude = sqrt(ax**2 + ay**2)
a_magnitude


# In[14]:


# Substituir t = 0.5 para encontrar os valores numéricos
vx_at_05 = vx.subs(t, 0.5)
vy_at_05 = vy.subs(t, 0.5)
v_magnitude_at_05 = v_magnitude.subs(t, 0.5)
a_magnitude_at_05 = a_magnitude.subs(t, 0.5)

print(f'Velocidade em x (t = 0.5 s): {vx_at_05:.2f} m/s')
print(f'Velocidade em y (t = 0.5 s): {vy_at_05:.2f} m/s')
print(f'Intensidade da velocidade (t = 0.5 s): {v_magnitude_at_05:.2f} m/s')
print(f'Intensidade da aceleração (t = 0.5 s): {a_magnitude_at_05:.2f} m/s²')



# In[ ]:




