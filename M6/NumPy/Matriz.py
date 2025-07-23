# Criando um array bidimensional (matriz)

#impotando a biblioteca
import numpy as np

a = np.array([[1, 2], [3, 4]])
print("Matriz a:\n", a)
print("Forma do array:", a.shape)
print("Número de dimensões:", a.ndim)

print(a*2)

media = np.mean(a)
mediana = np.median(a)
desvio_padrao = np.std(a)
print(media)
print(mediana)
print(desvio_padrao)
