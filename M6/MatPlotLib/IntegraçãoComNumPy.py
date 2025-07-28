import matplotlib.pyplot as plt

# Gráfico de barras
df.plot(kind='bar', x='Nome', y='Salário', legend=False)
plt.title("Salário por Pessoa")
plt.ylabel("Salário")
plt.grid(True)
plt.show()

# Histograma
df['Salário'].hist(bins=5)
plt.title("Distribuição Salarial")
plt.xlabel("Salário")
plt.show()
