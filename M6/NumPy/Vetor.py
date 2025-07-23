# Criando um array de uma dimensão

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
#print("Array a:", a)
#print("Forma do array:", a.shape)
#print("Número de dimensões:", a.ndim)

#print(a*2)

#media = np.mean(a)
#print(media)

soma = a + b
#print(soma)

slicing = a[:2]
slicing2 = a[2:]
a[1:4] = 0
m = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
step_slice = m[1:8:2]
print("Elementos selecionados com step de 2:", step_slice)

