def organizar_malas(lista_pesos_malas):
  pesos = [int(peso) for peso in lista_pesos_malas]
  pesos.sort()
  pesos[0], pesos[-1] = pesos[-1], pesos[0]
  pesos[1], pesos[-2] = pesos[-2], pesos[1]
  return pesos

def parametros(qtd_blocos_carvao, peso, num_de_passageiros):
  velocidade = (qtd_blocos_carvao + 200) // 2
  carga = (peso + 4000) // 1000
  passageiros = num_de_passageiros + 40
  return velocidade, carga, passageiros

def turno(horario, roteiro, lista_funcionarios):
  hora_partida = int(horario.split(":")[0])
  if 7 <= hora_partida < 21:
    if roteiro == "Roteiro 1":
      convocados = lista_funcionarios[:2]
    
    elif roteiro == "Roteiro 2":
      convocados = [lista_funcionarios[0], lista_funcionarios[-1]]
  
  elif 21 <= hora_partida <= 23 or 0 <= hora_partida < 7:
    if roteiro == "Roteiro 1":
      convocados = [lista_funcionarios[2]]
    
    elif roteiro == "Roteiro 2":
      convocados = []
  
  else:
    convocados = []
  return convocados

def protocolo_de_inicio(lista_pesos_malas, parametros_input, lista_funcionarios, horario, roteiro):
  malas_organizadas = organizar_malas(lista_pesos_malas)
  print(f"A nova organização das malas é a seguinte: {', '.join(map(str, malas_organizadas))}")
  velocidade, carga, passageiros = parametros(*parametros_input)
  print(f"A velocidade que o trem partirá é de: {velocidade}Km/H")
  print(f"A carga do Trem em Toneladas é: {carga} Ton.")
  print(f"A quantidade de passageiros é de {passageiros}")
  convocados = turno(horario, roteiro, lista_funcionarios)
  
  if convocados:
    print(f"Os funcionários convocados são: {', '.join(convocados)}")
  
  else:
    print("Os funcionários convocados são: Nenhum! O turno da Madrugada vai ser tranquilo para todos")

lista_pesos_malas = input().split(", ")
parametros_input = [int(x) for x in input().split(", ")]
lista_funcionarios = input().split(", ")
horario = input()
roteiro = input()

protocolo_de_inicio(lista_pesos_malas, parametros_input, lista_funcionarios, horario, roteiro)

'''

É tempo de natal! E o Trem Mágico, com destino a Hogwarts, precisa da ajuda das suas habilidades para sair a tempo e preparado!

Seu código deverá ter no mínimo 4 funções, que serão executadas pelo condutor ao início da viagem. Caberá a ele somente executar a função protocolo_de_Inicio, e essa executará as outras 3, que estão descritas abaixo.

-> A função de organizar malas deverá ocorrer sob a seguinte lógica:

Recebe uma lista de Strings com os pesos de cada uma das malas, ordena elas em ordem crescente. Após isso, troca de lugar a mais leve com a mais pesada, e a segunda mais leve com a segunda mais pesada, afim de equilibrar melhor o peso! A função então retorna a lista organizada como descrito.
-> A função de parâmetros, recebe três argumentos (quantidade de blocos de carvão, peso e número de passageiros). Retorna também três: a velocidade, a carga total do trem, e a quantidade de pessoas que estarão naquela viagem.

A velocidade será calculada a partir da quantidade de blocos de carvão que lhe forem passadas, adicionado a 200, e então dividido por dois (Deve retornar um inteiro, não float)
A carga será contabilizada pelos quilos repassados a você, somados a 4000 e divididos por 1000, afim de retornar esse valor em toneladas. (Igualmente inteiro, não float)
O total de pessoas, será o número passado, somado a 40, para contabilizar os funcionários presentes (mesmo que não estejam oficialmente trabalhando).
-> A função de Turno recebe três argumentos (a hora da viagem, o número do roteiro, e uma lista de funcionários), analisa tais dados e retorna somente uma string (ou lista, como você preferir), com os convocados para o dado turno que o trem iniciará sua viagem.

Caso a hora de partida seja seja entre 7 e 21, e o roteiro seja o 1, os convocados serão o primeiro e segundo da lista de funcionários passada, e se for o roteiro 2, os convocados serão o primeiro, e o último.
Caso a hora seja maior ou igual a 21 e menor ou igual a 7, e o roteiro seja o 1, o convocado será somente o terceiro da lista, e caso seja o roteiro 2, ninguém será convocado.
train

Por fim, como mencionado, você deverá ter também a função que irá organizar e convocar esses protocolos, procurando diminuir o trabalho do Condutor.

Input

Incialmente, você receberá uma lista que corresponde aos pesos das malas, onde cada elemento está dividido por uma vírgula e um espaço (", ").

{lista_pesos_malas}

Depois, você receberá uma lista com os 3 valores necessários para excecutar a função dos parâmetros:

{qtd_blocos_carvao, peso, num_de_passageiros}

Em seguida, você receberá uma lista de funcionários, o horário de partida e o número do roteiro:

{lista_funcionarios}

horario (string)

roteiro

OBS. 1: A lista de funcionários terá cada elemento dividido por uma vírgula e um espaço (", ").

OBS. 2: O roteiro será entregue como: “Roteiro 1” ou “Roteiro 2”.

OBS. 3: O horário será entregue como: xz:yw, onde x, y, z e w são números inteiros.

Output

A medida que o programa for sendo processado, você deve printar os resultados na seguinte ordem:

O output referente a função de malas deve ser no formato:
"A nova organização das malas é a seguinte: {Lista com valores separados por ", "}"

O output referente a função de parâmetros, deve conter 3 linhas e vir da seguinte maneira:
"A velocidade que o trem partirá é de: {velocidade}Km/H"

"A carga do Trem em Toneladas é: {carga} Ton."

"A quantidade de passageiros é de {passageiros}"

Por fim, o output referente a função de turno deve ser:
Caso tenha sido convocado funcionários:

"Os funcionários convocados são: {Lista de convocados, separados por ", "}"

Caso ninguém tenha sido convocado a trabalhar:

"Os funcionários convocados são: Nenhum! O turno da Madrugada vai ser tranquilo para todos"

Dica: É sugerido que vocês estudem a função (list(map)) em Python, para alternar listas entre variáveis strings e inteiras, como no caso da função de organizar malas.

Programe com cuidado para que todos em Hogwarts tenha um natal tão mágico quanto seu código!

'''
