pontuacao = 0
musicas_tocadas = 0

while True:
  entrada = input()

  if entrada == "long live":
    musicas_tocadas += 1
    print(f"A Taylor conseguiu concluir o show sem muitas interrupções e cantou {musicas_tocadas} músicas.")
    break

  if entrada == "os fãs estão formando uma ciranda":
    pontuacao -= 3

  elif entrada == "os fãs estão ligando os flashes e atrapalhando a visão":
    pontuacao -= 2

  elif entrada == "os fãs estão dançando na frente da tela":
    pontuacao -= 2

  elif entrada == "os fãs estão gritando o nome da Taylor e atrapalhando a música":
    pontuacao -= 2

  elif entrada == "os fãs estão cantando as músicas em coro":
    pontuacao += 2

  elif entrada == "houve um pedido de casamento na sessão":
    pontuacao += 2

  else:
    pontuacao += 1
    musicas_tocadas += 1
  
  if pontuacao < 0:
    print(f"A Taylor só conseguiu cantar {musicas_tocadas} músicas e a sessão foi interrompida.")
    break
  
'''

A turnê de Taylor Swift chegou aos cinemas! O filme "Taylor Swift: The Eras Tour" mostra um show completo da artista, que fará shows no Brasil em novembro de 2023. Com isso, muitos fãs que não conseguiram garantir ingressos para ver a cantora estão aproveitando a experiência ao máximo nas salas de cinema de todo o país.

Várias cenas viralizaram nas redes sociais e o seu desafio é saber quantas músicas a Taylor conseguiu cantar antes da sessão ser interrompida.

Input

Você deverá receber entradas até que a pontuação se torne negativa ou o show seja encerrado. As entradas podem ser as músicas que estão na setlist do show ou acontecimentos envolvendo os fãs da Taylor.

Cada música vale +1 ponto.

Se acontecer alguma string da lista abaixo, os pontos são os seguintes:

"os fãs estão formando uma ciranda": -3 pontos

"os fãs estão ligando os flashes e atrapalhando a visão": -2 pontos

"os fãs estão dançando na frente da tela": -2 pontos

"os fãs estão gritando o nome da Taylor e atrapalhando a música": -2 pontos

"os fãs estão cantando as músicas em coro": +2 pontos

"houve um pedido de casamento na sessão": +2 pontos

A última música da setlist será "long live", onde Taylor chamará Paula Fernandes para cantar no palco (se ela conseguir concluir o show).

Obs.: Todas as entradas que não corresponderem às strings acima deverão ser consideradas como músicas.

Output

Se, após alguma ação dos fãs, a pontuação ficar negativa, deverá ser printada a seguinte mensagem e o programa será encerrado:

"A Taylor só conseguiu cantar {quantidade_de_musicas_tocadas} músicas e a sessão foi interrompida."

Se o programa receber "long live", que é a última música da setlist, o show será encerrado e a seguinte mensagem deverá ser exibida:

"A Taylor conseguiu concluir o show sem muitas interrupções e cantou {quantidade_de_musicas_tocadas} músicas."

Dica: Observe que você deverá contar, além da quantidade de pontos, a quantidade de músicas tocadas. Vale destacar que as ações dos fãs não valem como uma música tocada.

'''
