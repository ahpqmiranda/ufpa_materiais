import matplotlib.pyplot as plt
import numpy as np
import cv2

# Carregar a imagem original
image_path = "grafico_modulo_vs_densidade.png"
image = cv2.imread(image_path)

# Converter a imagem para RGB (OpenCV carrega em BGR por padrão)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Dimensões da imagem
height, width, _ = image.shape

# Criar um gráfico sobreposto para desenhar as retas
fig, ax = plt.subplots(figsize=(10, 7))
ax.imshow(image, extent=[1, 10000, 0.0001, 1000], aspect='auto')

# Gerar pontos para as retas
x_vals = np.logspace(1, 10000, 500)

# Inclinação 1.5 para questão 1.b e 2.a
y_vals_blue = 10 * (x_vals / 100)**1.5  # Passando pelo ponto (100,10) conforme indicado na questão 2.a
y_vals_red = 10 * (x_vals / 100)**1.5   # Mesmo declive, mesma referência

# Plotar as retas
ax.plot(x_vals, y_vals_blue, '--', color='blue', linewidth=2, label='Questão 1.b (Azul)')
ax.plot(x_vals, y_vals_red, '--', color='red', linewidth=2, label='Questão 2.a (Vermelho)')

# Configuração de escala log-log
ax.set_xscale('log')
ax.set_yscale('log')

# Rótulos
ax.set_xlabel("Densidade ρ (kg/m³)")
ax.set_ylabel("Módulo de Young E (GPa)")
ax.set_title("Gráfico Modificado com Retas de Inclinação 1.5")
ax.legend()

# Mostrar o gráfico
plt.show()
