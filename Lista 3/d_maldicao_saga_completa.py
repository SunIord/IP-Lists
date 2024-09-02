livros_saga = ["O Ladrão de Raios",
"O Mar de Monstros",
"A Maldição do Titã",
"A Batalha do Labirinto",
"O Último Olimpiano"]

colecao_sergio = input().split(', ')
qtd_total_edicoes = int(input())
colecao = 0
livros_faltando = []
outros_livros = []

for livros in livros_saga:
  if livros in colecao_sergio:
    colecao += 1
  else:
    livros_faltando.append(livros)

for livro in colecao_sergio:
  if livro not in livros_saga:
    outros_livros.append(livro)
  
if colecao == 5 and colecao:
  print("Sua coleção está completa! Você pode ler à vontade.")

elif 0 < colecao < 5:
  print(f"Infelizmente, sua coleção está incompleta. Falta(m) esse(s) livro(s): {', '.join(livros_faltando)}.")

elif colecao == 0:
  print("Caramba, você não tem nenhum livro. Compre todos imediatamente.")
  
if outros_livros and outros_livros != ['']:
  print(f'Cuidado, Sérgio! Você está organizando seus livros de uma forma errada, o(s) livro(s): {", ".join(outros_livros)}, não faz(em) parte da saga "Percy Jackson e os Olimpianos".')
  
'''

Sérgio Soares está muito ansioso para a nova série que será lançada chamada 'Percy Jackson e os Olimpianos'. Com isso, ele deseja ler todos os livros da saga 'Percy Jackson e os Olimpianos' para comparar com a nova série. No entanto, ele não tem certeza se possui todos os livros necessários, mas está disposto a comprar o restante.

Portanto, seu papel é ajudar Sérgio a identificar quais livros faltam para que ele complete a coleção.

Os livros da saga são:

O Ladrão de Raios
O Mar de Monstros
A Maldição do Titã
A Batalha do Labirinto
O Último Olimpiano
Input

Seu programa receberá apenas duas entradas: a coleção atual de Sérgio, que será entregue com os elementos separados por vírgulas, e a quantidade total de edições que ele tem:

colecao_sergio (string )

qtd_total_edicoes (inteiro )

OBS 1: Lembre-se que Sérgio pode nem ter começado a colecionar, isto é, coleção atual está vazia.

OBS 2: Sem querer, Sérgio pode lhe informar um nome de livro que seja de outra saga do universo Percy Jackson. Portanto, não se esqueça de verificar.

Output

Caso a coleção já esteja completa:
"Sua coleção está completa! Você pode ler à vontade."

Caso falte algum livro:
"Infelizmente, sua coleção está incompleta. Falta(m) esse(s) livro(s): {livros_faltando}."

Caso faltem todos os livros:
"Caramba, você não tem nenhum livro. Compre todos imediatamente."

Caso algum livro de outra saga do universo esteja na coleção de Sérgio:
"Cuidado, Sérgio! Você está organizando seus livros de uma forma errada, o(s) livro(s): {livros_outras_sagas}, não faz(em) parte da saga "Percy Jackson e os Olimpianos"."

ATENÇÃO: As saídas, quando necessárias, devem ser impressas na ordem acima.

'''
