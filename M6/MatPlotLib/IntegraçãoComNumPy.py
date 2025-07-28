import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(5, 5)
print("Médias por linha:", np.mean(data, axis=1))
print("Médias por coluna:", np.mean(data, axis=0))

plt.bar(range(5), np.mean(data, axis=1))
plt.title("Média por Linha")
plt.show()
