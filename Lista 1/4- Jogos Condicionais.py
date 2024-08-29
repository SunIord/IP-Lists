nv = input() # Nome da vítima
na = input() # Nome do antagonista
ta = input() # Tipo de armadilha
t = int(input()) # Tempo
t = float(t/60)

if (na == "John Kramer") and (ta == "Armadilha de urso reversa") and  (t>=5):
  print ("Com tempo de sobra, " + nv + " consegue retirar a armadilha de sua cabeça, sobrevivendo com sucesso ao jogo de Jigsaw.")

elif (na == "John Kramer") and (ta == "Armadilha de urso reversa") and (2.5<=t<5):
  print ("À beira de perder a cabeça, e desafiando as expectativas de seu algoz, " + nv + " remove a armadilha de urso e por pouco escapa de um destino cruel.")

elif (na == "John Kramer") and (ta == "Armadilha de urso reversa") and (t<2.5):
  print ("Game Over...")

elif (na == "John Kramer") and (ta == "Tanque de agua") and  (t>=4):
  print (nv + " usa suas práticas de respiração na natação a seu favor, vencendo o jogo de Jigsaw sem perder muito fôlego.")

elif (na == "John Kramer") and (ta == "Tanque de agua") and (2<=t<4):
  print (nv + " passa por maus bocados, mas vira o jogo e consegue evitar, no limite, seu afogamento dentro da armadilha.")

elif (na == "John Kramer") and (ta == "Tanque de agua") and (t<2):
  print ("Game Over...")

elif (na == "Amanda Young") and (ta == "Caixa de laminas") and (t>=10):
  print ("Apenas com ferimentos leves, " + nv + " se liberta rapidamente das perigosas lâminas da armadilha montada pela discípula de Jigsaw.")

elif (na == "Amanda Young") and (ta == "Caixa de laminas") and (6<=t<10):
  print ("Por um triz, " + nv + " sobrevive ao jogo de Amanda, mas com lesões profundas em suas mãos e braços.")

elif (na == "Amanda Young") and (ta == "Caixa de laminas") and (t<6):
  print ("Game Over...")

elif (na == "Amanda Young") and (ta == "Asas de anjo") and (t>=3):
  print ("Com surpreendente facilidade, " + nv + " alcança a chave da armadilha e vence o desafio da aprendiz de Jigsaw.")

elif (na == "Amanda Young") and (ta == "Asas de anjo") and (1.5<=t<3):
  print (nv + " desafia as possibilidades e o cruel anseio de sua algoz, escapando da armadilha com poucas queimaduras e arranhões.")

elif (na == "Amanda Young") and (ta == "Asas de anjo") and (t<1.5):
  print ("Game Over...")

else:
  print (" ")
  
