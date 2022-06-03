import pandas as pd

file = pd.read_csv('tabela temodinâmica do vapor dágua 100 a 200ºC.csv', sep=';', encoding='unicode_escape', on_bad_lines='skip')
df = pd.DataFrame(file)
print(df)
