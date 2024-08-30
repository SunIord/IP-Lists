pontuacao = 0
direcao_escolhida1 = input()
numero_porta = int(input())
opcao1 = str()
opcao2 = str()
opcao3 = str()
opcao4 = str()
opcao5 = str()

if numero_porta % 2 == 0 :
    direcao_certa = "esquerda"

else : 
    direcao_certa = "direita"

if direcao_escolhida1 == direcao_certa :
    pontuacao += 150
    opcao1 = "CERTA"

else :
    pontuacao -= 150
    opcao1 = "ERRADA"

direcao_escolhida2 = input()
cor_porta = input()
planta_porta = input()
forma_macaneta = input()

if (cor_porta == "dourada" or cor_porta == "prateada") or ((planta_porta == "avenca" or planta_porta == "espadinha") and forma_macaneta == "redonda") :
    direcao_certa = "direita"

else : 
    direcao_certa = "esquerda"

if direcao_escolhida2 == direcao_certa :
    pontuacao += 200
    opcao2 = "CERTA"

else : 
    pontuacao -= 200
    opcao2 = "ERRADA"

direcao_escolhida3 = input()
cor_porta = input()
numero_porta = int(input())
planta_porta = input()
forma_macaneta = input()

if ((numero_porta % 5 == 0) and (planta_porta == "espadinha") and (forma_macaneta == "quadrada")) or (cor_porta == "perolada"):
    direcao_certa = "esquerda"

else : 
    direcao_certa = "direita"

if direcao_escolhida3 == direcao_certa :
    pontuacao += 250
    opcao3 = "CERTA"

else : 
    pontuacao -= 250
    opcao3 = "ERRADA"

direcao_escolhida4 = input()
numero_porta = int(input())

if (numero_porta % 3 == 0) and (numero_porta % 2 != 0) and (numero_porta % 5 != 0) :
    direcao_certa = "direita"

else :
    direcao_certa = "esquerda"

if direcao_escolhida4 == direcao_certa :
    pontuacao += 300
    opcao4 = "CERTA"

else :
    pontuacao -= 300
    opcao4 = "ERRADA"

cor_porta = input()
numero_porta = int(input())
planta_porta = input()
flor_lado = input()
forma_macaneta = input()

if (cor_porta == "acobreada") and ((numero_porta % 2 == 1) or (forma_macaneta == "triangular" or forma_macaneta == "quadrada")) and (planta_porta == "jiboia") :
    pontuacao += 500
    opcao5 = "CERTA"

elif (cor_porta == "prateada") and ((flor_lado != "margarida") or (flor_lado != "papoula") or (flor_lado != "cosmos") and ((forma_macaneta == "hexagonal") or (forma_macaneta == "redonda"))) :
    pontuacao += 450
    opcao5 = "CERTA"

elif (cor_porta == "dourada") and ((flor_lado == "lirio") or (flor_lado == "ixora")) and (forma_macaneta == "hexagonal") :
    pontuacao += 400
    opcao5 = "CERTA"

else :
    pontuacao -= 500
    opcao5 = "ERRADA"

print("ARISU, VOCÊ FEZ SUAS ESCOLHAS E AGORA VEREMOS SE ESCOLHEU AS PORTAS CERTAS:")
print(opcao1, opcao2, opcao3, opcao4, opcao5)

if (pontuacao > 0) and ((opcao1 == "ERRADA") or (opcao2 == "ERRADA") or (opcao3 == "ERRADA") or (opcao4 == "ERRADA") or (opcao5 == "ERRADA")) :
    print(f'Você passou com {pontuacao} pontos, mas faça melhores escolhas da próxima vez.')

elif (pontuacao > 0) and ((opcao1 == "CERTA") and (opcao2 == "CERTA") and (opcao3 == "CERTA") and (opcao4 == "CERTA") and (opcao5 == "CERTA")) :
    print(f'Parece que a sorte está ao seu favor, Arisu... Você conseguiu passar com {pontuacao} pontos!')

elif (pontuacao < 0) and ((opcao1 == "CERTA") or (opcao2 == "CERTA") or (opcao3 == "CERTA") or (opcao4 == "CERTA") or (opcao5 == "CERTA")) :
    print(f'Por mais que você tenha feito escolhas corretas, não foi suficiente para sobreviver. Você finalizou o jogo com {pontuacao} pontos')

elif (pontuacao < 0) and ((opcao1 == "ERRADA") and (opcao2 == "ERRADA") and (opcao3 == "ERRADA") and (opcao4 == "ERRADA") and (opcao5 == "ERRADA")) :
    print(f'Todas suas escolhas foram erradas, Arisu, esperávamos mais de você... Você será executado pois obteve {pontuacao} pontos.')
    