'''

Cansados de observar por tanto tempo suas vítimas durante a execução de suas terríveis armadilhas, a dupla de antagonistas da saga ‘Jogos Mortais’, John Kramer e Amanda Young, resolve buscar um habilidoso programador para ajudá-los a automatizar seus desafios de sobrevivência.

Capturado pela dupla de vilões, você, um estudante CIn, acorda abruptamente em uma sala com pouca luminosidade, deparando-se com o clássico tocador de fitas de ‘Jigsaw’, além de um potente computador a sua frente. Como é de se esperar dos antagonistas, o tocador contém uma única fita, especialmente para você.

Tocando a fita, você ouve minuciosamente as instruções do seu jogo e entende que sua tarefa será criar um programa bastante simples. A funcionalidade do programa se resume em verificar determinadas condições, dada uma entrada que descreve as circunstâncias do desafio mortal da próxima vítima do Jigsaw, e imprimir como saída uma única linha de texto que indica o destino da vítima.

Descrição do problema
Você deverá desenvolver um código para um programa que recebe como entrada quatro informações:

Nome da vítima do jogo;
Nome do vilão responsável pelo desafio;
Tipo de armadilha executada; e
Tempo total para escapar da armadilha, em segundos.
Em relação aos vilões e tipos de armadilha, sabe-se que existem apenas dois possíveis vilões responsáveis pelo jogo: John Kramer e Amanda Young. Enquanto Kramer é o responsável pela Armadilha de urso reversa e o Tanque de agua, sua aprendiz é a criadora das letais Asas de anjo e Caixa de laminas.

Observação: Cada armadilha é de uso exclusivo do vilão associado a ela, ou seja, entradas que misturam a participação de um certo vilão com a armadilha do outro não serão reconhecidas e o programa encerrará sem realizar nenhuma ação, o mesmo deverá acontecer caso você receba nomes de vilões e armadilhas que não especificados previamente.

Além disso, deve ser considerado que as condições de sobrevivência para uma pessoa comum em cada tipo de armadilha dependem diretamente do tempo disponível. Determinados intervalos de tempo definem o destino da vítima, ou seja, se ela sobreviverá (com facilidade ou dificuldade), ou não, de acordo com as informações a seguir:

John Kramer:
Armadilha de urso reversa:
Sobrevive facilmente: tempo ≥ 5 minutos
Sobrevive com dificuldades: 2,5 minutos ≤ tempo < 5 minutos
Não sobrevive: tempo < 2,5 minutos
Tanque de agua:
Sobrevive facilmente: tempo ≥ 4 minutos
Sobrevive com dificuldades: 2 minutos ≤ tempo < 4 minutos
Não sobrevive: tempo < 2 minutos
Amanda Young:
Caixa de laminas:
Sobrevive facilmente: tempo ≥ 10 minutos
Sobrevive com dificuldades: 6 minutos ≤ tempo < 10 minutos
Não sobrevive: tempo < 6 minutos
Asas de anjo:
Sobrevive facilmente: tempo ≥ 3 minutos
Sobrevive com dificuldades: 1,5 minuto ≤ tempo < 3 minutos
Não sobrevive: tempo < 1,5 minuto
Input

Você deverá receber apenas 4 inputs, sendo eles o nome da vítima do jogo, o nome do antagonista responsável pelo jogo, o tipo de armadilha e, por último, um inteiro que representa o tempo total, em segundos, para que a vítima escape da armadilha:

nome_vitima

nome_antagonista

tipo_armadilha

tempo

OBS.1: Desconsidere a acentuação das palavras que dão nome às armadilhas - tanto na entrada, como na verificação condicional.

Output

Para Armadilha de urso reversa:
Se sobrevive facilmente, imprima:
“Com tempo de sobra, {nome_vitima} consegue retirar a armadilha de sua cabeça, sobrevivendo com sucesso ao jogo de Jigsaw.”

Se sobrevive com dificuldade, imprima:
“À beira de perder a cabeça, e desafiando as expectativas de seu algoz, {nome_vitima} remove a armadilha de urso e por pouco escapa de um destino cruel.”

Para Tanque de agua:
Se sobrevive facilmente, imprima:
“{nome_vitima} usa suas práticas de respiração na natação a seu favor, vencendo o jogo de Jigsaw sem perder muito fôlego.”

Se sobrevive com dificuldade, imprima:
“{nome_vitima} passa por maus bocados, mas vira o jogo e consegue evitar, no limite, seu afogamento dentro da armadilha.”

Para Caixa de laminas:
Se sobrevive facilmente, imprima:
“Apenas com ferimentos leves, {nome_vitima} se liberta rapidamente das perigosas lâminas da armadilha montada pela discípula de Jigsaw.”

Se sobrevive com dificuldade, imprima:
“Por um triz, {nome_vitima} sobrevive ao jogo de Amanda, mas com lesões profundas em suas mãos e braços.”

Para Asas de anjo:
Se sobrevive facilmente, imprima:
“Com surpreendente facilidade, {nome_vitima} alcança a chave da armadilha e vence o desafio da aprendiz de Jigsaw.”

Se sobrevive com dificuldade, imprima:
“{nome_vitima} desafia as possibilidades e o cruel anseio de sua algoz, escapando da armadilha com poucas queimaduras e arranhões.”

Caso a vítima do jogo não sobreviva, em qualquer uma das armadilhas, uma única linha de saída deverá ser impressa antes do fim da execução do programa:
“Game Over...”

'''
