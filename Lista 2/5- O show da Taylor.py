show_name = input()
codigo_vip = 1
contador = 0

while (codigo_vip != 1004):
  codigo_vip = int(input())
  
  if codigo_vip == 1000:
    contador += 1
    print("Mais um VIP! Não podemos esquecer de contabilizá-lo.")
  
  elif codigo_vip == 1001:
    print("Ingresso Normal. Não iremos contabilizá-lo.")
  
  elif codigo_vip == 1002:
    print("Ele ficará na frente do show, porém não é VIP! Não será contabilizado também.")
  
  elif codigo_vip == 1003:
    print("Espera, quem é esse? Ele não pagou! Não devemos sequer analisar sua entrada.")
  
  elif codigo_vip == 0000:
    break
  
  else:
    break

if codigo_vip == 1004:
  print("Esse código não existe! O sistema quebrou...")
  print("Vamos aguardar até que o suporte nos ajude.")
  comentario_aleatorio = input()

  while comentario_aleatorio != "Ajudou":
    comentario_aleatorio = input()
    print("Ainda não...")

print(f"O show da Taylor Swift será em {show_name} e contará com {contador} VIPs!")

'''

É hora do show da Taylor Swift!

Porém, mesmo com toda essa euforia nós precisamos organizar da melhor forma possível. Fomos contratados para criar um programa que ajude a contabilizar o número de pessoas no show, principalmente os VIPs! Precisamos fazer com que esse show seja impecável e não pare por nada, se não teremos problema…

Entretanto, vamos lembrar que queremos um programa simples, logo vamos usar apenas condicionais e loops, pois caso contrário vamos ter que refazer 😟

Input

Você receberá primeiro o lugar do show

show_name

Depois, você irá receber N códigos de pessoas! Correspondente a todas as pessoas que devemos analisar…

codigo_vip

Porém, devemos analisar elas com cuidado…

Temos algumas opções de código que podem ser 0000, 1000, 1001, 1002, 1003 ou 1004, onde cada um possuí um significado específico:

0000: Fim da análise.
1000: VIPs
1001: Ingressos normais longe do palco.
1002: Ingressos normais perto do palco.
1003: Pessoas que não pagaram.
1004: Erro.
Não teremos nenhum problema para a maioria dos códigos e nosso principal foco são os VIPs. Eles possuem o código 1000, logo, precisamos contar toda vez que um VIP aparecer para organizar sua experiência da melhor forma possível.

Entretanto, caso apareça um 1004 … esse é um código vírus que pode afetar nosso sistema então devemos esperar ajuda técnica. Enquanto isso, você receberá entradas aleatórias que correspondem a situação do sistema e, somente quando a entrada for “Ajudou”, siginifica que está resolvido. Mas, mesmo depois de ter recebido a ajuda, por precaução ele não receberá mais nenhum código pra analisar.

text_situacao

Output

Quando chegar um VIP, deverá sempre ser contabilizado e printar a seguinte mensagem:

"Mais um VIP! Não podemos esquecer de contabilizá-lo."

Para ingressos comuns longe do palco, deverá apenas ser printado:

"Ingresso Normal. Não iremos contabilizá-lo."

Para ingressos comuns perto do palco, deverá apenas ser printado:

"Ele ficará na frente do show, porém não é VIP! Não será contabilizado também."

Quando tivermos código 1003, deverá apenas ser printado:

"Espera, quem é esse? Ele não pagou! Não devemos sequer analisar sua entrada."

Quando tivermos código de erro, deverá ser printado as seguintes mensagens:

"Esse código não existe! O sistema quebrou..."

"Vamos aguardar até que o suporte nos ajude."

Além disso, enquanto se espera o input de ajuda para cada vez que o sistema não tiver sido consertado deverá mostrar:

"Ainda não..."

Por fim, o programa será encerrado quando não tiver mais nenhum código para analisar ou quando tiver sido consertado.

Após o término das análises, deverá ser mostrada a seguinte mensagem:

"O show da Taylor Swift será em {show_name} e contará com {contador} VIPs!"

Onde show_name corresponde ao lugar do show e contador corresponde a quantidade de VIPs.

'''
