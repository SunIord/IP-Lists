n1 = int(input())
if n1 <= 0:
  print(f"{n1:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")

else:
  n2 = int(input())
  
  if n2 <= 0:
    print(f"{n2:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
  
  else:
    n3 = int(input())
    
    if n3 <= 0:
      print(f"{n3:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    
    else:
      palavra = input()
      
      if not palavra.islower():
        print(f"{palavra} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
      
      else:
        n5 = int(input())
        
        if n5 <= 0:
          print(f"{n5:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir")
        
        else:
          if n1 % 2 == 0:
            n1 *= 2
          
          else:
            n1 *= 0.5
          
          if n2 % 2 == 0:
            n2 *= 2
          else:
            n2 = n2 * 0.5
          
          if n3 % 2 == 0:
            n3 *= 2
          else:
            n3 *= 0.5
        numero_final = (n5 * n1 * n2 * n3) ** 0.5
        
        if numero_final >= 10:
          print(f"O número {numero_final:.2f} e a palavra {palavra} eram as respostas. A caixa foi aberta.")
        
        else:
          diferenca = 10 - numero_final
          print(f"A combinação era muito pequena, a caixa só vai poder ser aberta daqui a {diferenca:.2f} anos.")
          
'''

Robertinho é um excelente detetive e que possui diversos clientes ao redor do mundo.

Certo dia ele recebeu um novo caso, um cliente havia comprado uma caixa estranha com um vendedor no Marrocos que o desafiou a desvendar seus segredos.

Sendo um bom detetive, Robertinho descobriu facilmente as regras para abrir a caixa. Mas, como ele é bastante ocupado, deixou para você, seu brilhante assistente, escrever um código que consiga abrir a caixa automaticamente.

Ele disse que a combinação que abre a caixa é composta por um número e por uma palavra.

Para descobrir essa combinação, você poderá receber até 4 números e 1 palavra. Para cada um dos 3 primeiros números recebidos, você deverá multiplicá-lo por 2, caso ele seja par ou multiplicá-lo por 0.5, caso ele seja ímpar.

Depois disso, você deverá multiplicar o quarto número recebido por todos os outros três valores encontrados e por fim, tirar a raiz quadrada desse resultado para encontrar o número que pode abrir a caixa.

numero_final = √(n5 x n1 x n2 x n3)

Dica: Não arredonde valores durante os cálculos.

Input

Inicialmente, você poderá receber até 4 inputs, os três primeiros sendo números e o último uma palavra.

n1

n2

n3

palavra

Entretanto, apenas números positivos podem ser aceitos pela caixa, dessa forma, caso o número não atenda ao requisito, seu código deve parar imediatamente e não deve receber mais inputs.

Ou seja, você somente deve receber o n2 se n1 for positivo. O mesmo se aplica a n3.

Em relação a palavra recebida, você só deve continuar o programa caso ela esteja TODA escrita em minúsculo. Caso ela não esteja escrita dessa forma, o seu código deve parar e não deve receber mais nenhum input.

Se todas as 4 entradas forem aceitas, você deve receber mais um número.

n5

Output

Caso seu código pare em alguma situação nos primeiros 4 inputs você deve printar:

"{Y} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.”

{Y} sendo o valor que não foi aceito pelo código, podendo ser o número ou a palavra.

Caso o número final encontrado seja maior ou igual a 10:

"O número {numero_final} e a palavra {palavra} eram as respostas. A caixa foi aberta."

Caso o número final encontrado seja menor que 10:

"A combinação era muito pequena, a caixa só vai poder ser aberta daqui a {Z} anos."

Z é a diferença entre 10 e numero_final.

Obs.: Lembre-se todos os outputs que possuirem números deverão ter duas casas decimais.

'''        
