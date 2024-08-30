numero = int(input())

if numero == 1:
  string_1 = input()
  string_2 = input()
  string_3 = input()

  if len(string_1) > len(string_2) and len(string_1) > len(string_3):
    print(string_1)
    print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

  elif len(string_2) > len(string_1) and len(string_2) > len(string_3):
    print(string_2)
    print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

  elif len(string_3) > len(string_1) and len(string_3) > len(string_2):
    print(string_3)
    print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

  else:
    print("(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)")

    if string_1 > string_2 and string_1 > string_3:
      print(string_1)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

    elif string_2 > string_1 and string_2 > string_3:
      print(string_2)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

    elif string_3 > string_1 and string_3 > string_2:
      print(string_3)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
  
    else:
      print('"AAAAAA! Um fantasma me assustou!"')
      print('(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")')

elif numero == 2:
  string_1 = input()
  string_2 = input()
  string_3 = input()

  if len(string_1) < len(string_2) and len(string_1) < len(string_3):
    print(string_1)
    print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

  elif len(string_2) < len(string_1) and len(string_2) < len(string_3):
    print(string_2)
    print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

  elif len(string_3) < len(string_1) and len(string_3) < len(string_2):
    print(string_3)
    print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

  else:
    print("(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)")

    if string_1 > string_2 and string_1 > string_3:
      print(string_1)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

    elif string_2 > string_1 and string_2 > string_3:
      print(string_2)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

    elif string_3 > string_1 and string_3 > string_2:
      print(string_3)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

    else:
      print('"AAAAAA! Um fantasma me assustou!"')
      print('(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")')

else:
  print(" ")
print("(Depois de ler a mensagem, você dormiu. Ao acordar, você não estava mais no CIn de outubro de 2012, mas no CIn de 2023, sem acreditar na situação que vivenciou)")

'''

Eventos estranhos estão ocorrendo nesse Halloween e você também foi afetado por eles. Um belo dia, você resolveu ficar estudando em um dos grads do CIn, mas acabou adormecendo por conta do cansaço. Estranhamente, quando acordou, você não estava em 2023, mas no CIn de outubro de 2012! Nesse período, existia um jogo chamado Club Penguin e, nele, a festa de Halloween estava acontecendo.

Ainda sem entender direito, você percebeu que havia um bilhete no grad onde adormeceu. Nesse bilhete, estava escrito “Ligue o monitor para realizar o teste”. Depois de ligar, você viu um teste... para tentar virar um agente da EPF? Apesar de não estar entendendo direito a situação, você fez o que foi pedido. Depois, na tela do monitor, apareceu uma mensagem dizendo:

“Parabéns, você agora é agente da EPF (elite Penguin Force). Nós não temos tempo para explicar tudo, mas precisamos da sua ajuda e das suas habilidades de programação. Recentemente, detectamos sinais de atividades não identificadas na Mansão Mal-Assombrada. Precisamos que você vá até a mansão e descubra qual é o ambiente que possui mais sinais desconhecidos, entre os 3 que serão fornecidos. As instruções que explicam como encontrar essa resposta também serão fornecidas. Mas, cuidado, se você não descobrir a tempo, um fantasma pode te assustar. É Halloween!”.

OBS 1: Agente, você não poderá utilizar qualquer função de ordenação no seu código. Além disso, é recomendável pesquisar sobre a função len().

Input

Inicialmente, você receberá um número inteiro que pode ser 1 ou 2. Esse número dirá o que você deve fazer com as strings que receberá:

numero

Depois, você receberá 3 strings seguidas. Cada string é um nome de um local da mansão assombrada:

string_1

string_2

string_3

Output

Se você tiver recebido o número 1 inicialmente, você deve printar a string com mais letras, entre as strings recebidas. Ela corresponde ao local com mais sinais desconhecidos:
string_mais_letras

Se você tiver recebido o número 2 inicialmente, você deve printar a string com menos letras, entre as strings recebidas. Ela corresponde ao local com mais sinais desconhecidos:
string_menos_letras

Porém, se não for possível descobrir a string com mais ou menos letras (houver um empate na quantidade de caracteres), você deve printar:
(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)

Caso a situação citada logo acima ocorra, para descobrir o local com mais sinais desconhecidos é necessário que você descubra a string lexicograficamente maior das 3 strings recebidas. Se for possível encontrá-la, printe-a:

string_lexicograficamente_maior

OBS 2: Agente, ordem lexicográfica é igual à ordem alfabética. Quando digo que estamos buscando a string lexicograficamente maior, isso significa que estamos buscando a string que se encontra mais perto do fim do dicionário. Em Python, você pode usar > e < para encontrá-la.

No entanto, se não for possível descobrir, printe:

"AAAAAA! Um fantasma me assustou!"

(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")

Caso você descubra o local com mais sinais desconhecidos, você deve exibir o seguinte print:
(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")

No fim, sempre printe:
(Depois de ler a mensagem, você dormiu. Ao acordar, você não estava mais no CIn de outubro de 2012, mas no CIn de 2023, sem acreditar na situação que vivenciou)

'''
