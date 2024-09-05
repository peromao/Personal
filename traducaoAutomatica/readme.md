# Resposta 1
Ao observar o gráfico, podemos perceber que o tamanho do vocabulário tem um crescimento rápido no início junto com o aumento de valores de exemplo, até um momento que se cria um plato.

O cresimento acontece porque quando temos poucas frases de exemplo, realmente não vamos ter uma variedade em palavras. Ao aumentar cada vez mais o número de exemplo, mais palavras ainda desconhecidas vão aparecendo. Entretanto, a quantidade de palavras novas vai diminuindo conforme temos mais exemplos, porque muitas palavras vão se repetir.

# Resposta 2
Para esses casos, se usa uma abordagem com base em caracteres ou em morfemas. A maioria dos tokenizers em japonês usam uma estrutura de grafo com possíveis substrings a partir do texto de entrada e um custo associado a elas. Depois se usa o algoritmo de viterbi para calcular qual a sequência de estados escondidos até o nó n que gera o menor custo.

Referência: https://towardsdatascience.com/how-japanese-tokenizers-work-87ab6b256984
