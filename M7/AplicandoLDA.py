from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = load_iris(as_frame=True)
df = iris.frame

target_names = iris.target_names
df['species'] = target_names[df['target']]

# Separar em X os dados com as características
X = df.iloc[:, :-2].values
# Separar em y os dados com as espécies
y = df.iloc[:, -1].values

# Divide os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Cria o modelo LDA para redução em 2 componentes
lda = LinearDiscriminantAnalysis(n_components=2)

# Treina com os valroes de X_train e y_train
# obtem um novo X (X_train_lda) de dimensionalidade 2 com base no X_train
X_train_lda = lda.fit_transform(X_train, y_train)
# Com o modelo treinado co X_train e y_train
# obtem um novo X (X_test_lda) de dimensionalidade 2, com base no X_test
X_test_lda = lda.transform(X_test)

# Coloca os dados do X_train_lda e y_train em um dataframe para melhor visualização
df_lda_train = pd.DataFrame(X_train_lda, columns=['LDA Component 1','LDA Component 2'])
df_lda_train['species']=y_train

print(df_lda_train.head())

# Plota os valores do X_train_lda
# o sort_values é apenas para que as spécies apareçam em uma determinada ordem
sns.scatterplot(df_lda_train.sort_values(by='species'), x='LDA Component 1', y='LDA Component 2', hue='species')
plt.show()
