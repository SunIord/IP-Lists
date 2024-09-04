def soma_codigos(nome):
  total = 0
  
  for i in nome:
    if i != '':
      total += ord(i)

  if (total % 2 != 0) and (nome_presente not in presentes_excluidos):
    presentes_excluidos.append(nome_presente)

  elif (total % 2 == 0) and (nome_presente not in presentes_decodificados) and (nome_presente not in presentes_excluidos):
    presentes_decodificados.append(nome_presente)

def decodificar_presente(presente_codificado):
  presente_decodificado = ''
  
  for j in presente_codificado:
    if j != '':
      presente_decodificado += chr(int(j))

  return presente_decodificado

n = int(input())
presentes_decodificados = []
presentes_excluidos = []

for k in range(n):
  presente_codificado = input().split()
  nome_presente = decodificar_presente(presente_codificado)
  
  if (nome_presente in presentes_decodificados) or (nome_presente in presentes_excluidos):
    print(f"{nome_presente} já está na lista de presentes da Anya!!")
  
  else:
    print(f"{nome_presente} foi adicionado a lista ultrassecreta de presentes da Anya!!")

  soma_codigos(nome_presente)
  
if (len(presentes_excluidos) > 0):
  print(f'Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: {", ".join(presentes_excluidos)}.')

if (len(presentes_decodificados) == 0 or (presentes_decodificados == [' '])):
  print('O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!') 

elif (len(presentes_excluidos) == 0) or (presentes_excluidos == [' ']):
  print('Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…')

if len(presentes_decodificados) != 0:
  print(f'Lista final dos melhores presentes da Anya: {", ".join(presentes_decodificados)}.')
  
'''

O Dia das Crianças é uma data mágica que traz um brilho especial aos olhos de todas as crianças. É um dia de alegria, surpresas e, é claro, presentes! As crianças mal podem esperar para ver o que lhes espera neste dia tão especial.

E, como em qualquer família, na casa dos Forger, o Dia das Crianças é um evento repleto de expectativas e entusiasmo. Anya, a jovem telepática da família, está especialmente animada para a ocasião. Mas, há um pequeno problema - Anya pode ler mentes! Isso mesmo, ela sempre acaba descobrindo os presentes antes mesmo de abri-los. Mas seu pai Twilight tem um plano engenhoso para manter a surpresa e fazer deste Dia das Crianças um evento verdadeiramente mágico.

Twilight pediu a ajuda dos alunos de IP/P1 do CIN para desenvolver um programa em Python que o auxiliará a escolher os presentes perfeitos para Anya. Twilight já preparou uma lista de possíveis presentes, mas eles estão codificados usando caracteres na tabela ASCII, justamente para a Anya não descobrir antes da hora.

Seu trabalho será decodificar os presentes, ou seja, converter esses códigos ASCII de volta para os nomes dos brinquedos originais. Além disso, você precisará aplicar o critério de exclusão estabelecido por Twilight: apenas os brinquedos em que a soma dos códigos ASCII das letras de seus nomes resultar em um número par poderão fazer parte da lista final de presentes para o Dia das Crianças.

Antes de começar, é importante entender o que é a tabela ASCII. A tabela ASCII é uma representação numérica de caracteres. Por exemplo, o caractere 'a' é representado pelo número 97 na tabela ASCII. Para mais informações e visualização da tabela completa, você deve pesquisar na internet.

Atenção: nesta questão, você usará a função chr() para decodificar os presentes a partir dos códigos ASCII.

Requisitos da questão:

Criar uma função para somar os valores dos códigos de cada presente
Criar uma função para decodificar o nome do presente
Utilizar passagem de parâmetros e return nas suas funções
Não utilizar a função sum()
Não utilizar variável global
Input

Primeiro, você receberá um valor n correspondente a quantidade de possíveis presentes que Anya poderá ganhar:

n

Logo após, você receberá n vezes as entradas correspondentes aos nomes codificados dos presentes:

presente_codificado_1

presente_codificado_2

….

presente_codificado_n

Output

Para cada presente decodificado, você deverá imprimir:
{presente_decodificado_x} foi adicionado a lista ultrassecreta de presentes da Anya!!

Caso algum presente se repita na lista, independete dele cumprir o critério de exclusão ou não, você deve imprimir:
{presente_decodificado_x} já está na lista de presentes da Anya!!

Após todos os presentes decodificados, caso haja um ou mais brinquedos que devam ser excluídos da lista final de presentes, você deverá imprimir:
Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: {lista_de_presentes_excluidos}.

Caso nenhum brinquedo seja excluído e ela realmente ganhe algum presente, imprima:
Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…

Caso a lista de presentes fique vazia, imprima:
O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!

Por último, no caso da lista de presentes não ter sido zerada, imprima:
Lista final dos melhores presentes da Anya: {lista_presentes_final}.

Obs.: Ao printar {lista_de_presentes_excluidos} ou {lista_presentes_final}, os items da lista devem ser printados separados uns dos outros por uma vígula e um espaço.

'''
