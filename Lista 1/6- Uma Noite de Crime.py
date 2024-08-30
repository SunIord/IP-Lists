sua_vida = int(input())
poder_sua_arma = int(input())
sua_habilidade_luta = int(input())
seu_poder_surpresa = int(input())
poder_arma_mascarado = int(input())
habilidade_luta_mascarado = int(input())
poder_surpresa_mascarado = int(input())
defesa_mascarado = int(input())

if (poder_sua_arma > poder_arma_mascarado) and (sua_habilidade_luta > habilidade_luta_mascarado) and (seu_poder_surpresa > poder_surpresa_mascarado):
  print("Ainda bem que deu tudo certo, está quase em casa")

else:
  sua_vida -= defesa_mascarado
  
  if sua_vida > 0:
    poder_sua_arma *= 0.95
    sua_habilidade_luta *= 0.95
    seu_poder_surpresa *= 1.05
    print("Rápido, corra antes que ele vá atrás de você!")
  
  else:
    print("Oh, no! Acabou pra mim")

if sua_vida > 0:
  poder_arma_novo_mascarado = int(input())
  poder_luta_novo_mascarado = int(input())
  poder_surpresa_novo_mascarado = int(input())
  
  if (poder_sua_arma >= poder_arma_novo_mascarado) or (sua_habilidade_luta >= poder_luta_novo_mascarado) or (seu_poder_surpresa >= poder_surpresa_novo_mascarado):
    print("Casa, aqui vou eu")
  
  else:
    print("Oh, no! Acabou pra mim")
    
'''

A Noite do Crime foi criada com o objetivo de diminuir a criminalidade durante o ano a partir da legalização de todo tipo de crime em uma noite específica do ano. A primeira noite de anarquia, no Brasil, irá acontecer e você não tem nenhum interesse em participar, apenas em se proteger.

Porém, você estava tão focado na primeira lista de IP/P1 que não percebeu o início da Noite de Crime. Agora é tarde demais para voltar pra casa em total segurança, mas é uma opção melhor do que ficar em espaços públicos.

No caminho de casa, você se depara com uma pessoa mascarada que está atacando todos que passam na rua e conclui que sua única chance é atacar primeiro. Então você procura por uma arma abandonada e tenta um ataque surpresa.

Para saber se vai vencer a luta ou não, é necessário ter algumas informações: o poder da arma, o poder de luta e o poder de surpresa de ambos (poder de surpresa de quem está sendo atacado é a tolerância aos ataques surpresas), sua quantidade de vida e o nível de defesa do mascarado. Se o atacante (inicialmente, você) tiver todas as três primeiras categorias maiores do que a outra pessoa, o ataque é bem-sucedido. No cenário oposto, o atacante perde a luta.

Se você, atacante, perder a primeira luta, sua vida decresce o valor do nível de defesa do mascarado. Caso ainda tenha vida (vida > 0), você ainda consegue fugir, mas os poderes de arma e de luta diminuem 5% cada, enquanto a sua tolerância às surpresas cresce 5%.

Caso você tenha tido sucesso em derrotar essa pessoa mascarada ou se ainda estiver vivo, continua andando em direção ao seu lugar seguro, porém o companheiro do mascarado vai em busca de vingança. Nessa rodada, você está se defendendo e o outro bandido mascarado é o atacante. Além disso, são recebidas novas informações: os poderes do novo atacante.

Para decidir a segunda luta, se você tiver qualquer um dos poderes maior ou igual ao do atacante, essa defesa é o suficiente para você correr para casa, caso contrário, não há esperanças!

Input

Primeiro, são dadas as estatísticas da primeira rodada, que são 8 inteiros, cada um em uma linha diferente:

sua_vida

poder_sua_arma

sua_habilidade_luta

seu_poder_surpresa

poder_arma_mascarado

habilidade_luta_mascarado

poder_surpresa_mascarado

defesa_mascarado

Caso você consiga passar dessa luta, (ou seja, vida > 0), você receberá os dados para a próxima luta:

poder_arma_novo_mascarado

poder_luta_novo_mascarado

poder_surpresa_novo_mascarado

Output

Se você for bem-sucedido no primeiro ataque, logo após a vitória a saída deve ser:
Ainda bem que deu tudo certo, está quase em casa

Porém, se você perder e ainda tiver vida:
Rápido, corra antes que ele vá atrás de você!

Caso você ganhe a segunda luta, imprima:
Casa, aqui vou eu

Caso você perca a segunda luta ou não tenha mais vida após a primeira rodada:
Oh, no! Acabou pra mim

'''
