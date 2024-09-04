def distancia_euclidiana(x1, y1, x2, y2):
  return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def cifra_cesar(palavra, numero_de_posicoes, direcao):
  alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  resultado = ''

  for letra in palavra:
    if 'A' <= letra <= 'Z':
      indice = ord(letra) - ord('A')

      if direcao == 'R':
        novo_indice = (indice + numero_de_posicoes) % 26
      
      elif direcao == 'L':
        novo_indice = (indice - numero_de_posicoes) % 26

      resultado += chr(ord('A') + novo_indice)

    else:
      resultado += letra

  return resultado

def encontrar_caminho_mais_curto(x_noel, y_noel, info_cidade, caminho = []):
  distancia_sem_ordem = []
  distancia_com_ordem = []
  
  for coordenada_cidade in info_cidade:
    distancia = distancia_euclidiana(x_noel, y_noel, float(coordenada_cidade[1]), float(coordenada_cidade[2]))
    
    if (distancia != 0) and (coordenada_cidade[0] not in caminho):
      distancia_sem_ordem.append(distancia)
    else:
      distancia_sem_ordem.append(2834678.1)
    
  distancia_com_ordem = sorted(distancia_sem_ordem)
  cidade_mais_perto_index = distancia_sem_ordem.index(distancia_com_ordem[0])
  
  return cidade_mais_perto_index


def caminho_certo(info_cidade):
  caminho = []
  cidade_mais_perto_index = encontrar_caminho_mais_curto(0,0, info_cidade)

  for i in range(len(info_cidade)):
    caminho.append(info_cidade[cidade_mais_perto_index][0])
    x_cidade_proxima = float(info_cidade[cidade_mais_perto_index][1])
    y_cidade_proxima = float(info_cidade[cidade_mais_perto_index][2])
    cidade_mais_perto_index = encontrar_caminho_mais_curto(x_cidade_proxima, y_cidade_proxima, info_cidade, caminho)

  return caminho   

qtd_cidades = int(input())
lista_senhas = []
info_cidade = [] 
distancia_sem_ordem = []
distancia_com_ordem = []
lista_nomes_cidades = []

for i in range(qtd_cidades):
  informacoes = input().split(', ')
  
  if len(informacoes) != 0 and informacoes != [' ']:
    info_cidade.append(informacoes)
    senha = cifra_cesar(informacoes[3], int(informacoes[-2]), informacoes[-1]) 
    lista_senhas.append(senha)
    lista_nomes_cidades.append(info_cidade[i][0])

trajetoria = caminho_certo(info_cidade)

for n in range(len(trajetoria)):
  idx = lista_nomes_cidades.index(trajetoria[n])
  print(f'A senha da cidade {info_cidade[idx][0]} é: {lista_senhas[idx].upper()}') 
  
'''

À medida que mais um fim de ano se aproxima, o Papai Noel está entusiasmado para realizar todas as entregas de presentes no Natal. Contudo, uma surpresa inesperada o aguarda: Grinch. Decidido a causar transtornos, Grinch planeja atrapalhar as entregas instalando fechaduras com senha nas chaminés de algumas cidades, na tentativa de impedir que o Papai Noel faça suas descidas tradicionais.

Diante desse desafio, o Papai Noel embarca em uma missão crucial para resgatar o espírito natalino, decifrando os enigmas de Grinch e assegurando que cada pessoa receberá os presentes que merece.

Para complicar a vida do Papai Noel, Grinch aplicou uma estratégia astuta ao criptografar a entrada das chaminés: optou por usar a cifra de César. Essa técnica envolve essencialmente avançar ou retroceder uma determinada quantidade de letras no alfabeto para cifrar e decifrar mensagens.

Exemplos:

Ao avançar 3 letras no alfabeto, para cada uma das letras de "NOITE", ela se torna "QRLWH".
Retrocedendo 4 letras no alfabeto, "NATAL" se torna "JWPWH".
OBS. 1: Quando a cifra atinge as extremidades do alfabeto, a contagem continua, significando que após "Z" a próxima letra será "A" e vice-versa ("A" retrocede para "Z").

Além disso, para otimizar o percurso que realizará ao visitar as cidades sabotadas por Grinch, Papai Noel sempre visitará a próxima cidade mais perto da cidade atual em que se encontra. Portanto, imagine o bom velhinho em um plano cartesiano, começando no ponto (0, 0). Sua missão consiste em determinar qual cidade está mais próxima do ponto atual em que se encontra, a fim de seguir em direção a ela. Para isso, use a fórmula da distância euclidiana mostrada abaixo e ao chegar a uma cidade, suas coordenadas serão equivalentes às da cidade que está sendo visitada naquele momento.

OBS. 2: Se houver mais de uma cidade com a mesma distância, a escolha será determinada pela ordem de listagem das cidades no input da questão, optando pela primeira cidade nessa ordem.

Importante!!

Você deve criar pelo menos essas 2 funções para resolver essa questão:

Função para calcular a distância euclidiana
Função para a cifra de César
Input

Em primeiro lugar, o programa irá ler a quantidade de cidades sabotadas que o Papai Noel está prestes a visitar:

quantidade_de_cidades

Após isso, para cada cidade, deve-se ler as suas respectivas informações seguindo o padrão (separados por vírgula e um espaço):

nome, x, y, palavra_criptografada, numero_de_posicoes, direcao

Onde:

nome: Nome da cidade - string
x, y: Coordenadas da cidade - float
palavra_criptografada: Palavra a ser descriptografada (sempre em maiúsculo e sem acento ou cedilha) - string
numero_de_posicoes: Número de letras a serem avançadas ou retrocedidas - int
direcao: Define se para descriptografar deverá avançar ou retroceder no alfabeto. São aceitas apenas duas opções de string (em maiusculo):
“R”: Para avançar letras (right)
“L”: Para retroceder letras (left)
Output

O programa deverá exibir todas as cidades com suas respectivas senhas descriptografadas, mostradas de acordo com a ordem de visitação do Papai Noel.

A senha da cidade {nome} é: {palavra_descriptografada}

Em que, {nome} refere-se ao nome da cidade que está sendo visitada e {palavra_descriptografada} é a palavra criptografada recebida depois de ter sido aplicada a ela a função que decifra a cifra de César.

'''
