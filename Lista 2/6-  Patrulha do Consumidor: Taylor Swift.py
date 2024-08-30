numero_compradores = int(input())
total_suspeitos = 0

for i in range(numero_compradores):
  nome_comprador = input()
  cpf_comprador = input()
  nome_identidade = input()
  cpf_identidade = input()
  qtd_ingressos = int(input())
  preco_total_ingressos = float(input())
  codigo_compra = input()
  contador_criterios = 0

  if nome_comprador != nome_identidade:
    contador_criterios += 1

  if cpf_comprador != cpf_identidade:
    contador_criterios += 1

  if qtd_ingressos > 12:
    contador_criterios += 1

  if preco_total_ingressos > 1500:
    contador_criterios += 1
  digitos_impares = sum(1 for d in codigo_compra if int(d) % 2 != 0)

  if digitos_impares >= 7:
    contador_criterios += 1

  if contador_criterios >= 3:
    total_suspeitos += 1

print(f"Total de compradores analisados: {numero_compradores}")
print(f"Total de suspeitas de cambistas: {total_suspeitos}")

'''

Você faz parte da equipe de investigação liderada por Celso Russomano em 2023, que está empenhada em identificar cambistas que vendem ingressos a preços abusivos no show da Taylor Swift. Para ajudar na investigação, você foi encarregado de criar um programa em Python que analise informações detalhadas sobre compradores de ingressos e determine se eles se enquadram nos critérios de possíveis cambistas.

O código analisará cada comprador individualmente e contará o número de critérios que são atendidos. Se um comprador atender a pelo menos 3 critérios, ele é considerado um possível cambista. O resultado é exibido no final do programa, indicando quantos compradores são considerados possíveis cambistas com base nos critérios definidos no código.

Input

O programa começa recebendo o número total de compradores que serão analisados

numero_compradores (int)

Em seguida, para cada comprador, o programa solicita as seguintes informações:

nome_comprador (string)

cpf_comprador (string)

nome_identidade (string)

cpf_identidade (string)

qtd_ingressos (int)

preco_total_ingressos (float)

codigo_compra (string)

OBS.: Não será necessário uma verificação na estrutura do CPF e do CÓDIGO DE COMPRA, eles terão, em todos os casos, 11 dígitos e 15 dígitos.

Deverão ocorrer as seguintes verificações:

Nome do Comprador e Nome na Identidade:

O programa compara o nome do comprador (nome_comprador) com o nome encontrado na identidade (nome_identidade).
Se houver diferença entre os nomes (ou seja, se nome_comprador for diferente de nome_identidade), o contador_criterios é incrementado em 1.
Isso significa que o comprador não forneceu um nome consistente com o da identidade, o que é considerado um critério que pode sugerir que ele seja um possível cambista.
CPF do Comprador e CPF na Identidade:

O programa compara o CPF do comprador (cpf_comprador) com o CPF encontrado na identidade (cpf_identidade).
Se houver diferença nos CPFs (ou seja, se cpf_comprador for diferente de cpf_identidade), o contador_criterios é incrementado em 1.
Isso indica que o comprador forneceu um CPF que não corresponde ao registrado na identidade, o que é outro critério que pode sugerir que ele seja um possível cambista.
Quantidade de Ingressos:

O programa verifica a quantidade de ingressos comprados (qtd_ingressos).
Se a quantidade for maior do que 12, o contador_criterios é incrementado em 1.
Isso implica que o comprador comprou uma quantidade excessiva de ingressos, o que é um critério adicional para suspeitar que ele seja um possível cambista.
Preço Total dos Ingressos:

O programa verifica o preço total pago pelos ingressos (preco_total_ingressos).
Se o preço total for maior do que R$ 1500, o contador_criterios é incrementado em 1.
Isso sugere que o comprador gastou uma quantia considerável de dinheiro na compra dos ingressos, o que é outro critério que pode levantar suspeitas sobre sua atividade.
Código de Compra e Números Ímpares:

O programa coleta o código de compra, que é uma sequência de 15 números.
O programa deve percorrer cada dígito no código de compra e verificar se o dígito é ímpar.
OBS.: Caso não saiba, deve pesquisar como percorre cada item em uma string de caracteres (Não é difícil, mas peço isso para incentivar a pesquisa para implementação de código, que ocorre muito no mercado de trabalho).
Após analisar todos os dígitos, o programa verifica se a quantidade de dígitos ímpares é maior ou igual a 7. Se for, o contador_criterios é incrementado em 1.
Isso significa que se houver pelo menos 7 dígitos ímpares no código de compra, a conta do comprador não é verificada.
No final, o programa determina se o comprador é um possível cambista com base no valor do contador_criterios. Se contador_criterios for maior ou igual a 3, o suspeito é considerado um possível cambista, caso contrário, ele é inocentado.

Output

O programa fornecerá a seguinte saída:

Total de compradores analisados: {x}

Total de suspeitas de cambistas: {y}

Em que as variáveis x e y correspondem a numero_compradores e a total_suspeitos, respectivamente.

'''
