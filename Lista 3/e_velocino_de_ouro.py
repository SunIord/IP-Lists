informacoes_deuses = [['Zeus', 'Poseidon', 'Atenas', 'Ares', 'Afrodite'],
[100, 90, 80, 70, 60],
['Raio', 'Tridente', 'Égide', 'Lança', 'Cinto Mágico']]

sequencia = input()
n = len(sequencia) - 1
x = 0 

for i in (sequencia):
  indice_deus = int(i)
  nome_deus = informacoes_deuses[0][indice_deus]
  poder_deus = informacoes_deuses[1][indice_deus]
  artefato_deus = informacoes_deuses[2][indice_deus]
  genero = "Deus" if indice_deus not in [2, 4] else "Deusa"

  if x != n:
    print(f'{genero}:{nome_deus}\n'
    f'Poder:{poder_deus}\n'
    f'Artefato:{artefato_deus}\n')

  else:
    print(f'{genero}:{nome_deus}\n'
    f'Poder:{poder_deus}\n'
    f'Artefato:{artefato_deus}')
  x += 1
  
'''

Percy Jackson e seus amigos estão em uma missão atrás do velocino de ouro, um artefato mágico com habilidades de cura poderosas, e para encontrá-lo, eles precisarão entrar na ilha do Polifemo. Porém, ao chegarem lá, eles viram que a porta de acesso para a sala onde se encontra o velocino se encontra trancada e ela só abrirá se eles conseguirem desvendar um enigma. Enigma esse que envolve conhecimentos lógicos sobre listas em programação. Sendo assim, eles precisarão da sua ajuda, por ser um programador tão poderoso quanto um semideus, para desvendar esse enigma e abrir a porta.

O enigma envolve os deuses do olímpo, seus poderes e seus artefatos. Basicamente, a porta receberá uma sequência de números formada por dígitos que vão de 0 a 4 e ela precisará retornar, dependendo da combinação, informações sobre os deuses. Os semideuses sabem que quaisquer informações sobre os principais deuses precisam ser consultadas usando a estrutura oficial do Olímpo, sem usar isso a porta nunca abrirá:

informacoes_deuses = [
    ['Zeus', 'Poseidon', 'Atenas', 'Ares', 'Afrodite'],
    [100, 90, 80, 70, 60],
    ['Raio', 'Tridente', 'Égide', 'Lança', 'Cinto Mágico']
]
Agora que você tem acesso a essa estrutura, cabe a você resolver a charada e abrir a porta para conseguir achar o velocino de ouro!

OBS.1: É obrigatório o uso da estrutura fornecida para a resolução do problema.

Input

Você receberá uma única entrada, que pode ser lida como uma string, contendo uma quantidade qualquer de algarismos que vão de 0 a 4.

sequencia

Exemplos de possíveis entradas:

0
312
0001
01234
Output

A saída vai ser a resposta contendo as informações dos deuses no formato:

Deus:{nome_deus}

Poder:{poder_deus}

Artefato:{artefato_deus}

Para cada Deus requisitado, a cada dígito recebido.

Isso significa que, ao receber a entrada "01", por exemplo, você deveria imprimir as informações de Zeus (0) e depois Poseidon (1).

OBS.2: Para as Deusas mulheres (Atenas e Afrodite), deve ser printado o output mostrado acima, com a mudança de "Deus" para "Deusa".

OBS.3: Além disso, entre as informações de um Deus e outro deve ser pulada uma linha no output (perceba que isso não ocorre após printar as informações do último Deus).

OBS.4: Pode ser necessário printar as informações de um Deus mais de uma vez!

'''
