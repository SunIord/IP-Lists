computadores_disponiveis = int(input())
dinheiro_disponivel = float(input())
tempo_espera_limite = int(input())
n_amigos = 0
lista = True

while(lista):
  amigo = input()
  
  if(amigo == "end"):
    lista = False
  
  elif(amigo != "laura" and amigo != "carlos" and amigo != "roberto"):
    n_amigos += 1
  
    if(n_amigos >= computadores_disponiveis):
      lista = False

ingressos = 0
tem_ingresso = False

if(n_amigos > 0):
  print(f"Bom começo! Consegui {n_amigos} amigos que podem me ajudar a comprar o ingresso")
  
  for amigo in range(1, n_amigos+1):
    amigo_ajudando = True
  
    while (amigo_ajudando):
      valor_do_ingresso = float(input())
      local_do_show = input()
  
      if(local_do_show == "end"):
        amigo_ajudando = False
  
      elif(local_do_show == "rio de janeiro" or local_do_show == "são paulo" or local_do_show == "buenos aires"):
        print("Consegui um ingresso em um local que João possa ir! Agora temos que ver o preço")
        amigo_ajudando = False
  
        if(valor_do_ingresso <= dinheiro_disponivel):
          print("Consegui o dinheiro! Agora só falta ver a minha colocação na fila dos ingressos...")
          posicao_fila = int(input())
  
          if(posicao_fila <= tempo_espera_limite*6*16):
            print("ISSOOO, conseguimos um ingresso!!!")
            ingressos += 1
  
            if(not tem_ingresso):
              tem_ingresso = True
              computador_escolhido = amigo
              posicao_escolhida = posicao_fila
  
            else:
  
                if(posicao_fila < posicao_escolhida):
                  computador_escolhido = amigo
                  posicao_escolhida = posicao_fila 
  
          else:
            print(f"Caramba, essa foi quase! Mas infelizmente não consegui um bom lugar na fila dos ingressos no computador de número {amigo}")
  
        else:
          print("Caramba! Só tinha ingresso para a pista vip, que está bem acima do meu orçamento.")
  
  if(tem_ingresso):
    print(f"Consegui o ingresso! Com {int((ingressos/n_amigos)*100)}% de aproveitamento da ajuda dos meus amigos. E a fila escolhida para comprar o ingresso foi do computador número {computador_escolhido}. Rumo ao show da Taylor!!!")
  
  elif(not tem_ingresso and n_amigos >= computadores_disponiveis/2):
    print("Não acredito que tive amigos para ocuparem mais da metade dos computadores, e ainda assim não consegui um ingresso...")
  
  else:
    print("Poxa, não acredito que não consegui o ingresso, acho que eu devia ter chamado mais amigos para ajudar.")

else:
  print("Ah não! João não conseguiu nenhum amigo que o ajudasse. Agora ele vai ter que contar com a sorte para pegar um bom lugar na fila, usando apenas seu computador.")
  
