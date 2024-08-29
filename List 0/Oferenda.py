D = int(input())
A = 10
L = 30
Pe = 100
if D<=1:
  P = "Erro"
elif D <= A:
  P = "Arthur"
elif D <= L:
  P = "Luiz"
elif D <= Pe:
  P = "Pedro"
else:
  P = "Nenhum"
print (P)

'''

Após ficarem impressionados com a mecânica do jogo, Arthur, Luiz e Pedro resolveram continuar jogando. Como Tantan estava muito mais avançado em recursos, eles convidaram Tantan para morar em suas vilas e fizeram ofertas de diamantes para tornar o convite mais interessante. Arthur ofereceu 10 diamantes, Luiz ofereceu 30 e Pedro 100.

Tantan estava precisando de diamantes, porém, sendo um garoto muito humilde, falou que iria aceitar a menor oferta possível que suprisse sua necessidade.

Sua tarefa é fazer um programa que ajude Tantan a decidir com quem ir morar.

Input

D - número natural (1 <= D)
A linha única de entrada é composta pela quantidade de diamantes que Tantan necessita.

Obs: Você deve considerar que a entrada é amigável, ou seja, sempre estará dentro do formato descrito.

Output

P - string
A linha única de saída é composta pelo nome de quem fez a oferta que foi aceita por Tantan, ou pela string "Nenhum", no caso em que nenhuma oferta supria a quantidade de diamantes necessária.

'''
