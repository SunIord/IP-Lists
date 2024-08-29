local_do_teste = str(input())
hora_do_teste = int(input())
resposta = str(input())
if (local_do_teste == "Salão") and (resposta == "Sim, Pearl! Siga seus sonhos!"):
  H = hora_do_teste - 2
  print ("Em direção ao salão!")
  print ("Pra chegar na hora, vou ter que sair de " + str(H) + " horas.")
  print ("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
elif (local_do_teste == "Salão") and (resposta == "Não. Você ficará na fazenda.") :
  H = hora_do_teste - 2
  print ("Em direção ao salão!")
  print ("Pra chegar na hora, vou ter que sair de " + str(H) + " horas.")
  print ("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")
elif (local_do_teste == "Praça") and (resposta == "Sim, Pearl! Siga seus sonhos!"):
  H = hora_do_teste - 2
  print ("Para a praça eu vou!")
  print ("Pra chegar na hora, vou ter que sair de " + str(H) + " horas.")
  print ("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
elif (local_do_teste == "Praça") and (resposta == "Não. Você ficará na fazenda."):
  H = hora_do_teste - 2
  print ("Para a praça eu vou!")
  print ("Pra chegar na hora, vou ter que sair de " + str(H) + " horas.")
  print ("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")
elif (local_do_teste == "Centro da cidade") and (resposta == "Sim, Pearl! Siga seus sonhos!"):
  H = hora_do_teste - 1
  print ("Faz tempo que não visito o centro, mal posso esperar!")
  print ("Pra chegar na hora, vou ter que sair de " + str(H) + " horas.")
  print ("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
elif (local_do_teste == "Centro da cidade") and (resposta == "Não. Você ficará na fazenda.") :
  H = hora_do_teste - 1
  print ("Faz tempo que não visito o centro, mal posso esperar!")
  print ("Pra chegar na hora, vou ter que sair de " + str(H) + " horas.")
  print ("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")
  
'''

Após passar toda a sua vida trabalhando na fazenda de seus pais, Pearl sonha em sair e virar uma estrela de cinema. Porém, passa a maioria do seu tempo cuidando de seu pai enfermo, e sua mãe desaprova sua ambição. Um dia, sua cunhada vem lhe visitar na fazenda, e a conta sobre um espetáculo organizado pela igreja local que vai viajar por várias cidades. Ela descobre também que estavam procurando uma jovem para o papel principal, e que iria haver uma audição para o papel em breve. Pearl vê na peça sua oportunidade de finalmente ter a vida de sucesso que sempre sonhou!

Para conseguir ir pra audição, Pearl precisará saber o horário e local do teste, para planejar que horas irá sair de casa. Em seguida, ela deverá falar com sua mãe para lhe convencer a deixar ela ir para o teste.

Input

A entrada inicial consiste no local da audição:

local_do_teste

O local será um dos 3 locais a seguir:

Salão

Praça

Centro da cidade

Em seguida, você receberá o horário que começa o teste. Esse valor é inteiro, e varia de 8 ate 12 (horas):

hora_do_teste

Sua terceira entrada será a resposta da mãe após Pearl perguntar se pode ir para o teste.

resposta

As possíveis respostas são:

Sim, Pearl! Siga seus sonhos!

Não. Você ficará na fazenda.

Output

Primeiramente, após receber o local do teste, a saída deverá seguir os seguintes critérios:

Caso o local da audição seja "Salão", a saída deverá ser:

"Em direção ao salão!"

Se for "Praça", a saída deverá ser:

"Para a praça eu vou!"

Caso seja "Centro da cidade", a saída deverá ser:

"Faz tempo que não visito o centro, mal posso esperar!"

Em seguida, ao receber o horário do teste, você precisará calcular que horas Pearl terá que sair de casa para chegar à tempo. A hora de saída depende também do local onde a audição irá ocorrer.

Sendo assim, caso o local informado tenha sido "Salão" ou "Praça", Pearl precisará sair de casa :

2 horas antes do horário do teste.
Caso tenha sido "Centro da cidade", basta que ela saia :

1 hora antes do horário do teste.
Para calcular que horas Pearl precisará sair, basta utilizar a formula:

hora_do_teste - (quantas horas antes ela precisa sair)

A saída deverá ser:

"Pra chegar na hora, vou ter que sair de {hora que Pearl deve sair de casa} horas."

Após receber a resposta de sua mãe, caso ela diga "Sim, Pearl! Siga seus sonhos!", a saída deverá ser:

"Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!"

Entretanto, caso sua mãe a diga "Não. Você ficará na fazenda.", a saída deverá ser:

"Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!"

'''
