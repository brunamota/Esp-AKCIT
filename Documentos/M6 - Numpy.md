# NumPy: Processamento de Dados Estruturados Multidimensionais


[Documentação do NumPy](https://numpy-org.translate.goog/devdocs/user/absolute_beginners.html?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc)

## Conceitos

- Biblioteca fundamental para computação científica com Python
- Suporte para arrays n-dimensionais e operações vetoriais rápidas
- Base para outras bibliotecas: Pandas, SciPy, Scikit-learn

## Exemplos práticos

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

- Criando um Vetor (Array 1D)
``` python
import numpy as np
vetor = np.array([1,2,3])
print("Vetor:", vetor)
```
  
- Criando uma Matriz (Array 2D)
``` python
import numpy as np
matriz = np.array([[1,2],[3,4]])
print("Matriz:", matriz)
```

- Criando um Tensor (Array 3D+)
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
                              #           [14 15 16]]

print("Subtração:", matriz - 1) #  Subtração: [[0 1 2]
                                #              [3 4 5]]

print("Multiplicação:", matriz * 2) #  Multiplicação: [[ 2  4  6]
                                    #                  [ 8 10 12]]

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
- Função arrange
  - `início` é o primeiro valor da sequência.
  - `fim` é o valor final (inclusivo por padrão).
  - `passo` é a distância entre cada número na sequência.
  > np.arange(`início`,`fim`, `passo`)
- Função linspace gerar uma sequência de números igualmente espaçados
  - `início` é o primeiro valor da sequência.
  - `fim` é o valor final do intervalo.
  - `num` é o número total de elementos no array.
  > np.linspace(`início`,`fim`, `num`)

``` python
import numpy as np

array = np.array([1, 2, 3, 4, 5])

print("Média:", np.mean(array)) #  Média: 3.0
print("Mediana:", np.median(array)) #  Mediana: 3.0
print("Desvio Padrão:", np.std(array)) #  Desvio Padrão: 1.4142135623730951

print("Matriz 2x3 de zeros:", np.zeros((2,3))) #  Matriz 2x3 de zeros: [[0. 0. 0.]
                                               #                        [0. 0. 0.]]
print("Matriz 3x2 de uns:", np.mean((3,2))) # Matriz 3x2 de uns: [[1. 1.]
                                            #                     [1. 1.]
                                            #                     [1. 1.]]

print("Vetor com o intervalo de 0 até 10 com o passo de 2:", np.arange(0, 10, 2))
# Vetor com o intervalo de 0 até 10 com o passo de 2: [0 2 4 6 8]
print("Vetor com o intervalo de 0 até 1 que contem 5 números espaçados de maneira igual:", np.linspace(0, 1, 5))
# Vetor com o intervalo de 0 até 1 que contem 5 números espaçados de maneira igual: [0.   0.25 0.5  0.75 1.  ]

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print(m1[0,1]) # Elemento linha 0, coluna 1: 1

print("Produto Matricial:", np.dot(m1, m2)) # [[19 22]
                                            #  [43 50]]
print("Determinante:", np.linalg.det(m1)) # Determinante: -2.0000000000000004
print("Autovalores:", np.linalg.eigvals(m1)) # [-0.37228132  5.37228132]
print("Forma:", m1.shape) # Forma: (2, 2)
print("Dimensões:", m1.ndim) # Dimensões: 2
print("Tipos de dados:", m1.dtype) # Tipos de dados: int64
```

### Indexação e Slicing
- Técnicas para acessar e manipular partes do array
- Slicing é uma técnica de "fatiamento" de um array.
  - `início`: Determina onde será iniciado. Quando o valor de início é omitido, o fatiamento começa do primeiro elemento do array (índice 0).
  - `fim`: Determina onde será encerrado.Quando o valor de fim é omitido, o fatiamento vai até o último elemento do array.
  - `passo`: Um passo de significa que o código selecionará um elemento a cada x posições, começando pelo `inicio`.
  > array[`início`:`fim`]
  
  > array[`início`:`fim`: `passo`]
- Função where funciona com um "se-então-senão" que se aplica a um array inteiro de uma só vez.
  > where(`condição`, `valor_se_verdadeiro`, `valor_se_falso`)

``` python
import numpy as np

array = np.array([10, 20, 30, 40, 50])

print("Primeiros dois elementos:", array[:2]) # Primeiros dois elementos: [10 20]

print("Elementos entre a 2ª e a 4ª posição do array: ", array[1:4]) # Elementos entre a 2ª e a 4ª posição do array: [20 30 40]

print("Elementos selecionados com step de 2:", array[1:8:2]) # Elementos selecionados com step de 2: [20 40]

print("Elemento no índice 1:", array[1]) # Elemento no índice 1: 20

print("Escolhe de valores maiores que 30:", array[array > 30]) # Escolhe de valores maiores que 30: [40 50]

array[0] = 0
print("Array modificado:", array) # Array modificado: [ 0 20 30 40 50]

indices = [1, 3, 4]
print("Elementos selecionados:", array[indices]) # Elementos selecionados: [20 40 50]

print("Caso o número do array for maior que 25, substituir por 1, caso for menor substituir por 0", np.where(array > 25, 1, 0))
# Caso o número do array for maior que 25, substituir por 1, caso for menor substituir por 0 [0 0 0 1 1]

h = np.array([1, 2, 3])
i = np.array([[0], [1], [2]])

j = h + i
print("Broadcasting entre diferentes tamanhos:\n", j) # Broadcasting entre diferentes tamanhos: [[1 2 3]
                                                      #                                          [2 3 4]
                                                      #                                          [3 4 5]]
```

### Visualização com Matplotlib
- Plotagem
``` python
import numpy as np
import matplotlib.pyplot as plt

# Dados
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plotando
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)')
plt.title('Gráfico de Linha Simples')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()
```
- Histograma
``` python
# Dados aleatórios
data = np.random.normal(size=1000)

# Histograma
plt.figure(figsize=(8, 4))
plt.hist(data, bins=30, alpha=0.75, color='blue', edgecolor='black')
plt.title('Histograma de Dados Aleatórios')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()
```

### Desafio prático
- Calcular médias por linha
- Mostrar gráfico de barras

``` python
import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(5, 5)
print("Médias por linha:", np.mean(data, axis=1))
print("Médias por coluna:", np.mean(data, axis=0))

plt.bar(range(5), np.mean(data, axis=1))
plt.title("Média por Linha")
plt.show()
```

## Tutoria 10 - 16/07/2025

[Códigos feitos na tutoria](https://github.com/brunamota/Esp-AKCIT/tree/main/M6/NumPy)
