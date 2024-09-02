nome_missao = input()
quantidade_herois = 0
lista = []
heroi = " "

while heroi != "Grupo formado":
  heroi = input()
  quantidade_herois += 1
  lista.append(heroi)

lista.remove("Grupo formado")
quantidade_herois -= 1
print(f"O grupo formado por {quantidade_herois} heróis para a missão {nome_missao} foi:")

for heroi in lista:
  print(f"- {heroi}")
  
'''

O acampamento meio sangue é um lugar seguro onde os heróis, filhos de deuses gregos, vão para se proteger de ameaças mortais e treinar para missões perigosas que podem definir o destino da humanidade.

Recentemente, o oráculo tem anunciado várias profecias, fazendo com que diversos heróis precisem partir em missões, e como o grupo que faz parte de uma determinada missão é super importante, já que precisam de habilidades complementares e colaboração entre os membros, Quíron, diretor do acampamento quer desenvolver um programa que imprima o nome dos heróis em determinada missão, para que fique mais fácil saber os semideuses que não estão mais disponíveis.

Input

Primeiro, você receberá o nome da missão, em que os heróis partirão.

nome_missao

Em seguida, será recebido um número indeterminado de inputs, cada um com o nome de um herói que fará parte daquela missão.

heroi_1

heroi_2

...

heroi_n

Grupo formado

A string "Grupo formado", indicará o momento em que as entradas encerrarem e mais nenhum nome de herói será recebido.

Output

Como saída, você deverá imprimir primeiro a mensagem:

"O grupo formado por {quantidade_herois} heróis para a missão {nome_missao} foi:"

E em seguida, devem ser listados cada um dos nomes recebidos da seguite forma:

"- {heroi_1}"

"- {heroi_2}"

...

"- {heroi_n}"

OBS.: As aspas não devem sair no seu output.

'''
