n = int(input())
rep = 1
assento = 1

while n >= rep :
  musica = input().lower()
  pontos = 0

  for letra in musica :
    if (letra == "a") or (letra == "e") or (letra == "i") or (letra == "o") or (letra == "u") : 
      pontos += 1

    else :
      pontos += 2

  posicao = pontos
  assento *= posicao
  rep += 1
print(f"Parabéns por adquirir o ingresso! Seu assento é o {assento}, estamos ansiosos para vê-lo, vai ser incrível!")

'''

Bem-vindo ao desafio proposto pela estrela pop Taylor Swift! Ela é uma grande fã da programação e, para tornar o show ainda mais especial, decidiu contratar um programador para criar senhas de assentos únicas para os fãs.

Aqui está a missão: você receberá um número N de músicas famosas de Taylor Swift. Sua tarefa é decifrar qual será o número do assento de cada fã, com base nessas músicas. Para fazer isso, você deverá analisar as letras do nome de cada música que irá envolver apenas letras do alfabeto, sem acentos, espaços ou caracteres especiais. Cada vogal em uma música vale 1 ponto, enquanto cada consoante vale 2 pontos e a soma desses pontos gera o número associado daquela música que deverá ser multiplicado com os outros números associados das outras músicas recebidas. O resultado final corresponde ao número do assento.

Exemplo: No case exemplo 1, a música Lover tem 2 vogais e 3 consoantes, logo o número associado a ela será 8, já a música Delicate com 4 vogais e 4 consoantes gera o número 12. Esses dois números ao serem multiplicados resultam em 96, que é o número do assento do fã analisado.

As músicas que você terá à sua disposição incluem sucessos como Anti-Hero, Blank Space, You Belong With Me, Shake it off, Lover, Delicate, Lavender Haze e Our Song. E, para tornar as coisas mais emocionantes, cada caso teste terá 2 ou mais músicas dessas para criar a senha do assento.

Após o desafio, você exibirá uma mensagem personalizada para os fãs, revelando seus assentos

Agora, mãos à obra e divirta-se criando assentos musicais exclusivos para os fãs de Taylor Swift!

Input

A primeira entrada do seu código será um número inteiro N, que indicará o número de músicas que serão analisadas.

Exemplo:

3

Após isso, serão recebidas N entradas contendo os nomes das músicas a serem analisadas.

Exemplo:

AntiHero

BlankSpace

YouBelongWithMe

Output

A saída do seu código deve mostrar uma mensagem para o fã que irá ao show da cantora Taylor Swift, indicando o número do seu assento. A mensagem deve seguir esse padrão:

"Parabéns por adquirir o ingresso! Seu assento é o {numero_do_assento}, estamos ansiosos para vê-lo, vai ser incrível!"

'''
