import pandas as pd
import pickle
import matplotlib.pyplot as plt

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'João'],
    'Idade': [23, 35, 30, 30],
    'Salário': [3000, 5000, 4500, 4000]
}

df = pd.DataFrame(dados)


# Acessando colunas e linhas
df['Nome']
df.iloc[0]
df.loc[0, 'Nome']
df.head(2)
df.tail(2)

# Estatísticas
df.describe()
df.info()

# Nova coluna
df['Bônus'] = df['Salário'] * 0.1

# Filtro
df[(df['Salário'] > 3500) & (df['Idade'] > 30)]
df['Idade'].mode() #filtra o valor que aparece mais dentro da coluna Idade

# Agrupamento
df.groupby('Idade')['Salário'].mean()

# Ordenação
df.sort_values(by = 'Salário', ascending = False)

# Salvando DataFrame
df.to_pickle('dados.pkl')
print("\nDataFrame salvo com sucesso em 'dados.pkl'")

# Lendo de volta
df_do_pickle = pd.read_pickle('dados.pkl')
print("\nDataFrame carregado do arquivo Pickle")
print(df_do_pickle)

df.to_csv('output.csv', index=False)

# Lendo de CSV
df_from_csv = pd.read_csv('output.csv')
print(df_from_csv)

# Gráfico de barras
df.plot(kind='bar', x='Nome', y='Salário', legend=False)
plt.title("Salário por Pessoa")
plt.ylabel("Salário")
plt.grid(True)
plt.show()