'''

João, um aluno do cin que é fã da taylor, precisa a todo custo conseguir o ingresso para o show "the eras tour". Porém, no dia da abertura de vendas dos ingressos, vão ter muitas pessoas entrando ao mesmo tempo e cada uma ficará em uma posição da fila. Sendo assim, João precisa conseguir o máximo de computadores que puder, e que lugar melhor do que um grad no cin? Além disso, ele precisa de amigos que o ajudem, pois cada um vai ocupar um computador para tentar conseguir o ingresso.

Você desenvolverá um algoritmo que escolha os amigos certos para ajudar João. Sendo assim, você não deverá aceitar esses nomes:

"laura", "carlos", e "roberto"

Pois eles não são tão próximos de João, e também não gostam da Taylor Swift. Então podem acabar sabotando o plano, ou desistindo de ajudar.

Logo depois, o algoritmo vai pegar o conteúdo de cada computador, e analisar os ingressos disponíveis em cada um deles, e verificar se João conseguirá comprar aquele ingresso.

Para que ele consiga comprar, há algumas condições:

O local do show que consta no ingresso tem que ser um desses três:
"rio de janeiro", "são paulo" ou "buenos aires"

O valor do ingresso tem que ser menor ou igual ao valor disponível na carteira de João
E eles têm tempo limitado no grad, então o tempo na fila não pode ser tão grande a ponto de o fazerem ultrapassar o tempo limite da sala.
Se mais de um amigo de João tiver encontrado um ingresso dentro das condições impostas, o que tiver em uma posição mais avançada da fila do ingresso, é o escolhido.

OBS.1: A cada 10 minutos, é avançada 16 posições da fila dos ingressos.

OBS.2: PROIBIDO O USO DE LISTAS.

Input

Primeiramente, você receberá 3 inputs:

1°- O número de computadores disponíveis no grad:

computadores_disponiveis

2°- O dinheiro disponível que João tem para comprar o ingresso:

dinheiro_disponivel

3°- Um número inteiro que representa o tempo limite que poderão ficar no grad (em horas):

tempo_espera_limite

Depois, você começará a receber os nomes dos amigos, cada um em uma linha:

nome

Você deve continuar recebendo os nomes, até que "nome" seja igual a "end", ou até que tenha ocupado todos os computadores. (Lembrando que os nomes "laura", "carlos", e "roberto", não serão aceitos).

OBS.3: Poderá ter mais computadores disponíveis do que computadores utilizados. Os utilizados por João vão depender da quantidade de amigos que ele conseguiu para ajudar.

OBS.3.1: Os computadores serão identificados por uma numeração que vai de 1 até a quantidade de computadores disponíveis (Qtd_CD). Além disso, cada amigo será alocado ao próximo computador livre, iniciando do computador 1. Por exemplo, 1º amigo a ser aceito -> computador 1; 2º amigo a ser aceito -> computador 2; ... n-ésimo amigo a ser aceito -> computador n; sendo n <= Qtd_CD.

Após isso, você deve analisar a quantidade de amigos que João encontrou.

Se Jõao não tiver conseguido nenhum amigo para o ajudar, você não receberá mais nenhum input, printará uma mensagem e o programa deverá encerrar.

Caso Contrário, você receberá, para cada computador sendo utilizado por um dos amigos de João, várias duplas de entrada. Onde, a primeira se refere ao valor do ingresso e a segunda ao local do show. Isso ocorrerá até que você ache um ingresso em um dos locais que João pode ir ou desista de comprar o ingresso. O caso de desistir do ingresso será identificado recebendo a entrada "end".

valor_do_ingresso

local_do_show

OBS.4: Mesmo recebendo a entrada "end", você ainda vai receber um valor qualquer no input do valor do ingresso e significa que apenas aquele amigo desistiu do ingresso, mas ainda podem ter outros tentando.

Se João conseguiu um local que ele possa ir e se o valor do ingresso é menor ou igual ao dinheiro que ele tem disponível, você irá receber o número que representa a posição na fila da compra do ingresso:

posicao_fila

Caso o tempo de espera, a partir da posição da fila em que se encontra, seja menor ou igual ao tempo de espera limite do grad, você deverá contabilizar essa possibilidade de ingresso e guardar as informações necessárias (incluindo se esse é o primeiro, segundo, ... computador analisado) para descobrir, ao final, qual ingresso deverá ser comprado e qual computador foi utilizado.

Output

Se João não conseguiu nenhum amigo que possa o ajudar, você deverá printar:

"Ah não! João não conseguiu nenhum amigo que o ajudasse. Agora ele vai ter que contar com a sorte para pegar um bom lugar na fila, usando apenas seu computador."

E com isso, encerra-se o programa.

Caso contrário: se conseguiu 1 ou mais amigos:

"Bom começo! Consegui {n_amigos} amigos que podem me ajudar a comprar o ingresso"

Ao conseguir amigos, o algoritmo parte para a busca dos lugares.

Sempre que conseguir um lugar em que possa ir, printe:

"Consegui um ingresso em um local que João possa ir! Agora temos que ver o preço"

Em seguida, após ter conseguido o lugar, ele verifica o valor do ingresso. Se o dinheiro disponível por João for maior ou igual ao valor do ingresso, printe:

"Consegui o dinheiro! Agora só falta ver a minha colocação na fila dos ingressos..."

Caso contrário, printe:

"Caramba! Só tinha ingresso para a pista vip, que está bem acima do meu orçamento."

Ao analisar o input P (posição da fila), se o tempo de demora na fila estiver dentro do limite de permanência no grad, printe:

"ISSOOO, conseguimos um ingresso!!!"

E se a demora for maior que o tempo limite, você deverá printar:

"Caramba, essa foi quase! Mas infelizmente não consegui um bom lugar na fila dos ingressos no computador de número {x}"

E por fim, quando já tiver analisado todos os computadores:

Caso tenha conseguido uma ou mais opções de ingressos viáveis, printe:

"Consegui o ingresso! Com {int((opcoes_ingressos/n_amigos)*100)}% de aproveitamento da ajuda dos meus amigos. E a fila escolhida para comprar o ingresso foi do computador número {computador_escolhido}. Rumo ao show da Taylor!!!"

Se não tiver conseguido nenhuma possibilidade de ingresso para comprar, e o número de computadores em uso era mais da metade dos disponíveis no grad, printe:
"Não acredito que tive amigos para ocuparem mais da metade dos computadores, e ainda assim não consegui um ingresso..."

Se não tiver conseguido nenhuma possibilidade de ingresso para comprar, mas o número de computadores em uso era menor ou igual que a metade dos disponíveis no grad, printe:
"Poxa, não acredito que não consegui o ingresso, acho que eu devia ter chamado mais amigos para ajudar."

OBS.5: esse "aproveitamento" é a razão entre o número de opções de ingressos válidos que os amigos de João conseguiram para ele, sobre o número total de amigos que o estavam ajudando multiplicado por 100.

OBS.6: Printe a porcentagem de aproveitamento como um inteiro, sem casas decimais.

'''
