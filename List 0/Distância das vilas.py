X = int(input())
Z = int(input())
H = float(((X - 34)**2 + (Z - 220)**2))**(1/2)
K = float(((X - 0)**2 + (Z - 0)**2))**(1/2)
S = float(((X - 140)**2 + (Z - 456)**2))**(1/2)
print("Distancia para Hogsmeade: %.2f" % H)
print("Distancia para Kakariko: %.2f" % K)
print("Distancia para Solitude: %.2f" % S)

'''

O mapa do Minecraft é composto de blocos cúbicos em uma relação de igualdade com o sistema métrico, assim, cada aresta dos blocos tem 1 metro. Dessa forma, é possível identificar localidades por triplas de coordenadas X, Y, Z, na qual X representa a longitude, Y representa a elevação em blocos e Z representa a latitude.

Para simplificar a comunicação, é comum se referir a localidades apenas no plano da superfície do mapa, utilizando apenas as coordenadas X e Z, referindo-se ao ponto no X e Z informados e no Y do ponto da superfície.

Para definir distâncias entre duas localidades é utilizada a fórmula de distância euclidiana, na qual o Y das duas coordenadas pode ser omitido para definir apenas a distância nas duas dimensões. A fórmula de distância euclidiana é:

D² = (X1 - X2)² + (Z1 - Z2)²
Para entregar os ferros para as vilas, Tantan precisaria saber quais as distâncias da sua localidade para cada vila, podendo se programar em suas viagens. Nas anotações de Tantan, as vilas estavam associadas as seguintes coordenadas:

Hogsmeade (X: 34, Y: 110, Z: 220)
Kakariko (X: 0, Y: 64, Z: 0)
Solitude (X: 140, Y: 200, Z: 456)
Sua tarefa é, baseado nas coordenadas atuais de Tantan, listar as distâncias para cada uma das vilas.

Input

X - número inteiro
Z - número inteiro
As duas linhas da entrada são compostas por números inteiros X e Z, que indica a coordenada atual de Steve, sem o Y, que pode ser abstraído como informado na descrição.

Obs: Você deve considerar que a entrada é amigável, ou seja, sempre estará dentro do formato descrito.

Output

Distancia para Hogsmeade: H

Distancia para Kakariko: K

Distancia para Solitude: S

-H - número de ponto flutuante -K - número de ponto flutuante -S - número de ponto flutuante

As linhas de saída são compostas por um texto seguido, seguido pela distância da coordenada atual de Tantan para a vila correspondente.

Obs: A distância deve ser aproximada em duas casas decimais.

'''
