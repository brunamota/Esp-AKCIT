# Espaço de Características e Funções Discriminantes

## A importância das Características

- **Extração:** Derivar informações úteis dos dados brutos.
- **Seleção:** Escolher um subconjunto das características mais relevantes para evitar "ruído".
- **Dimensionalidade:** Cada característica é uma nova dimensão. Muitas dimensões levam à "Maldição da Dimensionalidade"

## Redução vs. Normalização

- **Normalização:** Ajusta a escala das características para que todas tenham a mesma importância.
- **Redução de Dimensionalidade:** Cria novas características que resumem as originais.

## Funções Discriminantes

- Funções matemáticas que criam fronteiras de decisão para separar as classes no espaço de características.
- Para um novo dado, o algoritmo calcula uma "pontuação" para cada classe. A classe com a maior pontuação vence e o dado é classificado nela.
- Imagine que cada classe de dados vive em um 'bairro' diferente. A função discriminante é a 'fronteira' que o algoritmo desenha para separar esses bairros. Quando um novo dado chega, o algoritmo verifica de que lado da fronteira ele caiu para decidir a qual classe pertence.

<div align="center">
<img width="500" height="250" alt="image" src="https://github.com/user-attachments/assets/527af02b-31e9-49b4-85f7-27716bf3f711" />
</div>

### Classificação: binária e multiclasse.
- A classificação binária, como o próprio nome diz, refere-se apenas a duas classes, como por exemplo os casos ilustrados na figura abaixo e a direita. Nesse caso se resumem a uma única função (reta em verde) que separa as duas classes (O de X). Exemplos de métodos de classificação binária incluem Regressão Logística e SVM.
- Em problemas de classificação com mais de duas classes, como classificação de imagens em diferentes categorias, são requeridas múltiplas funções discriminantes , uma para cada par de classes, como o ilustrado abaixo (Figura 24) e a direita. A reta vermelha separa o X dos quadrados e triângulos. A reta em verde separa os triângulos dos X e quadrados, por fim, a reta em azul separa os quadrados dos triângulos e X. Alguns exemplos de métodos multiclasse são a LDA e QDA.
