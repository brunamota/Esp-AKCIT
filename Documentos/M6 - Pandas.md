# Pandas: Manipulação e Análise de Dados Bidimensionais

[Documentação do Pandas](https://numpy-org.translate.goog/devdocs/user/absolute_beginners.html?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc)

## Conceitos

- Biblioteca para manipular dados tabulares (como planilhas)
- Projetadas para trabalhar com dados "relacionais" ou "rotulados" de forma intuitiva.
- Principais estruturas:
  - `Series`: Uma estrutura **unidimensional**, semelhante a um array, que pode armazenar qualquer tipo de dado (inteiros, strings, etc.). Cada elemento possui um rótulo associado, chamado de índice.
  - `DataFrame`: Uma estrutura **bidimensional**, análoga a uma tabela de banco de dados ou uma planilha. Ela é composta por linhas e colunas, onde cada coluna é, na verdade, uma Series.
  
## Exemplos práticos

### Verificar se o Pandas e o Matplotlib estão instalados
- Instalar pelo CMD ou pela própria IDE utilizada

``` cmd
pip install pandas matplotlib
```
- Verificar se a instalação foi realizada
``` python
import pandas as pd
print("Versão do Pandas:",pd.__version__)
```
### Series e Dataframes

- Criando uma Series a partir de uma lista
``` python
import pandas as pd

s_lista = pd.Series([1, 3, 5, np.nan, 6, 8])
print("--- Series a partir de uma lista ---")
print(s_lista)
```
- Criando uma Series a partir de um dicionário
``` python
import pandas as pd

s_dicionario = pd.Series({'a': 10, 'b': 20, 'c': 30})
print(s_dicionario)
```
- Criando um DataFrame
``` python
import pandas as pd

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 35, 30],
    'Salário': [3000, 5000, 4500]
}
df = pd.DataFrame(dados)
print(df)
```

### Operações Básicas com DataFrames
- Acesso a colunas e linhas
- Criação de colunas novas
- Estatísticas básicas

``` python
import pandas as pd

# Acessando colunas e linhas
print(df['Nome'])          # Uma coluna
print(df.iloc[0])          # Primeira linha
print(df.loc[0, 'Nome'])   # Célula específica

# Estatísticas
print(df.describe())

# Nova coluna: bônus
df['Bônus'] = df['Salário'] * 0.1
print(df)
```

### Filtros e Agrupamentos

- Filtrar com condições
- Agrupar por colunas
- Ordenar dados
``` python
import pandas as pd

# Filtro
print(df[df['Salário'] > 4000])

# Agrupamento
print(df.groupby('Idade')['Salário'].mean())

# Ordenação
print(df.sort_values(by='Salário', ascending=False))
```

### Salvando e Carregando com Pickle
- Guardar dados como objetos Python
- Evita reprocessar toda vez

``` python
import pandas as pd
import pickle

# Salvando DataFrame
with open('dados.pkl', 'wb') as f:
    pickle.dump(df, f)

# Lendo de volta
with open('dados.pkl', 'rb') as f:
    df2 = pickle.load(f)

print(df2)
```

### Visualização com Matplotlib

``` python
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
```

## Desafio com Dataset Real
- Trabalhar com um dataset real
- Explorar agrupamento e média

## Tutoria 11 - 23/07/2025

[Códigos feitos na tutoria](https://github.com/brunamota/Esp-AKCIT/tree/main/M6/NumPy)
