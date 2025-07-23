# NumPy: Processamento de Dados Estruturados Multidimensionais

[Documentação do NumPy](https://numpy-org.translate.goog/devdocs/user/absolute_beginners.html?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc)

## Objetivos

- Entender o que é o NumPy e por que é utilizado
- Aprender a manipular arrays (1D, 2D, 3D)
- Comparar arrays NumPy com listas Python
- Realizar operações matemáticas com arrays
- Utilizar funções universais (ufuncs)
- Gerar gráficos com o Matplotlib
- Praticar com exemplos interativos no PyCharm

## Como funciona?

- Biblioteca fundamental para computação científica com Python
- Suporte para arrays n-dimensionais e operações vetoriais rápidas
- Base para outras bibliotecas: Pandas, SciPy, Scikit-learn

## Exemplos práticos feitos em sala

### Verificar se o NumPy e o Matplotlib estão instalados
- Importar pelo CMD ou pela própria IDE utilizada

``` cmd
pip install numpy matplotlib
```
- Verificar se a instalação foi realizada
``` python
import numpy as np
print("Versão do NumPy:", np.__version__)
```
### Vetores, Matrizes e Tensors

- Vetor = Array 1D (ex: [1, 2, 3])
``` python
import numpy as np
vetor = np.array([1,2,3])
print("Vetor:", vetor)
```
  
- Matriz = Array 2D (ex: [[1,2],[3,4]])
``` python
import numpy as np
matriz = np.array([[1,2],[3,4]])
print("Matriz:", matriz)
```

- Tensor = Array 3D+ (ex: imagem colorida)
``` python
import numpy as np
tensor = np.array([[1,2],[3,4],[5,6],[7,8]])
print("Tensor:", matriz)
```
### Operações com Arrays
- Soma, subtração, multiplicação
- Operações entre arrays e escalar

- Escalar

``` python
import numpy as np

matriz  = np.array([[1, 2, 3],[4, 5, 6]])

print("Adição:", matriz + 10) #  Adição: [[11 12 13]
                              #            [14 15 16]]

print("Subtração:", matriz - 1) #  Subtração: [[0 1 2]
                              #            [3 4 5]]

print("Multiplicação:", matriz * 2) #  Multiplicação: [[ 2  4  6]
                              #            [ 8 10 12]]

print("Divisão:", matriz / 2) #  Divisão: [[0.5 1.  1.5]
                              #            [2.  2.5 3. ]]


```

- Entre arrays
``` python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b
print("Adição:", c) #  Adição: [5 7 9]

d = b - a
print("Subtração:", d) #  Subtração: [3 3 3]

e = a * b
print("Multiplicação:", e) #  Multiplicação: [4 10 18]

f = b / a
print("Divisão:", f) #  Divisão: [4. 2.5 2.]
```

### Funções Universais (ufunc)
- Funções matemáticas aplicadas elemento a elemento
- Exemplos: np.mean, np.sum, np.sqrt, np.exp, np.sin
- np.arange(start, stop, step)
- np.linspace(start, stop, num)

``` python
import numpy as np

array = np.array([1, 2, 3, 4, 5])

print(array[0,1]) # Elemento linha 0, coluna 1: 1

print("Média:", np.mean(array)) #  Média: 3.0
print("Mediana:", np.median(array)) #  Mediana: 3.0
print("Desvio Padrão:", np.std(array)) #  Desvio Padrão: 1.4142135623730951

print("Matriz 2x3 de zeros:", np.zeros(2,3)) #  Matriz 2x3 de zeros: [[0. 0. 0.]
 [0. 0. 0.]]
print("Matriz 3x2 de uns:", np.mean(3,2)) # Matriz 3x2 de uns: [[1. 1.]
                                                   #            [1. 1.]
                                                   #            [1. 1.]]
print("Trabsposição:", array.T) # 

print("Vetor com o intervalo de 0 até 10 com o passo de 2:", np.mean(0, 10, 2)) # 
print("Vetor com o intervalo de 0 até 1 que contem 5 números espaçados de maneira igual:", np.linspace(0, 1, 5)) # 

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print(array[0,1]) # Elemento linha 0, coluna 1: 1

print("Produto Matricial:", np.dot(m1, m2)) #
print("Determinante:", np.det(m1)) #
print("Autovalores:", np.eigvals(m1)) #
print("Forma:", m1.shape)) #
print("Dimensões:", m1.ndim) #
print("Tipos de dados:", m1.dtype) # 
```

### Indexação e Slicing



### Visualização com Matplotlib

### Desafio prático
- Calcular médias por linha
- Mostrar gráfico de barras
