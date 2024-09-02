itens_desejados = input().split(', ')
itens_encontrados = input().split(', ')
n_itens_desejados = 0
n_itens_encontrados = 0
itens_comuns = []
n_itens_compra = 0
compras = []

for i in itens_desejados:
  if i in itens_encontrados:
    itens_comuns.append(i)
    n_itens_encontrados += 1

  else:
    n_itens_desejados += 1

if n_itens_encontrados == 0:
  print(f"Hmm, preciso visitar um vendedor ambulante! Não encontrei nenhum dos {n_itens_desejados} itens aqui no Acampamento Meio-Sangue.")

else:
  print("Estes são os itens que já tenho no Acampamento Meio-Sangue:")

  for j in range(1, len(itens_comuns) + 1):
    k = itens_comuns[j - 1]
    print(f"{j}º item: {k}")

for l in itens_desejados:
  if l not in itens_encontrados:
    compras.append(l)
    n_itens_compra += 1

if (n_itens_compra) != 0 and len(compras) < len(itens_desejados):
  print(f"Vou precisar adquirir {n_itens_compra} itens antes da batalha!")

elif (n_itens_compra) == 0:
  print(f"Perfeito, encontrei todos os {n_itens_encontrados} itens aqui no Acampamento Meio-Sangue!")

print("Estou pronto para a batalha! Que comece a guerra contra os Titãs!")

'''

Percy Jackson está se preparando para a batalha decisiva contra os Titãs e precisa de sua ajuda para garantir que tudo esteja em ordem. Para isso, ele fez uma lista de itens essenciais que deseja levar para o campo de batalha para garantir a vitória.

Percy Jackson, então, irá vasculhar o Acampamento Meio-Sangue, anotando tudo o que encontrar, mesmo os itens que ele não planeje levar para a batalha. Ajude Percy a determinar quais itens da sua lista ele já possui e quais ele precisará adquirir para vencer essa batalha!

Input

Inicialmente, Percy irá informar a lista de itens que deseja levar para a batalha, separados por uma vírgula e um espaço, na mesma linha:

item1, item2, item3, item4, …, item n

Depois, ele irá dizer os itens encontrou no Acampamento Meio-Sangue no mesmo formato descrito acima. Lembre-se de que nem todos os itens que Percy encontrar no acampamento estarão em sua lista de desejos para a batalha.

item1, item2, item3, item4, …, item n

Obs1: Utilize split() para tratar as entradas.

Obs2: Todos os itens listados são únicos, não havendo nenhuma repetição.

Obs3: Sempre haverá itens tanto na lista de Percy Jackson quanto encontrados no Acampamento Meio-Sangue.

Output

Como saída, a princípio, Percy quer que você imprima os itens da sua lista de desejos que ele de fato conseguiu encontrar no acampamento, no seguinte formato:

"Estes são os itens que já tenho no Acampamento Meio-Sangue:"

"1º item: {nome_item1}"

"2º item: {nome_item2}"

"3º item: {nome_item3}"

"4º item: {nome_item4}"

OBS.: Os itens devem ser impressos na mesma ordem em que Percy os listou como desejados.

Porém, caso Percy não encontre nenhum item da lista no Acampamento Meio-Sangue, ao invés de realizar a listagem acima, ele deve dizer:

"Hmm, preciso visitar um vendedor ambulante! Não encontrei nenhum dos {quantidade_de_itens_da_lista_de_desejo} itens aqui no Acampamento Meio-Sangue."

Além disso, caso Percy tenha encontrado algum item da lista no acampamento, ele quer saber quantos itens ainda precisará adquirir para a batalha. Itens que Percy precisa comprar são os itens da lista de desejos que ele não encontrou no acampamento.

Caso ele tenha itens a comprar, ele deve dizer:
"Vou precisar adquirir {quantidade_de_itens_não_encontrados} itens antes da batalha!"

Caso ele tenha encontrado todos os itens no acampamento, ele deve dizer:
"Perfeito, encontrei todos os {quantidade_de_itens_da_lista_de_desejo} itens aqui no Acampamento Meio-Sangue!"

E então finalizar com a mensagem:

"Estou pronto para a batalha! Que comece a guerra contra os Titãs!"

'''
