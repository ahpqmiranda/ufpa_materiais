from typing import Tuple, Any

import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import seaborn as sns


def visualization(tx, col, trdv, index):
    temp = np.linspace(100, 200, 1000)
    py = csp(temp)
    plt.style.use('seaborn-poster')
    fig = plt.figure(figsize=(21, 9))
    plt.plot(temp, py, 'g')
    ax = plt.axes(projection='3d')
    ax.scatter(temp,
               py,
               trdv,
               cmap='viridis',
               linewidth=0.25)
    # plt.scatter(database_dataframe['PC1'], database_dataframe['PC2'], database_dataframe['PC3'])
    plt.title("PCA's 3D visualization: ")
    plt.show()

    return


file = pd.read_csv('table_termo_100_200.csv',
                   sep=';',
                   encoding='unicode_escape'
                   )
df = pd.DataFrame(file)
df = df.replace({',': '.'}, regex=True)
T = df.iloc[:, :1].squeeze()
P = df.iloc[:, 1:2].squeeze()
csp = CubicSpline(T, P, bc_type='natural')
a = df.iloc[:1]
print(enumerate(a))


for i, k in enumerate(a):
    if i > 2:
        trdone = df.iloc[:, i:(i+1)].squeeze()
        visualization(T, str(k), trdone, i)
