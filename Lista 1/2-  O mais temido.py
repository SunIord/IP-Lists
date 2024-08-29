F = input() #Frase
C = input() #Características

P = "Bem-vindos ao Hotel Transilvânia!"
if F == "Parou filhotada, assim vocês vão deixar todo mundo maluco." and (C == "Uivar" or C == "Pelos" or C == "Caninos"):
  print (P)
  print ("Wayne, seu cachorrão.")
elif F == "Veio de novo pelo correio, deixa de ser pão duro." and (C == "Desmontável" or C == "Parafusos" or C == "Morto-vivo"):
  print (P)
  print ("Frank, assim vai acabar perdendo a cabeça.")
elif F == "Quem me beliscou?" and C == "Transparente":
  print (P)
  print ("Griffin, prazer em vê-lo.")
elif F == "Tô na área galera!" and (C == "Enfaixado" or C == "Morto-vivo"):
  print (P)
  print ("Murray, sempre soltando areia.")
else:
  print ("UM HUMANO! Quem é você, e como você achou esse lugar?")
  
'''

Depois de perder sua esposa, ele jurou proteger sua filha das aberrações que destruíram sua família. Para isso, construiu um hotel localizado na Transilvânia, Romênia, cujo principal objetivo é proporcionar aos hóspedes uma estadia segura, livre dessas criaturas.

raio atinge o castelo

Sua missão é garantir que todos os monstros consigam finalmente descansar e, ao mesmo tempo, proteger-se do mais temido de todos: OS HUMANOS!!!

drácula gritando

Para isso, será preciso reconhecer o monstro e permitir ou não a entrada dele.

Input

Você receberá duas entradas:

A primeira entrada será exatamente alguma das frases a seguir que remetem a cada monstro

“Parou filhotada, assim vocês vão deixar todo mundo maluco.” - Lobisomem

“Veio de novo pelo correio, deixa de ser pão duro.” - Frankenstein

“Quem me beliscou?” - Homem Invisível

“Tô na área galera!” - Múmia

E, em seguida, somente uma das possíveis características dele:

“Uivar” / “Pelos” / “Caninos” - Lobisomem

“Desmontável” / “Parafusos” / “Morto-vivo” - Frankenstein

“Transparente” - Homem Invisível

“Enfaixado” / “Morto-vivo” - Múmia

Qualquer combinação de entradas que não seja a frase do monstro juntamente com alguma das suas respectivas características determinará que a criatura é um humano.

Output

Se for liberada a entrada, deverá aparecer primeiramente a seguinte frase:

“Bem-vindos ao Hotel Transilvânia!”

Seguido da frase do respectivo monstro:

“Wayne, seu cachorrão.” -  Lobisomem

“Frank, assim vai acabar perdendo a cabeça.” - Frankenstein

“Griffin, prazer em vê-lo.” - Homem Invisível

“Murray, sempre soltando areia.” - Múmia

Se negada a entrada:

“UM HUMANO! Quem é você, e como você achou esse lugar?”

'''
