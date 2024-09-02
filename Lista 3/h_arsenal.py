instrumentos = ["Foice de Hades", 
"Talismã de Ícaro", 
"Elmo da Invisibilidade", 
"Cinto de Hermes", 
"Espada Anaklusmos", 
"Escudo Aegis", 
"Adaga Katoptris"]
entrada = input().split("-")

while entrada[0] != "Parar":
  nome = entrada[0]
  instrumentos_indesejados = entrada[1:]
  instrumentos_escolhidos = instrumentos.copy()
  
  for instrumento in instrumentos_indesejados:
    instrumentos_escolhidos.remove(instrumento)
  
  if len(instrumentos_escolhidos) == 0:
    print(f"{nome} irá batalhar na base do murro!")
  
  elif len(instrumentos_escolhidos) == 1:
    print(f"{nome} irá rumo a batalha com o equipamento: {instrumentos_escolhidos[0]}!")
  
  else:
    last = instrumentos_escolhidos[-1]
    instrumentos_escolhidos.pop()
    answ = ', '.join(n for n in instrumentos_escolhidos)
    print(f"{nome} irá rumo a batalha com os seguintes equipamentos: {answ} e {last}!")
  
  entrada = input().split("-")

'''

No acampamento Meio-Sangue, uma profecia ecoou pelos bosques, anunciando uma jornada épica para os semideuses. Percy Jackson, Annabeth Chase, Grover Underwood e outros heróis reuniram-se diante da majestosa árvore de Thalia, onde uma mesa mágica exibia uma variedade de equipamentos lendários.

Quíron, o centauro sábio, entregou a cada semideus a chance de escolher seus instrumentos para a batalha iminente.

Os equipamentos disponíveis eram:

Foice de Hades, Talismã de Ícaro, Elmo da Invisibilidade, Cinto de Hermes, Espada Anaklusmos, Escudo Aegis e Adaga Katoptris

A profecia exigia que cada semideus personalizasse sua mochila mágica, excluindo do seu arsenal os equipamentos indesejados. A escolha era crucial, pois cada equipamento poderia mudar o rumo da batalha de várias formas.

Você, utilizando a ferramenta mágica ancestral “Pythonius Bugadus”, deverá criar um programa que ajudará os heróis a organizar a sua mochila de equipamentos mágicos.

Input

Inicialmente, você deverá criar uma lista em seu código com todos os equipamentos mágicos disponíveis.

Após isso, o programa receberá uma quantidade indefinida de entradas como mostra abaixo:

nome1-equipamento1-equipamento2- ... -equipamentoN

...

nomeN-equipamento1-equipamento2- ... -equipamentoN

Parar

Com o nome do meio-sangue e os equipamentos que ele não quer em seu arsenal, separados por um hífen ("-").

O programa deverá receber entradas até que a palavra "Parar" seja recebida.

Obs.1: O Meio-sangue poderá precisar de todos os equipamentos disponíveis, ou seja, a entrada pode consistir apenas do nome do Meio-sangue, sem equipamentos indesejados.

Em seguida, você deverá criar cópias da sua lista de equipamentos original e excluir dessa cópia os itens que o Meio-sangue não deseja em seu arsenal.

Dica 1 - Aprenda como criar e manipular essas cópias utilizando o método ".copy()" clicando aqui

Output

A cada herói que fizer suas escolhas, você deverá retornar o seu nome e os itens que cada um escolheu manter para a batalha.

Caso ele(a) não queira utilizar nenhum equipamento mágico, você deverá imprimir:

{nomeDaPessoa} irá batalhar na base do murro!

Caso ele(a) escolha apenas um equipamento mágico, você deverá retornar:

{nomePessoa} irá rumo a batalha com o equipamento: {equipamento}!

Caso ele(a) escolha dois ou mais equipamentos mágicos, você deverá retornar:

{nomePessoa} irá rumo a batalha com os seguintes equipamentos: {equipamento1}, {equipamento2}, ... e {equipamentoN}!

Obs.2: nesse último caso, cada equipamento desejado deve ser printado, separado uns dos outros por uma vírgula e um espaço, com exceção do último, que deverá ser precedido por um espaço, um "e" e outro espaço (" e "). Caso só tenham dois equipamentos não serão adicionadas vígulas, apenas o " e " para separar os dois elementos.

Dica 2 Clique aqui para ter uma ideia de como realizar a formatação dos outputs.

'''
