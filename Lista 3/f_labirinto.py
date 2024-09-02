labirinto = []
linha = input().split()

while linha != ["Fim", "do", "labirinto"]:
  labirinto.append(linha)
  linha = input().split()

reliquias_encontradas = []

for i in range(len(labirinto)):
  for j in range(len(labirinto[i])):
    if labirinto[i][j] == "1":
      reliquias_encontradas.append((i, j))

if reliquias_encontradas:
  print("Relíquias encontradas nos seguintes locais:")
  for posicao in reliquias_encontradas:
    linha, coluna = posicao
    print(f'linha: {linha}, coluna: {coluna}')

else:
  print("Nenhuma relíquia encontrada no labirinto.")

'''

Dentro do Labirinto, os semideuses estão em busca de relíquias mágicas perdidas. O labirinto é representado por uma grade retangular, onde cada célula pode conter ou não uma relíquia. Sua missão é criar um programa que, através de listas, explore o labirinto e encontre a localização das relíquias. Portanto, seu programa deve percorrer cada célula do labirinto, identificar a possível presença de relíquias e armazenar, usando listas, as coordenadas de cada relíquia encontrada.

Input

O Labirinto é representado por uma lista (ou um conjunto de listas), onde bits indicam a presença ou não de relíquias. Dessa forma, você receberá strings compostas por uma série de 0’s ou 1’s separados por espaços até que receba a entrada "Fim do labirinto".

"1" indica relíquia presente

"0" indica relíquia ausente.

Por exemplo:

0 0 0 0 1

0 0 0 1 0

0 0 0 0 0

1 0 0 0 0

Fim do labirinto

Output

Ao chegar ao fim do labirinto, você deve imprimir o resultado:

Caso encontre relíquias, imprima as coordenadas de cada uma das relíquias encontradas no formato:
Relíquias encontradas nos seguintes locais:

linha: {valor_linha}, coluna: {valor_coluna}

Caso nenhuma relíquia tenha sido encontrada:
Nenhuma relíquia encontrada no labirinto.

'''
