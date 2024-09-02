coluna = int(input())
linha = int(input())
matriz = []

for i in range(coluna):
  andar = [int(input()) for i in range(linha)]
  matriz.append(andar)

for j in range(coluna):
  linha_atual = [str(matriz[j][k]) for k in range(linha)]
  print(" ".join(linha_atual))
print()

numero_chale = 0
quantidade_campistas = 0

for l in range(coluna):
  soma_atual = sum(matriz[l])
  if soma_atual > quantidade_campistas:
    quantidade_campistas = soma_atual
    numero_chale = l + 1 
print(f"O chalé {numero_chale} foi o que mais recebeu semi-deuses, tendo um acréscimo de {quantidade_campistas} novos campistas!") 

'''

Percy acabou de chegar no Acampamento Meio-Sangue e, junto a ele, vieram diversos outros semi-deuses que precisam de um local pra dormir. Como existem diversos chalés, e cada campista deve ser direcionado a um específico, Quíron, um dos responsáveis pela organização do acampamento, pediu sua ajuda para separar os novos integrantes pelos diferentes dormitórios.

Vale ressaltar que cada chalé tem sua decoração específica, mas o número de andares por dormitório é padronizado, em que cada campista pode ser colocado em qualquer andar, de qualquer chalé.

Input

Os dormitórios serão representados por uma matriz de tamanho M x N, em que M representa o número de chalés disponíveis para o recebimento de campistas e N representa o número de andares dos chalés.

Inicialmente, você vai receber o inteiro positivo M, que será usado como número de linhas da matriz.

M

Em seguida, você vai receber um inteiro positivo N que será utilizado como o número de colunas da matriz.

N

Depois disso, para cada um dos M chalés, você vai receber, para cada um dos N andares, o número de semi-deuses que vão passar a habitar esse mesmo andar.

campistas_chale1_andar1

campistas_chale1_andar2

...

campistas_chale1_andarN

...

...

campistas_chaleM_andar1

campistas_chaleM_andar2

...

campistas_chaleM_andarN

Perceba, você vai receber um total de M vezes N entradas, pois você estará recebendo N inputs para cada um dos M chalés.

Dica: como matrizes são listas dentro de listas, o primeiro elemento da primeira lista contida dentro da matriz poderia ser acessado da seguinte forma: matriz[0][0]

Output

O output será uma matriz representando quantos campistas foram recebidos em cada andar de cada chalé:


 Informação do último andar de cada chalé
          ↓
x1 x2 ... xM     <- Informações do Chalé 1

y1 y2 ... yM

z1 z2 ... zM     <- Informações do Chalé N
É obrigatório o uso de matrizes na resolução (listas dentro de listas).

Além disso, deve ser printado uma frase falando qual o chalé que mais recebeu novos campistas:

"O chalé {numero_chale} foi o que mais recebeu semi-deuses, tendo um acréscimo de {quantidade_campistas} novos campistas!"

Sendo numero_chale, o número do chalé com maior quantidade de novos integrantes e que começa a contagem a partir do número 1, como no exemplo da matriz acima, apesar dos índices começarem em 0. E quantidade_campistas a quantidade total de novos semi-deuses naquele chalé, considerando todos os seus andares.

OBS: Entre a matriz e a frase que indica o chalé que mais recebeu campistas deve haver uma linha vazia.

OBS: Cada elemento da matriz deve ser separado do outro por um espaço. O último elemento de uma linha não deve ter espaço após ele.

'''
