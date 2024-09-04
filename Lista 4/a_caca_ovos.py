def calcular_max(valor1, valor2):
  if valor1 > valor2:
    return valor1
  
  elif valor1 < valor2:
    return valor2

def calcular_ovos_encontrados(ovos_escondidos_dia, numero_dia, horoscopo_dia):
  if horoscopo_dia == "Os astros estão radiantes hoje! Eles farão o possível para abençoar a todos com boa sorte.":
    return ovos_escondidos_dia
  
  elif horoscopo_dia == "Os astros estão de bom humor hoje. Acho que você terá um pouco de sorte extra.":
    return int(ovos_escondidos_dia * 0.7)
  
  elif horoscopo_dia == "As estrelas estão neutras hoje. O dia está em suas mãos.":
    return int(calcular_max(ovos_escondidos_dia * 0.7, ovos_escondidos_dia / ((ovos_escondidos_dia % numero_dia) + 1)))
  
  elif horoscopo_dia == "Isso é raro. As estrelas estão absolutamente neutras hoje.":
    return int((ovos_escondidos_dia % numero_dia) + 1)

  else:
    return 0

qtd_dias = int(input())
total_ovos_encontrados = 0
total_ovos_escondidos = 0

for i in range(1, qtd_dias + 1):
  ovos_escondidos_dia = int(input())
  horoscopo_dia = input()

  ovos_encontrados_dia = calcular_ovos_encontrados(ovos_escondidos_dia, i, horoscopo_dia)
  total_ovos_encontrados += ovos_encontrados_dia
  total_ovos_escondidos += ovos_escondidos_dia

  print(f"Dia {i}")
  print(f"Hoje Carlos encontrou {ovos_encontrados_dia} ovos!!")

  aproveitamento = (total_ovos_encontrados / total_ovos_escondidos) * 100

print(f"Kiq encontrou {total_ovos_encontrados} de um total de {total_ovos_escondidos}")

if aproveitamento == 100:
  print("Incrível! Seu signo está em alta. Você encontrou todos os ovos!")

elif 66 < aproveitamento <= 100:
  print("Ótimo trabalho! Os astros estão ao seu lado. Você encontrou a maioria dos ovos!")

elif 33 < aproveitamento <= 66:
  print("Bom esforço! Os astros sorriem para você. Muitos ovos foram encontrados.")

elif 0 < aproveitamento <= 33:
  print("Continue procurando! Seu horóscopo sugere que há mais ovos a serem encontrados.")

else:
  print("Ainda não encontrou nenhum ovo. O horóscopo aconselha persistência. Continue tentando!")

'''

O ex-monitor de IP e atual monitor de AVLC, Kiq, está prestes a viver uma aventura emocionante durante a caça aos ovos de Páscoa. Ele confia no horóscopo para orientá-lo nessa jornada repleta de surpresas e desafios. Então, ele decidiu que vai ler o horóscopo todos os dias de evento.

Kiq precisa criar um programa que o auxilie a coletar dados durante a caçada e, ao final, realizar análises intrigantes usando técnicas de algebra linear. Para isso, ele pediu a sua ajuda, aluno de IP/P1.

Primeiro, ele precisa saber quantos dias será a caçada. Além disso, ele gostará de ler o horoscopo todos os dias. Kiq quer visualizar de formas simples quantos ovos ele encontrou em cada dia e, após isso, gostaria de uma analise total de todos os dias.

A verdadeira magia acontece na mensagem final, onde as conquistas de Kiq são interpretadas à luz das estrelas. A porcentagem de ovos encontrados em relação ao total escondido é calculada, revelando insights astrológicos sobre seu desempenho na caçada e proporcionando a Kiq uma análise cósmica personalizada de sua jornada de Páscoa.

Com este programa, Kiq não apenas desfrutará da caça aos ovos, mas também terá uma experiência astrológica única, proporcionando uma abordagem lúdica e mística para a análise final de seus feitos.

Input

O primeiro valor a ser recebido será o número de dias, este valor inteiro define por quanto tempo a caçada aos ovos ocorrerá, guiada pelas previsões astrológicas diárias.:

qtd_dias

Para cada dia da caçada, fornecemos quantos ovos estão escondidos no dia, um desafio único para a jornada de Kiq e a frase do horóscopo que servirá como bússola cósmica para as atividades do dia:

ovos_escondidos_dia

horoscopo_dia (Horóscopo do Dia):

O Horóscopo do dia é usado para calcular quantos ovos foram encontrados naquele dia. O cálculo é feito da seguinte forma para cada frase:

"Os astros estão radiantes hoje! Eles farão o possível para abençoar a todos com boa sorte."

→ ovos_encontrados = ovos_escondidos_dia

"Os astros estão de bom humor hoje. Acho que você terá um pouco de sorte extra."*

→ ovos_encontrados = ovos_escondidos_dia* 0.7

"As estrelas estão neutras hoje. O dia está em suas mãos."*

→ ovos_encontrados = max(ovos_escondidos_dia* 0.7, ovos_escondidos_dia/ ((ovos_escondidos_dia% numero_dia) + 1))

"Isso é raro. As estrelas estão absolutamente neutras hoje."*

→ ovos_encontrados = (ovos_escondidos_dia% numero_dia) + 1

"Hoje, Kiq não pôde consultar as estrelas. Sem a orientação astrológica, a busca por ovos fica à mercê do destino."*

→ Nesse caso, Kiq se sente muito desmotivado e não consegue encontrar nenhum ovo.

Como Kiq só pode contar ovos inteiros, ele joga fora os ovos quebrados que encontra. Para isso, você precisará calcular apenas a parte inteira do número de ovos_encontrados.

Obs.1: Você não pode usar nenhuma função integrada do Python para calcular max, devendo criar sua própria função que retorna o maior entre dois valores.

Obs.2: Na(s) função(ões) que criar, não utilize variáveis globais, em vez disso, utilize passagem de parâmetros e o return para acessar e modificar variáveis de fora da função.

Output

Ao fim de cada dia, o programa compartilha as seguintes informações com Kiq:
"Dia {i}"

"Hoje Carlos encontrou {ovos_encontrados_dia} ovos!!"

Ao fim do evento de caça aos ovos, Kiq receberá um resumo impactante:
"Kiq encontrou {total_ovos_encontados} de um total de {total_ovos_escondidos}"

Quantidade TOTAL de ovos, ou seja, valor acumulado durante todo o evento.

Após isso você deve imprimir a mensagem final

Você deve calcular o aproveitamento de kiq na caça aos ovos, calculando a % de ovos encontrados por kiq em relação à quantidade total de ovos

aproveitamento = (total_ovos_encontrados / total_ovos_escondidos) * 100

Caso o aproveitamento seja de 100%, imprima:

"Incrível! Seu signo está em alta. Você encontrou todos os ovos!"

Caso seja maior que 66% e menor que 100%, imprima:

"Ótimo trabalho! Os astros estão ao seu lado. Você encontrou a maioria dos ovos!"

Caso seja maior que 33% e menor ou igual a 66%, imprima:

"Bom esforço! Os astros sorriem para você. Muitos ovos foram encontrados."

Caso seja maior que 0 e menor ou igual a 33%, imprima:

"Continue procurando! Seu horóscopo sugere que há mais ovos a serem encontrados."

Caso seja igual a 0, imprima:

"Ainda não encontrou nenhum ovo. O horóscopo aconselha persistência. Continue tentando!"

'''
