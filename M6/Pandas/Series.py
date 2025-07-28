import pandas as pd

s = pd.Series({'a': 20, 'b': 20, 'c': 30, 'd': 40, 'e': 50})
s2 = pd.Series({'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50})

# Indexação
s.loc['a']
s.iloc[2]

# Slicing
s.loc['b':'d']
s.iloc[1:4]

# Atributos úteis
s.index
s.values
s.dtype

# Operações aritméticas vetorizadas
s + 5
s + s2

# Filtragem
s[s > 30]

# Verificando valores nulos
s.isnull()

# Ordena os valores
s.sort_values()
s.sort_values(ascending=False)          

# Remove duplicatas
s.drop_duplicates()

# Refazer os índices
s.reindex(['g', 'f', 'e', 'd', 'c', 'b', 'a']
