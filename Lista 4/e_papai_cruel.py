def desafio_pangrama(frase):
  frase = frase.replace(" ", "").lower()
  pangrama = all(frase.count(letra) > 0 for letra in 'abcdefghijklmnopqrstuvwxyz')
  letra_repetida = max(set(frase), key=frase.count) if pangrama else min(set(frase), key=frase.count)
  return frase.count(letra_repetida)

def desafio_fibonacci(palavra):
  n = len(palavra)
  fib_resultado = fibonacci(n)
  return fib_resultado * 4 if any(letra in 'aeiou' for letra in palavra) else fib_resultado * 2

def fibonacci(n):
  sequencia_fib = [0, 1]
  if n <= 1:
    return sequencia_fib[n]
  
  else:
    for i in range(2, n + 1):
      sequencia_fib.append(sequencia_fib[-1] + sequencia_fib[-2])
    return sequencia_fib[-1]

def desafio_diferenca_letras(palavra_z, frase_z):
  maiusculas_p = 0
  minusculas_p = 0
  for letra in palavra_z:
    if letra.isupper():
      maiusculas_p += 1
    
    else:
      minusculas_p += 1
  
  dif_palavra = minusculas_p - maiusculas_p
  
  maiusculas_f = 0
  minusculas_f = 0 
  for letras in frase_z.replace(" ",""):
    if letras.isupper():
        maiusculas_f += 1
  
    else:
        minusculas_f += 1
  dif_frase = minusculas_f - maiusculas_f 
  
  z_noel = int((dif_frase)**(dif_palavra))
  return z_noel

def calcular_distancia(x_noel, y_noel, z_noel, x_jack, y_jack, z_jack):
  distancia = ((x_noel - x_jack) ** 2 + (y_noel - y_jack) ** 2 + (z_noel - z_jack) ** 2) ** 0.5 
  return distancia

frase_x = input()
x_noel = desafio_pangrama(frase_x)
print(f"A 1ª coordenada do Papai Noel é: {x_noel}")

palavra_y = input()
y_noel = desafio_fibonacci(palavra_y)
print(f"A 2ª coordenada do Papai Noel é: {y_noel}")

palavra_z = input()
frase_z = input()
z_noel = desafio_diferenca_letras(palavra_z, frase_z)
print(f"A 3ª coordenada do Papai Noel é: {z_noel}")

x_jack = int(input())
y_jack = int(input())
z_jack = int(input())

distancia_final = calcular_distancia(x_noel, y_noel, z_noel, x_jack, y_jack, z_jack)
print(f"A distância entre Jack Esqueleto e Papai Noel é: {distancia_final:.2f}")

'''

Um mês antes do Natal, Jack Esqueleto desejava transformar-se no Papai Noel e, para que isso, acontecesse ele precisava se livrar do verdadeiro Papai Noel. Assim, teve a ideia de pedir a Tranca, Choque e Rapa que o sequestrassem e trancassem em um local onde ninguém pudesse encontrá-lo até o fim do Natal.

Entretanto, após algum tempo, Jack voltou atrás na ideia de se tornar o Papai Noel e decidiu continuar apenas celebrando o Halloween. Assim, perguntou a Tranca, Choque e Rapa a localização do bom velhinho para poder salvar o Natal.

Os três brincalhões concordaram em dizer, porém, só revelariam as coordenadas a Jack se ele conseguisse resolver o desafio proposto por cada um, recebendo assim as coordenadas x, y e z do Papai Noel.

Será que Jack conseguirá encontrar o Papai Noel a tempo?

Input

1º Desafio (x):
No primeiro desafio, proposto por Tranca e relacionado à coordenada x, Jack receberá como entrada apenas uma frase:

frase_x (string)

Posteriormente, Jack deve determinar se a frase recebida é um pangrama. Se for um pangrama, a resposta deve ser a contagem da letra que mais se repete na frase. Se não for um pangrama, a resposta será a contagem da letra que menos se repete na frase.

Assim, Jack terá desvendado a primeira coordenada do Papai Noel:

x_noel (inteiro)
2º Desafio (y):
No segundo desafio, proposto por Choque e relacionado à coordenada y, Jack receberá como entrada apenas uma palavra.

palavra_y (string)

Posteriormente, Jack deve calcular o número de Fibonacci com base no comprimento da palavra. Se a palavra contiver vogais, a resposta será o resultado de Fibonacci multiplicado por 4. Caso não tenha vogais, a resposta será o resultado de Fibonacci multiplicado por 2.

Assim, Jack terá desvendado a segunda coordenada do Papai Noel:

y_noel (inteiro)
3º Desafio (z):
No terceiro desafio, proposto por Rapa e relacionado à coordenada z, Jack receberá como entrada primeiro uma palavra e depois uma frase.

palavra_z (string)

frase_z (string)

Posteriormente, Jack deve calcular a diferença entre a quantidade de letras minúsculas e a quantidade de letras maiúsculas da palavra. Da mesma forma, deve calcular a diferença entre a quantidade de letras minúsculas e a quantidade de letras maiúsculas da frase. Por fim, elevar o resultado do cálculo da frase à potência do resultado do cálculo da palavra.

Assim, Jack terá desvendado a terceira coordenada do Papai Noel:

z_noel (inteiro)
Distância Final:
Agora que Jack tem as coordenadas do Papai Noel, ele precisa localizar suas próprias coordenadas (x, y e z).

x_jack (inteiro)

y_jack (inteiro)

z_jack (inteiro)

Posteriormente, utilizando a fórmula de distância entre dois pontos no espaço tridimensional, expressa como:

d(noel, jack)^2 = (x_noel - x_jack)^2 + (y_noel - y_jack)^2 + (z_noel - z_jack)^2
Jack deve calcular a distância entre ele e o Papai Noel.

distancia_final (float)
OBS.: Um pangrama é uma frase que contém todas as letras do alfabeto pelo menos uma vez.

Output

Ao final de cada desafio, Jack deverá imprimir na tela a seguinte frase:

“A {numero_desafio}ª coordenada do Papai Noel é: {coordenada_noel}”

Por fim, obtendo a distância entre ele e o Papai Noel, Jack deverá imprimir na tela, informando essa distância com até duas casas decimais, a seguinte frase:

“A distância entre Jack Esqueleto e Papai Noel é: {distancia}”

Dica:
Para tornar mais fácil, Jack deve tratar adequadamente as frases em cada desafio, levando em consideração o contexto específico. É permitido utilizar as funções min() e max(), as quais podem ser muito úteis. Também não haverão caracteres especiais, pontuações ou acentos nas frases e palavras. Além disso, atente-se aos espaços entre palavras de uma frase.

Observação:
É obrigatório que o código contenha no mínimo três funções, uma para cada desafio, e é terminantemente proibido o uso de qualquer biblioteca externa.

'''
