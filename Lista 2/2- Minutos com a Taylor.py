musicas_ouvidas = 0
total_minutos = 0
opiniao = input()

while (opiniao != "parei") or (musicas_ouvidas <= 21):
  if opiniao == "amei":
    total_minutos += 4
    musicas_ouvidas += 1

  elif opiniao == "essa não deu":
    pass

  elif opiniao == "escutei só metade":
    total_minutos += 2
    musicas_ouvidas += 1

  elif opiniao == "não parei de ouvir":
    musicas_ouvidas += 1
    repeticoes = 0
    comentario = input()

    while comentario != "pulei":
      repeticoes += 1
      comentario = input()
      total_minutos += 4 * repeticoes

  opiniao = input()
print(f"Você ouviu {total_minutos} minutos hoje!!!")

'''

A carreira da Taylor Swift é marcada por vários albúns musicais icônicos que, muitas vezes, ficam anos como os mais ouvidos nas plataformas de música.

Uma grande fã da Taylor queria saber quanto tempo por dia ela ouvia sua cantora favorita e pra descobrir isso ela chamou você, aluno estrela do CIN, para ajudá-la.

Ultimamente ela está viciada no novo álbum da Taylor, "1989 (Taylor's Version)”, que tem 21 músicas e você vai usar ele como base para seus cálculos.

Para facilitar as contas, considere que cada música do álbum tem 4 minutos.

Input

Para calcular, a fã irá opinar sobre as músicas. Logo, a cada música escutada, você receberá um input correspondente a opinião da garota sobre aquele som:

opiniao (string)

Vai ser recebido n vezes, enquanto ela estiver ouvindo música.

Perceba que ela vai dar a opinião dela sobre no máximo 21 músicas do álbum, mas ela pode não escutar todas.

Esse input de opinião pode ser:

“amei” → Ela escutou a música inteira (4 min)
“não parei de ouvir” → Ela repetiu essa música inteira x vezes até ela dizer "pulei". Cada vez que ela ouvir a música, ela irá fazer um comentário aleatório e diferente desses citados, até que o comentário seja “pulei”, o que significa que ela terminou de ouvir pela xº vez e mudou. Nesse caso, o total de minutos ouvidos é igual a 4x, sendo x igual ao número de comentários aleatórios recebidos.
“essa não deu” → ela não gostou dessa música e por isso não escutou (0 min)
“escutei só metade” → ela ouviu metade da música (2 min)
“parei” → ela não vai mais escutar música
Observação: Apenas músicas diferentes contam (ouvir a mesma música 10 vezes não será contabilizado como 10 músicas). Além disso, músicas puladas e escutadas apenas pela metade também contam como uma música.

Output

Quando a fã parar de ouvir as músicas ou bater a quantidade máxima você deverá printar:

“Você ouviu {quant_min} minutos hoje!!!”

Onde quant_min é a quantidade total de minutos que ela escutou música.

'''
