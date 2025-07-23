# Pandas: Manipulação e Análise de Dados Bidimensionais

[Documentação do Pandas](https://pandas.pydata.org/docs/)

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
print(s_lista)
```
- Criando uma Series a partir de um dicionário
``` python
import pandas as pd

so = pd.Series({'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50})
print(s)
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

## Operaçõescom Series
### Indexação e Slicing
  - `[]`: Acessa por rótulo ou posição.
  - `loc`: Acessa um grupo de linhas e colunas por rótulos.
  - `iloc`: Acessa por posição inteira (índice numérico)

``` python
# Indexação 
print("Valor no índice 'b':", s.loc['b'])
print("Valor na posição 2:", s.iloc[2])

# Slicing 
print("Slicing de 'b' até 'd':", s.loc['b':'d']) # Fatiando com rótulos (inclui o final)
print("Slicing da posição 1 até a 3:",s.iloc[1:4]) # Fatiando com posições (exclui o final, como em listas Python)
```

### Atributos e Operações Vetorizadas
``` python
# Atributos úteis
print("Índices da Series:", s.index) # Retorna a lista de indicies a-e
print("Valores da Series:", s.values) # Retorna a lista de valores 10-50
print("Tipo de dado da Series:", s.dtype) # Retorna o tipo dos valores

# Operações aritméticas vetorizadas
print("Soma de mais 5 em cada valor:", s + 5) # Soma escalar
print("Soma dos valores de cada serie:",s + s2) # Soma de series
```

### Filtragem e Métodos Úteis
``` python
# Filtragem
print("Valores > 30:\n", s[s > 30]) # Retorna d 40 e 50

# Verificando valores nulos
print("Valores nulos na serie:", s.isnull()) # Retorna true ou false

# Ordena os valores
print(s.sort_values())

# Remove duplicatas
print(s.drop_duplicates())

# Refazer os índices
print(s.reindex(['g', 'f', 'e', 'd', 'c', 'b', 'a']))

# Ordenando os valores
print(s.sort_values(ascending=False)) # Ordenando os valores em ordem decrescente
```

## Operaçõescom DataFrames
- Acesso a colunas e linhas
- Criação de colunas novas
- Estatísticas básicas
- Seleção de Colunas: Retorna uma Series. 
- `loc`: Acessa dados por rótulos (nomes de índice e coluna).
- `iloc`: Acessa dados por posição inteira (como em listas Python).

``` python
# Acessando colunas e linhas
print(df['Nome'])          # Uma coluna
print(df.iloc[0])          # Primeira linha
print(df.loc[0, 'Nome'])   # Célula específica
print(df.head(2))  # Mostra as duas primeiras linhas
print(df.tail(2))  # Mostra as duas últimas linhas

# Estatísticas
print(df.describe()) # Obter um resumo estatístico das colunas numéricas
print(df.info()) # Obter um resumo conciso, incluindo tipos de dados e valores não nulos

# Nova coluna
df['Bônus'] = df['Salário'] * 0.1  # Cria uma nova coluna "Bônus"
print(df)
```

### Filtros e Agrupamentos

- Filtrar com condições
- Agrupar por colunas
- Ordenar dados
``` python
# Filtro
print(df[df['Salário'] > 4000]) # Filtra as linhas que possuem salário maior que 4000

# Agrupamento
print(df.groupby('Idade')['Salário'].mean()) # Agrupando por 'Idade' para calcular a média de salário

# Ordenação
print(df.sort_values(by='Salário', ascending=False)) # Coloca em ordem decrescente em relação ao salário
```

### Salvando e Carregando com Pickle
- A serialização é o processo de converter um objeto Python (como um DataFrame) em um fluxo de bytes para que possa ser salvo em um arquivo
- Guardar dados como objetos Python
- Evita reprocessar toda vez
- Serialização com Pickle


``` python
import pickle

# Salvando DataFrame
df.to_pickle('dados.pkl')
print("\nDataFrame salvo com sucesso em 'dados.pkl'")

# Lendo de volta
df_do_pickle = pd.read_pickle('dados.pkl')
print("\nDataFrame carregado do arquivo Pickle")
print(df_do_pickle)

```
### Lendo e escrevendo em formato CSV

```Python
# Escrevendo para CSV
df.to_csv('output.csv', index=False)

# Lendo de CSV
df_from_csv = pd.read_csv('output.csv')
print(df_from_csv)
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

[Códigos feitos na tutoria](https://github.com/brunamota/Esp-AKCIT/tree/main/M6/Pandas)