'''

Neste episódio de "Alice in Borderland," Arisu se encontra diante de um novo e desafiador enigma. Ele se vê no centro de um labirinto misterioso, composto por um emaranhado de corredores sinistros, e cada passagem apresenta uma bifurcação com apenas duas opções: direita ou esquerda. Mas este labirinto é diferente - em cada uma dessas portas, um enigma intrincado aguarda, com o destino de Arisu pendendo por um fio. Ele inicia sua jornada com zero pontos, e cada escolha de direção que ele fizer o fará ganhar a pontuação referente a porta, caso seja a direção certa, ou perder a pontuação, caso seja a direção errada. O objetivo? Acumular pontos suficientes para escapar ileso deste labirinto mortal e voltar ao mundo real, ou enfrentar um destino trágico caso sua pontuação se torne negativa.

No coração deste desafio, você é o mestre que dita as regras. Cada porta representa uma decisão a ser tomada por Arisu, e a sorte está em suas mãos. As regras por trás de cada escolha permanecem ocultas, desafiando Arisu a decifrar o que o aguarda além de cada bifurcação. Sua pontuação será afetada por suas escolhas, ganhando ou perdendo pontos com base no resultado de cada enigma. Ao final do desafio, se Arisu tiver uma pontuação positiva, ele escapará com vida, mas se sua pontuação for negativa, ele enfrentará um destino trágico. O público fica ansioso para ver como ele navegará por esse labirinto mortal, onde cada escolha determina o rumo de sua jornada em "Alice in Borderland".

Input

Você receberá algumas informações para cada uma das 5 portas que Arisu escolher, que podem ser: a direcao que ele escolheu, a cor da porta, o numero que está nela, a planta que está na frente, a flor que está ao lado e a forma da maçaneta, cada característica em uma linha diferente, exemplo:

direita

acobreada

quadrada

Primeira porta

Vale 150 pontos
As características que você vai receber para analisar serão: direção_escolhida e número (nessa ordem)
→ A direção certa será direita caso o número da porta seja ímpar, senão a direção certa é a esquerda

Segunda porta

Vale 200 pontos
As características que você vai receber para analisar serão: direção_escolhida, cor, planta e maçaneta (nessa ordem)
→ A direção certa será direita caso (a cor da porta seja dourada ou prateada) ou ((a planta que estiver na frente seja avenca ou espadinha) e a maçaneta seja redonda) , senão deve ser escolhida a esquerda

Terceira porta

Vale 250 pontos
As características que você vai receber para analisar serão: direção_escolhida, cor, número, planta, maçaneta (nessa ordem)
→ A direção certa será a esquerda caso (o número da porta seja divisível por 5, a planta da frente seja espadinha e a maçaneta seja quadrada) ou (a cor seja perolada), senão a direção certa é a direita

Quarta porta

Vale 300 pontos
As características que você vai receber para analisar serão: direção_escolhida e número (nessa ordem)
→ A direção certa será direita caso o número da porta seja divisível por 3, mas não por 2 e não por 5, senão a direção certa é a esquerda

Quinta porta

Pode valer 500, 450 ou 400 pontos positivos ou 500 pontos negativos
As características que você vai receber para analisar serão: cor, número, planta, flor e maçaneta (nessa ordem)
→ Caso a cor seja acobreada E (o número da porta ímpar ou a maçaneta triangular ou quadrada) E a planta jiboia, Arisu ganhará 500 pontos

→ Caso a cor seja prateada E (a flor não é margarida, papoula ou cosmos) E (a maçaneta for hexagonal ou redonda), Arisu ganhará 450 pontos

→ Caso a cor seja dourada E (a flor ser lirio ou ixora) E a maçaneta ser hexagonal, Arisu ganhará 400 pontos

→ Caso nenhuma dessas condições seja contemplada, Arisu perderá 500 pontos

OBS: Atente aos parênteses, eles indicam a ordem em que as operações lógicas devem ser efetuadas

Output

Ao final do desafio você deverá imprimir a mensagem:

“ARISU, VOCÊ FEZ SUAS ESCOLHAS E AGORA VEREMOS SE ESCOLHEU AS PORTAS CERTAS:”

Você deverá imprimir a sequência de portas que ele escolheu, com CERTA para identificar a correta e ERRADA para identificar a errada, exemplo:

"CERTA ERRADA CERTA CERTA ERRADA”

Caso ele vença o desafio:

mas tenha escolhido alguma porta errada:
”Você passou com {pontuacao} pontos, mas faça melhores escolhas da próxima vez."

e se não tiver escolhido nenhuma porta errada:
"Parece que a sorte está ao seu favor, Arisu... Você conseguiu passar com {pontuacao} pontos!"

Caso perca:

mas tenha escolhido alguma porta certa:
"Por mais que você tenha feito escolhas corretas, não foi suficiente para sobreviver. Você finalizou o jogo com {pontuacao} pontos"

e se não tiver escolhido nenhuma porta certa:
"Todas suas escolhas foram erradas, Arisu, esperávamos mais de você... Você será executado pois obteve {pontuacao} pontos."

Sendo {pontuacao} a pontuação final conquistada por Arisu.

'''
