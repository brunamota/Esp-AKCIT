from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega o conjunto de dados Iris, incluindo um dataframe
# Essa função retorna um dicionário, com vários itens
iris = load_iris(as_frame=True)

# Guarda o item 'frame' do dicionario como df
df = iris.frame

# Mostra os primeiros dados do dataset
print(df.head())
# Note que a coluna target está em função de valores numéricos
# Para melhor entender, será adicionado uma coluna que converte esse número para a espécie da flor


# Acessando os nomes das espécies
# Segundo a documentação do sklearn, os valores dos rótulos estão contidos no dicionário do load_iris()
# Guarda o item 'target_names' do dicionario como df
target_names = iris.target_names

# Adicionando uma nova coluna com os nomes das espécies
df['species'] = target_names[df['target']]

# Visualizando o DataFrame
# Observe a última coluna com o nome das espécies
#print(df.head())

sns.pairplot(df.drop(columns='target'), hue='species', markers=["o", "s", "D"])
plt.show()

