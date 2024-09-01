num_versos = int(input())
input_plateia = " "
verso = 0
pontos = 0

for i in range(1 , num_versos + 1):
  input_plateia = input().lower()

  if verso == 0:
    verso += 1
    print("Cause, baby, now we've got")

    if input_plateia == "bad blood":
      pontos += 1
      print(f"{input_plateia}".upper())

  elif verso == 1:
    verso += 1
    print("You know it used to be")

    if input_plateia == "mad love":
      pontos += 1
      print(f"{input_plateia}".upper())

  elif verso == 2:
    verso += 1
    print("So take a look what")

    if input_plateia == "you've done":
      pontos += 1
      print(f"{input_plateia}".upper())

  elif verso == 3:
    verso += 1
    print("Cause, baby, now we've got")

    if input_plateia == "bad blood, hey":
      pontos += 1
      print(f"{input_plateia}".upper())

if pontos == num_versos:
  print("A plateia deu um show! Acertou tudo!")

elif pontos >= (0.5 * num_versos):
  print("A plateia acertou a maior parte da música")

elif pontos < (0.5 * num_versos):
  print("Foi um dia atípico e a plateia se esqueceu de grande da música")

'''

Em um novo show, Taylor Swift teve como convidado especial o rapper Kendrick Lamar, para performarem ao vivo, em celebração do lançamento da nova versão da música Bad Blood, em que ambos colaboraram: Bad Blood (Taylor's Version) (Remix ft. Kendrick Lamar)

Apesar de muito similar, os artistas estavam ansiosos para ver o engajamento dos fãs, pelo fato de que não estrelavam em um show juntos há um tempo, e, com isso, decidiram tentar no início da música cantar parte dos versos, e incentivar a plateia a completar cantando o resto deles.

Os artistas, porém, por estarem focados em sua apresentação e estarem em um local onde a dinâmica de som não favorecia muito a percepção da plateia como um todo, ouviram apenas parcialmente as respostas dos fãs, e, após o show, ficaram curiosos para saber o quão precisos os fãs tinham sido ao completar as partes da letra da música.

O seu trabalho é: Recebendo, a cada verso incompleto, o som emitido pela plateia como um todo, documentar e verificar a precisão da cantoria dos fãs em relação as letras reais da música.

Para facilitar isso, está aqui uma tabela dos versos, sendo a primeira parte a parte que irá ser cantadas pelos artistas, e a segunda a parte que eles esperam ouvir da plateia.

Elas seguem o formato:

1° parte do verso

2° parte do verso

Além disso, eles decidirão a quantidade de versos que irão tentar deixar a plateia completar anteriormente, sendo o número máximo de versos 4 e o mínimo 1.

Os versos são:

1° verso:

Cause, baby, now we've got

BAD BLOOD

2° verso:

You know it used to be

MAD LOVE

3° verso:

So take a look what

YOU'VE DONE

4° verso:

Cause, baby, now we've got

BAD BLOOD, HEY

Input

Inicialmente, você receberá o número exato de versos a ser cantado/completado pela plateia

numVersos

Em seguida, para cada verso a ser cantado pela plateia, você receberá uma string correspondente ao que predominantemente cantaram

inputPlateia

Output

Deve ser printado, para cada verso:

A primeira parte do verso cantada pelos artistas, como dada na descrição da questão.

Em seguida, somente se a resposta da plateia após ser convertida para letras maiúcusculas seja igual ao trecho esperado, você deve imprimir:

A segunda parte do verso, como dada na descrição da questão.

Obs. 1: A conversão para letras maiúsculas acontece pois uma eventual desafinação não é relevante. Afinal, o objetivo é acertarem as palavras.

Obs. 2: Para esta questão, caso ache necessário, será permitido o uso da função .upper() e variantes, apenas em um único carácter por vez.

E, no final, deve-se imprimir uma frase em formato de string em relação à performance da plateia.

Caso a plateia tenha certado todos os versos, deve-se imprimir na tela:
A plateia deu um show! Acertou tudo!

Porém, caso não tenha acertado tudo, mas pelo menos 50% dos versos, deve-se mostrar:
A plateia acertou a maior parte da música

Alternativamente, caso tenham acertado menos do que 50% da música, deve-se exibir:
Foi um dia atípico e a plateia se esqueceu de grande da música

'''
