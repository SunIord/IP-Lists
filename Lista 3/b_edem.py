q = int(input())
zeus = ["Zeus", "trovão", "deus"]
afrodite =["Afrodite", "amor", "deusa"]
poseidon = ["Poseidon", "oceanos", "deus"]
hercules = ["Hércules", "força", "semideus"]
aquiles = ["Aquiles", "resistência", "semideus"]
orfeu = ["Orfeu", "música", "semideus"]
acertos = 0

if q == 0:
  print("Infelizmente, Percy Jackson, chegou atrasado para a exame...")

else:
  for i in range(1, q + 1):
    resposta_percy = input().split(', ')
    
    if (resposta_percy[0] in zeus) and (resposta_percy[1] in zeus) and (resposta_percy[2] in zeus):
      print(f"A resposta da {i}ª questão está... CORRETA!")
      acertos += 1
    
    elif (resposta_percy[0] in afrodite) and (resposta_percy[1] in afrodite) and (resposta_percy[2] in afrodite):
      print(f"A resposta da {i}ª questão está... CORRETA!")
      acertos += 1
    
    elif (resposta_percy[0] in poseidon) and (resposta_percy[1] in poseidon) and (resposta_percy[2] in poseidon):
      print(f"A resposta da {i}ª questão está... CORRETA!")
      acertos += 1
    
    elif (resposta_percy[0] in hercules) and (resposta_percy[1] in hercules) and (resposta_percy[2] in hercules):
      print(f"A resposta da {i}ª questão está... CORRETA!")
      acertos += 1

    elif (resposta_percy[0] in aquiles) and (resposta_percy[1] in aquiles) and (resposta_percy[2] in aquiles):
      print(f"A resposta da {i}ª questão está... CORRETA!")
      acertos += 1

    elif (resposta_percy[0] in orfeu) and (resposta_percy[1] in orfeu) and (resposta_percy[2] in orfeu):
      print(f"A resposta da {i}ª questão está... CORRETA!")
      acertos += 1

    else:
      print(f"A resposta da {i}ª questão está... ERRADA!")
  
  porcentagem_acertos = int((acertos / q) * 100)
  print(f"Percy Jackson, sua taxa de acerto no EDEM é de aproximadamente... {porcentagem_acertos}%")
  if porcentagem_acertos == 100:
    print("UAU, você gabaritou! Você é praticamente um deus do Olimpo!")

  elif 60 <= porcentagem_acertos < 100:
    print("Muito bem, você quase pode começar a desfilar entre os semideuses!")

  elif 20 <= porcentagem_acertos < 60:
    print("Você pode melhorar um pouco mais!")

  else:
    print("Bem... te vejo ano que vem")

'''

Percy Jackson, o semideus filho de Poseidon, está se preparando no acampamento meio-sangue para o Exame Divino do Ensino Médio (EDEM). Sua habilidade com a espada contracorrente é inquestionável, mas agora ele enfrenta um desafio diferente: a prova de Raciocínio Lógico Divino. Agora, cabe a você, corrigir a prova e determinar o resultado dele neste exame.

Na prova, Percy responderá sobre deuses e semideuses e a sua função é determinar se a resposta dele está correta.

Para isso, você tem o gabarito, isto é, a lista com deuses e semideuses e suas respectivas especialidade e natureza.

Lista correta de deuses e semideuses:
Nome: Zeus, Especialidade: trovão, Natureza: deus

Nome: Afrodite, Especialidade: amor, Natureza: deusa

Nome: Poseidon, Especialidade: oceanos, Natureza: deus

Nome: Hércules, Especialidade: força, Natureza: semideus

Nome: Aquiles, Especialidade: resistência, Natureza: semideus

Nome: Orfeu, Especialidade: música, Natureza: semideus

Input

Primeiramente, é solicitada a quantidade (Q) de questões que Percy respondeu.

Q (inteiro)

Em seguida, as Q respostas de Percy, contendo o nome de um deus, sua especialidade e sua natureza, separados por vírgula, exemplo:

Zeus, trovão, deus

Afrodite, amor, deusa

Hércules, força, semideus

OBS.: Use o método split() para tratar a entrada das respostas.

Output

Se a quantidade de questões recebidas for igual a 0, deverá ser exibida somente a mensagem abaixo e encerrar o programa:

Infelizmente, Percy Jackson, chegou atrasado para a exame...

Se não for o caso:

A correção é feita passando por cada resposta, e verificando se as informações estão corretas para cada deus especificado, retornando em ordem, a cada resposta, se houve acerto ou não:

Se a reposta estiver correta, é exibida a mensagem:
A resposta da {n}ª questão está... CORRETA!

Se a resposta estiver errada, é exibida a mensagem:
A resposta da {n}ª questão está... ERRADA!

OBS.: A contagem do valor de n começa em 1.

ATENÇÃO!!!

A ordem das caracteríticas das respostas não importam, ou seja, tanto a resposta "Afrodite, amor, deusa" como "deusa, Afrodite, amor" estão exatas.

Se Percy tiver que fazer alguma questão relacionadas sobre algum deus sem estar na lista mencionada acima, ele automaticamente erra a questão por não ter estudado o suficiente antes do exame.

Após verificar todas as respostas, você deve exibir a porcentagem aproximada de acertos de Percy no Exame, calculada através da fórmula int((questoes_corretas / total_questoes) * 100):
Percy Jackson, sua taxa de acerto no EDEM é de aproximadamente... {porcentagem}%

Em seguida, são exibidas mensagens diferentes de acordo com o desempenho obtido:

Se a porcentagem for igual a 100%, é exibida a mensagem:
UAU, você gabaritou! Você é praticamente um deus do Olimpo!

Se a porcentagem for maior ou igual 60% e for menor que 100%, é exibida a mensagem:
Muito bem, você quase pode começar a desfilar entre os semideuses!

Se a porcentagem for maior ou igual a 20% e menor que 60%, é exibida a mensagem:
Você pode melhorar um pouco mais!

Se a porcentagem for menor que 20%, é exibida a mensagem:
Bem... te vejo ano que vem

'''
