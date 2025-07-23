# NumPy: Processamento de Dados Estruturados Multidimensionais

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
print("Shape:", vetor.shape) # (3,)
```
  
- Matriz = Array 2D (ex: [[1,2],[3,4]])
``` python
import numpy as np
matriz = np.array([[1,2],[3,4]])
print("Matriz:", matriz)
print("Shape:", matriz.shape) # (2,2)
```

- Tensor = Array 3D+ (ex: imagem colorida)
``` python
import numpy as np
tensor = np.array([[1,2],[3,4],[5,6],[7,8]])
print("Tensor:", matriz)
print("Shape:", tensor.shape) # (2,2,2)
```

