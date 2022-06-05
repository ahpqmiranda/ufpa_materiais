import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import seaborn as sns


file = pd.read_csv('table_termo_100_200.csv',
                   sep=';',
                   encoding='unicode_escape'
                   )
df = pd.DataFrame(file)
df = df.replace({',': '.'}, regex=True)
T = df.iloc[:, :1].squeeze()
P = df.iloc[:, 1:2].squeeze()
csp = CubicSpline(T, P, bc_type='natural')

tx = np.linspace(100, 200, 100)
py = csp(tx)
plt.style.use('seaborn-poster')
fig = plt.figure(figsize=(21, 9))
plt.plot(tx, py, 'g')
# plt.plot(T, P, 'bo')
plt.title('Interpolação Spline Cubica')
plt.xlabel('Temperatura (Cº)')
plt.ylabel('Pressão (bar)')
plt.show()

'''
correlation = csp_df.corr()
mask = np.triu(np.ones_like(correlation), dtype='bool')
f, ax = plt.figure(figsize=(11,9))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(correlation, mask=mask, cmap=cmap, vmax=200, center=0, square=True, linewidth=.5, cbar_kws={"shrink:.5"})
'''
