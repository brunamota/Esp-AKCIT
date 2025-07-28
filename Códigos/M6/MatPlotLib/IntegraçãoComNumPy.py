import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)  # 100 valores entre 0 e 10
y = np.sin(x)

plt.plot(x, y, label="Sen(x)")
plt.title("Função Senoidal")
plt.xlabel("x")
plt.ylabel("sen(x)")
plt.grid(True)
plt.legend()
plt.show()
