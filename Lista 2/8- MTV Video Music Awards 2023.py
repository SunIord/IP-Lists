n= int(input())
celebridade = " "
pontos = 0
candidato = " "
kanye = False
gerard = False
chris = False
taylor = False
katy = False
ariana = False
beyonce = False
shakira = False

while (pontos != n):
  celebridade = input()
  pontos += 1

  if celebridade == "Kanye West":
    kanye = True

  if celebridade == "Gerard Piqué":
    gerard = True

  if celebridade == "Chris Martin":
    chris = True
  print(f"Apresentador: Contamos com a ilustre presença de {celebridade}, uma salva de palmas!")

while (candidato != "Início da Premiação"):
  candidato = input()

  if candidato == "Taylor Swift":
    taylor = True

  if candidato == "Katy Perry":
    katy = True 

  if candidato == "Ariana Grande":
    ariana = True

  if candidato == "Beyoncé":
   beyonce = True

  if candidato == "Shakira":
    shakira =True

print("Apresentador: Vamos deixar de enrolação e ir para a premiação!")
print("Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...")

if taylor == True:
  print("TAYLOR SWIFT")

  if kanye == True:
    print("Kanye West: Eu vou te deixar terminar. Estou feliz por você, mas Beyoncé fez um dos melhores vídeos de todos os tempos.")

elif taylor == False and katy == True:
  print("KATY PERRY")

elif taylor == False and katy == False and ariana == True:
  print("ARIANA GRANDE")

elif taylor == False and katy == False and ariana == False and beyonce ==True:
  print("BEYONCÉ")

  if chris == True:
    print("Chris Martin: Minha heroína, minha irmã, meu tudo. Você merece!")

elif taylor == False and katy == False and ariana == False and beyonce == False and shakira == True:
  print("SHAKIRA")

  if gerard == True:
    print("Gerard Piqué: Meu amor me perdoa, volta pra mim...")
    
'''

Todo ano ocorre a premiação do MTV Video Music Awards (VMA) e, para evitar a recorrência de polêmicas no resultado desse ano, o MTV pediu para os alunos de IP/P1 fazerem um programa que consiga prever o que irá acontecer na premiação de acordo com os dados informados. Dessa forma, os organizadores do evento estarão preparados para as possíveis ocorrências no dia da premiação.

Input

Você receberá uma entrada N correspondente ao número de celebridades presentes na premiação. E, após isso, uma sequência de N inputs com os nomes das respectivas celebridades.

N

celebridade1

celebridade2

...

celebridadeN

Exemplo:

1

Elton John

Após todas as N entradas, a apresentação das celebridades termina. Em seguida você receberá uma sequência de inputs com os nomes dos candidatos ao prêmio VMA. Caso um desses inputs seja "Início da Premiação", então todos os concorrentes ao prêmio já foram informados e o programa passa para a próxima etapa.

nome_candidato1

nome_candidato2

...

"Início da Premiação"

Exemplo:

Katy Perry

Taylor Swift

Anitta

Início da Premiação

Output

Para cada celebridade presente na premiação, o programa deverá anunciá-la da seguinte forma:

"Apresentador: Contamos com a ilustre presença de {celebridade}, uma salva de palmas!".

É nesse momento que você deve se atentar para caso apareçam o Kanye West, Gerard Piqué, Chris Martin.

Quando se iniciar a premiação, não importa quantos nomes sejam ditos, somente 5 possíveis nomes podem ganhar o prêmio, são eles: "Taylor Swift", "Katy Perry", "Ariana Grande", "Beyoncé", "Shakira". Em qualquer caso, pelo menos uma dessas aparecerá. Caso apareça mais de uma, deve-se seguir uma regra de hierarquia da primeira à quinta, respectivamente.

Quando se iniciar a premiação, ou seja, todos os nomes de concorrentes já foram passados, deverá ser impresso:

"Apresentador: Vamos deixar de enrolação e ir para a premiação!"

Após a análise da possível vencedora do prêmio, você imprimirá:

"Apresentador: E a artista do ano do MTV Video Music Awards 2023 é..."

seguido do nome da artista na próxima linha em maiúsculo, como:

NOME

Exemplo:

Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...

TAYLOR SWIFT

Em seguida, você deve imprimir uma previsão do que irá acontecer na plateia de acordo com o possível resultado da premiação:

Caso Taylor Swift vença e Kanye West esteja no evento, imprima:
"Kanye West: Eu vou te deixar terminar. Estou feliz por você, mas Beyoncé fez um dos melhores vídeos de todos os tempos."

Caso Shakira vença e Gerard Piqué esteja no evento, imprima:
"Gerard Piqué: Meu amor me perdoa, volta pra mim..."

Caso Beyoncé vença e Chris Martin esteja no evento imprima:
"Chris Martin: Minha heroína, minha irmã, meu tudo. Você merece!"

Caso não ocorra nenhum desses casos, não precisa imprimir nada.

Atenção: Lembre-se que só é permitido o uso do que já foi visto na disciplina até então.

'''
