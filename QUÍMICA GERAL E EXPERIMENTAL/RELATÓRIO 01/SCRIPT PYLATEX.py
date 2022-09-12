import pandas as pd
from sympy import *

mass = 2.521 # [g] CUSO4.5H2O
molar_CUSO4 = 249.6850 # [g/mol] CUSO4.5H2O
molar_H20 = 18.01528 # [g/mol] H20
vol_H20 = 0.1 # [L] H2O
rho_H20 = 1 # [g/L] H20


df = pd.Series({
    'Massa de CUSO4.5H2O [g]': mass,
    'Massa Molar de CUSO4.5H2O [g/mol]': molar_CUSO4,
    'Volume de Solvente (H20) [L]': vol_H20,
    'Mols de CUSO4.5H2O [mols]': mass/molar_CUSO4,
    'Mols de H20 [mols]': vol_H20 * rho_H20 / molar_H20,
    'Concentração [mol/L]': (mass/molar_CUSO4) / vol_H20
})

print(df)
