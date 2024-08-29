A = int(input())
L = int(input())
P = int(input())
H = int(input())
Da = A * H
Dl = L * H
Dp = P * H
M2 = int((Da + Dl + (abs(Da - Dl))) /2)
M = int((M2 + Dp + (abs(M2 - Dp))) /2)
print (M)

'''

Quantidade de diamantes é uma boa forma de medir riqueza no Minecraft pois é um dos recursos minerais mais difícil de ser encontrado e minerado no mapa.

Arthur, Luiz e Pedro decidiram fazer uma competição no Minecraft, para decidir quem iria escolher qual brega que irá tocar durantes suas longas noites de programação no CIn e pediram ajuda de Tantan para disponibilizar suas vilas como moradia para cada um. Foi combinado que a competição iria ser realizada dentro do jogo, na qual cada participante iria criar um mundo do zero e teria que encontrar o máximo de diamantes no tempo definido.

Para deixar a competição mais divertida, eles combinaram que cada um iria definir uma restrição para o programa que computaria qual o maior valor de diamantes encontrado pelos participantes.

Luiz definiu que o programa não poderia utilizar nenhuma estrutura condicional em seu código, como IF e outras;
Pedro proibiu a utilização de quaisquer funções de bibliotecas externas para calcular o máximo da quantidade de diamantes do vencedor;
Arthur falou que, para encontrar o valor final da quantidade máxima de diamantes, seria obrigatório utilizar a seguinte função para encontrar o máximo entre 2 valores: x = (a + b + (|a - b|)) / 2.
Visando deixar a solução mais simples, Arthur e Pedro chegaram a um acordo e decidiram que seria permitido utilizar funções externas para calcular o valor absoluto de um número (abs(), em Python).

Sua tarefa é escrever o programa que vai auxiliar os três a descobrir o vencedor da competição, em acordo com todas as restrições.

Input

A - número natural
L - número natural
P - número natural
H - número natural (1 <= H)
As três primeiras linhas representam a quantidade média de diamantes obtidos por hora de Arthur, Luiz e Pedro, respectivamente.

A quarta linha de entrada é composta por um valor que representa a duração da competição, em horas.

obs: Você deve considerar que a entrada é amigável, ou seja, sempre estará dentro do formato descrito.

Output

M - número natural
A linha única da saída é composta por um valor que representa o valor máximo de diamantes obtido por um participante, na competição.

'''
