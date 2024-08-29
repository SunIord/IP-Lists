resposta_correta_1 = input()
resposta_correta_2 = input()
resposta_correta_3 = input()

pergunta_1 = input()
resposta_1 = input()

if resposta_1 == resposta_correta_1:
  print("Muito bem! Olha como a primeira foi fácil, seu amigo talvez sobreviva. Falta só mais duas para acabar com isso!")
  
  pergunta_2 = input()
  resposta_2 = input()
  
  if resposta_2 == resposta_correta_2:
  
    print("A resposta está e…exata! Você é mais inteligente do que eu pensei, já posso caprichar nesta última, vamos ver se você realmente conhece filmes de terror!")
    pergunta_3 = input()
    resposta_3 = input()
    if resposta_3 == resposta_correta_3:
      print("Droga, não vai ser hoje que vou ver sangue, que pena! Mas não se esqueça de mim, quem sabe um dia algum dos seus amigos não queiram brincar para lhe salvar!")
  
    else:
      print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")
  
  else:
    print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")

else:
  print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")

'''

Você estava em sua casa sozinho se arrumando para uma festinha de Halloween, mas do nada seu telefone toca. Você checa se não vem de São Paulo, mas é realmente daqui, então atende:

— Alô?

— Olá, você gosta de filmes de terror?

Você já acha que é seu amigo sem ter o que fazer e desliga o telefone, mas o telefone toca de novo:

— Feliz Halloween, meu escolhido! Não desligue, tenho uma proposta pra você.

— Quem é?

— Bem, isso é um segredo. Mas eu só queria te dizer que seu amigo está aqui, e a vida dele depende do quanto você conhece os filmes de terror!

Mesmo achando que é só mais uma brincadeira, você decide não arriscar devido aos casos com Ghostface que vêm ocorrendo na vizinhança:

— Tu-tudo bem, como funciona?

— Bom, lá vai as regras: vou lhe fazer 3 perguntas. Se você errar alguma, alguém querido irá morrer essa noite. É bem simples, não é?

— Essa brincadeira não tem graça!

— E quem está brincando? Minha apresentação já terminou, lá vai as perguntas, e cuidado pra não errar, hein?

Input

Inicialmente você receberá 3 respostas em ordem para cada pergunta.

resposta_correta_1

resposta_correta_2

resposta_correta_3

Após isso, receberá a pergunta e a sua resposta dada para cada uma delas, sempre na ordem de primeiro a pergunta e depois a resposta. Caso você erre, nenhuma entrada a mais é recebida. Caso você acerte, receberá um novo par de pergunta e resposta, até que as 03 perguntas sejam feitas.

pergunta

resposta

Output

Caso você acerte a primeira pergunta, imprima:

Muito bem! Olha como a primeira foi fácil, seu amigo talvez sobreviva. Falta só mais duas para acabar com isso!

Caso você acerte a segunda, imprima:

A resposta está e…exata! Você é mais inteligente do que eu pensei, já posso caprichar nesta última, vamos ver se você realmente conhece filmes de terror!

Por último, caso você acerte a terceira, imprima:

Droga, não vai ser hoje que vou ver sangue, que pena! Mas não se esqueça de mim, quem sabe um dia algum dos seus amigos não queiram brincar para lhe salvar!

Se, infelizmente, você não acertar alguma questão, imprima:

A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!

Mas lembre-se, no jogo do Ghostface, só é necessária uma resposta errada para que tudo acabe, então não é necessário continuar com as próximas perguntas!

'''
