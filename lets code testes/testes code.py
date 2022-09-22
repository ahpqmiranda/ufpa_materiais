import numpy as np
import pandas as pd
import urllib.parse as up


tabela = {
    'Maria': {'Nota 1': 5, 'Nota 2': 6.5},
    'Pedro': {'Nota 1': 8, 'Nota 2': 10},
    'Rafael': {'Nota 1': 9, 'Nota 2': 7.5}
    }

print(tabela['Rafael']['Nota 2'])