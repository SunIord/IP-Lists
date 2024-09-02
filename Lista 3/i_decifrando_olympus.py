codigo = input()
mensagem_decifrada = ""
tamanho_total = len(codigo)
ignorar_espacos = False
louco = False

for i in codigo:
  if i != " ":
    valor_decimal = ord(i)
    valor_somado = valor_decimal + tamanho_total

    if ord('0') <= valor_somado <= ord('9') and louco == False:
      print("Algo de errado não está certo. Será que estou ficando doido?")
      louco = True
    
    caractere_decifrado = chr(valor_somado)
    mensagem_decifrada += caractere_decifrado
    ignorar_espacos = False

  elif not ignorar_espacos:
    mensagem_decifrada += " "
    ignorar_espacos = True  

if louco == False:
  if mensagem_decifrada.strip() == "":
    print("Ué não tem nada para me decifrar aqui")
  else:
    print(f"Descobri o que a mensagem significa: {mensagem_decifrada}")

'''

Percy Jackson sempre foi o garoto apagado da escola, e isso parecia normal. Um dia, em uma visita ao museu, Percy descobre que sua dislexia parece ser “anulada” e lá, ele consegue ler tudo que está escrito em grego antigo, como se falasse a língua desde sempre. Porém, ao tentar ler e decifrar o grego antigo em seu celular ou computador houve uma dificuldade em entender como a escrita funcionava.

Ao perceber que o computador interpreta bits em números e números em letras através de uma tabela de representação (ASCII), ele chamou você para ajudar-lo a decifrar essas mensagens.

OBS: Para melhor entendimento da questão pesquisar sobre Tabela ASCII

ATENÇÃO: Utilizar listas e as funções ord() e chr() para resolver a questão

Input

O input será uma única string que você terá que decifrar para ajudar Percy a descobrir a mensagem e para isso, deverá seguir os seguintes passos, individualmente, com cada um dos caracteres da string recebida:

Primeiro: você deverá descobrir o valor decimal associado àquele caractere na tabela ASCII
Segundo: esse valor decimal deverá ser somado com o valor total do tamanho da string
Terceiro: esse valor encontrado deverá ser usado para descobrir o caractere da tabela ASCII associado a ele
Quarto: decifrado esse caractere, ele deverá ser armazenado para formar parte da string final
Exemplo:

No case exemplo 1, o caractere ' está associado ao número 39 na tabela ASCII, esse número somado ao tamanho total da string ' SKJ[YG KYZÇ TU 2GHOXOTZU que é 26, resulta no número 65 que por sua vez está associado ao caractere A na tabela ASCII
Seguindo os mesmos passos com o caractere S temos: S → 83 + 26 → 109 → m
OBS: Os espaços em branco " " não devem passar por esse procedimento, eles deverão ser adicionados à mensagem final

como " ".

Output

Ao decifrar toda a mensagem você deverá imprimir:

"Descobri o que a mensagem significa: {mensagem_decifrada}"

Caso a mensagem seja um espaço vazio (" "), você deverá imprimir:

"Ué não tem nada para me decifrar aqui"

Caso na mensagem já decifrada haja pelo menos 1 algarismo, Percy não irá entender e você deverá imprimir apenas:

"Algo de errado não está certo. Será que estou ficando doido?"

'''
