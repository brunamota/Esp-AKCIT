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

## Os algoritmos LDA, QDA e RDA

- **LDA (Análise Discriminante Linear)**
  - Traça uma fronteira RETA (linear) para separar as classes.
  - É mais simples e rápido, ideal para problemas onde as classes são bem separadas.
- **QDA (Análise Discriminante Quadrática)**
  - Traça uma fronteira CURVA (quadrática).
  - É mais flexível e consegue resolver problemas mais complexos onde uma linha reta não é suficiente.
- **RDA (Regularizada)**
  - Um híbrido inteligente que busca um equilíbrio entre a simplicidade do LDA e a flexibilidade do QDA.

## Conceitos-Chave de Forma Intuitiva

- Matriz de Covariância
  - É uma medida de "relacionamento" entre as características.
  - Positiva: Quando uma sobe, a outra também tende a subir (ex: altura e peso).
  - Negativa: Quando uma sobe, a outra tende a descer (ex: temperatura e venda de casacos).
- Autovetores e Autovalores
  - O Autovetor é uma direção especial que não muda o sentido, apenas o comprimento.
  - O Autovalor é o quanto essa direção foi esticada ou encolhida.
  - O LDA usa esse conceito para encontrar a melhor direção que separa as classes.
 
## Prática: Dataset Iris

[Código feito na tutoria](https://github.com/brunamota/Esp-AKCIT/tree/main/M7)
