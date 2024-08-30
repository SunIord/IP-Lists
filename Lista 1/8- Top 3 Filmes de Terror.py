nome_filme_1 = input()
pontuacao_global_filme_1 = int(input())
critica_filme_1 = input()
nome_filme_2 = input()
pontuacao_global_filme_2 = int(input())
critica_filme_2 = input()
nome_filme_3 = input()
pontuacao_global_filme_3 = int(input())
critica_filme_3 = input()

if critica_filme_1 == "boa":
    nota_final_1 = pontuacao_global_filme_1 * 1.25

elif critica_filme_1 == "media":
    nota_final_1 = pontuacao_global_filme_1 * 1.00

elif critica_filme_1 == "ruim":
    nota_final_1 = pontuacao_global_filme_1 * 0.75

elif critica_filme_1 == "pessima":
    nota_final_1 = 0

if critica_filme_2 == "boa":
    nota_final_2 = pontuacao_global_filme_2 * 1.25

elif critica_filme_2 == "media":
    nota_final_2 = pontuacao_global_filme_2 * 1.00

elif critica_filme_2 == "ruim":
    nota_final_2 = pontuacao_global_filme_2 * 0.75

elif critica_filme_2 == "pessima":
    nota_final_2 = 0

if critica_filme_3 == "boa":
    nota_final_3 = pontuacao_global_filme_3 * 1.25

elif critica_filme_3 == "media":
    nota_final_3 = pontuacao_global_filme_3 * 1.00

elif critica_filme_3 == "ruim":
    nota_final_3 = pontuacao_global_filme_3 * 0.75

elif critica_filme_3 == "pessima":
    nota_final_3 = 0

if nota_final_1 >= nota_final_2 and nota_final_1 >= nota_final_3:
  print("**** TOP 3 FILMES ****")
  print(f"{nome_filme_1} está em 1° lugar")
  
  if nota_final_2 >= nota_final_3:
    print(f"{nome_filme_2} está em 2° lugar")
    print(f"{nome_filme_3} está em 3° lugar")
  
  else:
    print(f"{nome_filme_3} está em 2° lugar")
    print(f"{nome_filme_2} está em 3° lugar")

if nota_final_2 >= nota_final_1 and nota_final_2 >= nota_final_3:
  print("**** TOP 3 FILMES ****")
  print(f"{nome_filme_2} está em 1° lugar")

  if nota_final_1 >= nota_final_3:
    print(f"{nome_filme_1} está em 2° lugar")
    print(f"{nome_filme_3} está em 3° lugar")

  else:
    print(f"{nome_filme_3} está em 2° lugar")
    print(f"{nome_filme_1} está em 3° lugar")

if nota_final_3 >= nota_final_1 and nota_final_3 >= nota_final_2:
  print("**** TOP 3 FILMES ****")
  print(f"{nome_filme_3} está em 1° lugar")

  if nota_final_1 >= nota_final_2:
    print(f"{nome_filme_1} está em 2° lugar")
    print(f"{nome_filme_2} está em 3° lugar")

  else:
    print(f"{nome_filme_2} está em 2° lugar")
    print(f"{nome_filme_1} está em 3° lugar")

if nota_final_1 == 0:
    print(f"{nome_filme_1} teve uma crítica péssima")

elif nota_final_2 == 0:
    print(f"{nome_filme_2} teve uma crítica péssima")

elif nota_final_3 == 0:
    print(f"{nome_filme_3} teve uma crítica péssima")
    
'''

Em um fórum online, entusiastas estão imersos numa acalorada discussão sobre os três melhores filmes de terror de todos os tempos. Durante esse debate, diversos aspectos foram abordados, incluindo a crítica especializada e o desempenho nas bilheteiras. Contudo, diante da incerteza sobre a classificação de cada filme, um estudante CIn surgiu como solucionador desse impasse, desenvolvendo um programa capaz de ranquear os filmes de maneira objetiva.

Sendo assim, você ficará responsável desenvolver esse programa que será a chave para resolver problema.

Input

Para cada um dos três filmes, você receberá uma série de 3 entradas:

nome_filme

pontuacao_global_filme

critica_filme

A pontuacao_global_filme será o número inteiro de pontuação que o filme teve ao ser recebido pelo público.
A critica_filme é uma string que pode assumir os valores: "boa", "media", "ruim" e "pessima".
Para determinar o ranking, serão atribuídas pontuações.

A nota final do filme será dada pela pontuacao global do filme após passar pela nota da crítica, que funcionará no seguinte formato:

Crítica "boa":

pontuacao_global_filme * 1.25

Crítica "media":

pontuacao_global_filme * 1.00

Crítica "ruim":

pontuacao_global_filme * 0.75

Crítica "pessima":

O filme perde todos os seus pontos.

OBSERVAÇÕES:

Você não receberá nenhum caso de empates.
Você receberá no máximo UM filme com a crítica péssima.
A pontuação do filme pelo público sempre será um valor maior que zero (ou seja, pontuacao_global_filme > 0).
A pontuação final do filme poderá ser zero caso receba uma nota péssima.
Output

A estrutura da primeira saída sempre terá o seguinte formato:
"**** TOP 3 FILMES ****"

A segunda saída sempre será o resultado dos top 3 filmes:
"{filme_1} está em 1° lugar"

"{filme_2} está em 2° lugar"

"{filme_3} está em 3° lugar"

Se houver alguma crítica péssima para algum filme do ranking acima, a saída incluirá o ranque (como descrito acima), seguido por:

"{filme} teve uma crítica péssima"

'''
