n = int(input())
pontos_beyonce = 0
beyonce_pontos = 0
pontos_taylor = 0
taylor_pontos = 0
rodada = 1
fim_rodada = False
print("Vai começar! Vamos ver quem é a verdadeira diva!")

for i in range (n):
    if not fim_rodada:
      print(f"Vai começar a {rodada}º rodada!")
      nota_coreografia_taylor = int(input())
      nota_figurino_taylor = int(input())
      nota_coreografia_beyonce = int(input())
      nota_figurino_beyonce = int(input())
      pontos_beyonce = (4 * nota_coreografia_beyonce) + (3 * nota_figurino_beyonce)
      pontos_taylor = (4 * nota_coreografia_taylor) + (3 * nota_figurino_taylor)
      
      if pontos_taylor > pontos_beyonce:
        taylor_pontos += 1
      
      else:
        beyonce_pontos += 1
      placar_vencedor = max(pontos_taylor, pontos_beyonce)
      placar_perdedor = min(pontos_taylor, pontos_beyonce)
      diferenca_pontos = placar_vencedor - placar_perdedor
      
      if pontos_taylor > pontos_beyonce:
        cantora_x = "Tay"
      
      else:
        cantora_x = "Bey"
      print(f"Fim da apresentação! O placar da rodada {rodada} foi {placar_vencedor}x{placar_perdedor} para os representantes da {cantora_x}.")
      
      if diferenca_pontos > 20:
        print(f"A diferença na pontuação foi de {diferenca_pontos} pontos.")
      
      else:
        print(f"A diferença de pontos foi de apenas {diferenca_pontos}.")
      rodada += 1
      
      if taylor_pontos == 3 or beyonce_pontos ==3:
        fim_rodada = True
if pontos_taylor > pontos_beyonce:
  print(f"Uuuh! Por um placar de {taylor_pontos} a {beyonce_pontos}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!")

else:
  print(f"Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {beyonce_pontos} a {taylor_pontos}. A Bey é a verdadeira rainha do pop!")
  
'''

A rivalidade entre os fãs de Beyoncé e os fãs de Taylor Swift chegou a um ponto crítico. Eles decidiram resolver suas diferenças em uma competição para determinar quem é a verdadeira rainha do Pop. Duas equipes serão formadas, representando as artistas. Uma equipe será responsável por fazer uma apresentação representando a Taylor Swift, enquanto a outra equipe representará a Beyoncé.

A competição funcionará da seguinte forma: Um sorteio será realizado para definir quem integrará as equipes de cada artista. Em seguida, cada equipe apresentará um cover musical inspirado em sua artista preferida. O projeto será apresentado ao mundo todo ao vivo no talent show norte-americano - The Voice e, os calouros do CIn, por serem jovens prodígios da UFPE, foram designados como responsáveis por criar o programa que calculará a equipe vencedora.

Input

A primeira entrada será um inteiro n que corresponde ao número de apresentações que cada equipe fará na competição.

n

Por n vezes, será fornecido um par de entrada (números inteiros, que variam de 0 a 10) para cada equipe. Esse par corresponde as notas obtidas naquela apresentação.

As entradas serão entregues na seguinte ordem:

nota_coreografia_taylor

nota_figurino_taylor

nota_coreografia_beyonce

nota_figurino_beyonce

Cada nota recebida deve ser inserida na nota final da respectiva equipe, de acordo com a conversão abaixo:

1 ponto de coreografia = 4 pontos na nota final
1 ponto de figurino = 3 pontos na nota final
Exemplo: Se a equipe recebeu 8 na coreografia e 6 no figurino, deve-se adicionar 50 pontos à pontuação daquela equipe

A equipe que obtiver mais pontos, ganhará a rodada! E a equipe que ganhar mais rodadas, vence a competição.

Atenção: Caso uma equipe ganhe 03 rodadas, ela automaticamente ganha a competição. Ou seja, se houver apresentações restantes, elas não irão acontecer. E se apresentações não acontecem, elas não recebem notas!!!

OBS.: Não haverá empates

OBS. 2: É proibido o uso de break nessa questão!

Output

Primeiramente, você deve imprimir:

"Vai começar! Vamos ver quem é a verdadeira diva!”

No começo de cada rodada, você deve imprimir:

"Vai começar a {x}º rodada!"

Onde x representa o número daquela rodada

No final das rodadas, você deve imprimir:

"Fim da apresentação! O placar da rodada {x} foi {placar_vencedor}x{placar_perdedor} para os representantes da {cantora_x}."

Sendo o {placar_vencedor} a quantidade de pontos da equipe que venceu a rodada, da mesma forma o {placar_perdedor} representa a pontuação da equipe perdedora, e a {cantora_x} é a cantora cuja equipe se saiu vitoriosa, que será carinhosamente apelidada de "Tay" ou "Bey".

Caso a diferença de pontos do vencedor para a equipe derrotada seja maior que 20 pontos numa rodada, imprima:
"A diferença na pontuação foi de {diferenca_pontos} pontos.”

Caso contrário, imprima:
“A diferença de pontos foi de apenas {diferenca_pontos}."

Caso a equipe da Taylor saia vencedora, imprima:
“Uuuh! Por um placar de {y_equipe_vitoriosa} a {y_equipe_perdedora}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!”

Caso a equipe da Beyoncé vença, imprima:
“Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {y_equipe_vitoriosa} a {y_equipe_perdedora}. A Bey é a verdadeira rainha do pop!"

Onde {y_equipe_vitoriosa} representa a quantidade de rodadas vencidas pela a equipe vencedora, enquanto {y_equipe_perdedora} representa a quantidade de partidas vencidas pela equipe perdedora.

'''
