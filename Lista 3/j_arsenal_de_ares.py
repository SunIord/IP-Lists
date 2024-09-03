lista_arsenal = []
arsenal = input()
lista_arsenal = arsenal.split(" - ")
index = len(lista_arsenal) // 2
objeto = []
objeto_clarisse = int(input())

for i in range(objeto_clarisse):
  giro = input()
  escolha = input()
  direcao = giro[-1]
  numero_rotacoes = int(giro[:-1])
  
  if direcao == ">":
    index = (index + numero_rotacoes) % len(lista_arsenal)
  elif direcao == "<":
    index = (index - numero_rotacoes) % len(lista_arsenal)
  
  if index < 0:
    index += len(lista_arsenal)

  objeto_exibido = lista_arsenal[index]

  if objeto_exibido in objeto:
    print(f"{objeto_exibido} já está na mochila. Não seja gananciosa, ou acabará como Midas!")
  else:
    if escolha == "Adicionar":
      objeto.append(objeto_exibido)
      print(f"{objeto_exibido} adicionado a mochila!")
    elif escolha == "Ignorar":
      print(f"{objeto_exibido} não vai ser tão útil assim!")

if len(objeto) == 0 or objeto == [" "]:
  print("Não achei nada útil no arsenal. Acho que vamos precisar ser menos violentos dessa vez…")
else:
  print("Com ", end="")
  for j in objeto:
      print(j, end=', ')
  print("seremos imbatíveis na caça à bandeira!")
  
'''

A cabana com os filhos de Ares, o deus da guerra, se prepara para uma partida de caça à bandeira, e então mandaram a líder da equipe, Clarisse, escolher os equipamentos necessários para a partida no grande arsenal de Ares.

Como um deus bom de guerra, Ares tem um sistema para organizar seus artefatos ilegais de batalha. Esse sistema funciona como um expositor giratório que gira para a esquerda e para a direita, sempre mostrando um objeto de cada vez.

Contudo, depois de milhares de anos funcionando, Clarisse notou que a máquina que rotacionava o arsenal havia pifado. Então, ela pediu a você, aluno do CIn, para reprogramar a máquina, a fim de que ela e sua cabana pudessem vencer a caça à bandeira.

Input

Primeiramente, você receberá uma lista com todos os objetos presentes no arsenal rotatório separados por ‘ - ’. No caso do número de objetos ser ímpar, o objeto que está exatamente no meio será o objeto sendo mostrado à Clarisse, mas se o número de objetos for par, o objeto à direita mais próximo do meio será o objeto mostrado. Por exemplo, em um caso em que você tivesse:

“Machado Taurico - Anel do Poder - Contracorrente - Faca da Annabeth”.

Contracorrente seria o item mostrado à Clarisse.

Após isso, você receberá um número inteiro N, que dirá quantos objetos Clarisse vai querer analisar no arsenal giratório.

"N"

Em seguida você receberá N entradas, que dirão as informações sobre como Clarisse irá rotacionar o arsenal, nos seguintes formatos.

“x<”

ou

“x>”

Em que x (>=0) será a quantidade de posições que a base giratória irá rodar, exibindo um objeto diferente a cada posição movida e a direção em que a seta está apontada (‘<’ é esquerda e ‘>’ é direita) será a direção para a qual está se movendo.

Obs.: Você deve simular o movimento circular do arsenal, logo, considere o 1° elemento como o sucessor do último e o último como o antecessor do 1°.

Dica - clique aqui!!

Após cada entrada com o par de informações da rotação do arsenal, você receberá uma string com a decisão de Clarisse em relação ao objeto mostrado. Essa string poderá ser:

“Adicionar”

ou

“Ignorar”

A string será “Ignorar” se ela não se interessar pelo objeto e será “Adicionar” se ela quiser adicionar o objeto à sua mochila.

Output

Após cada uma das N entradas dizendo os movimentos que o arsenal fará, a direção, e a string com a decisão de Clarisse em relação ao objeto mostrado. Você deverá imprimir o seguinte:

Caso o objeto já tenha sido adicionado à mochila anteriormente, sendo a decisão "Adicionar" ou "Ignorar", você deve apenas imprimir:

“{objeto} já está na mochila. Não seja gananciosa, ou acabará como Midas!”

Caso o objeto não esteja na mochila e você receber “Adicionar”, o objeto mostrado será adicionado à mochila de Clarisse, e então você deve imprimir:

“{objeto} adicionado a mochila!”

Contudo, se o objeto não estiver na mochila e você receber “Ignorar”, você deve imprimir:

“{objeto} não vai ser tão útil assim!”

Após receber todas as entradas, se a mochila de Clarisse tiver algum objeto, você deve imprimir todos os objetos na ordem em que foram adicionados unidos por vírgula e um espaço (‘, ’) e no seguinte formato:

“Com {objeto1}, {objeto2}, …, {objetoN}, seremos imbatíveis na caça à bandeira!”

Caso a mochila de Clarisse esteja vazia ao fim das entradas, você deve imprimir:

“Não achei nada útil no arsenal. Acho que vamos precisar ser menos violentos dessa vez…”

'''
