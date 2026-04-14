##pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True se o participante tiver entre 16 e 18 anos, já tiver jogado pelo menos 3 jogos e já ter vencido pelo menos 1 jogo, permitindo seu ingresso no clube.

Idade = int(input("Qual a sua idade:  "))
Partidas = input("Já jogou pelo menos 3 jogos de tabuleiro? (responda com True ou False)")
Vitorias = int(input("Quantos jogos já venceu? "))


#entre 16 e 18 anos, já tiver jogado pelo menos 3 jogos e já ter vencido pelo menos 1 jogo, permitindo seu ingresso no clube.

a = Idade >= 16 and Idade <=18
b = Partidas = True
c = Vitorias >=1

apto = a and b and c


if apto:
    print("Sim apto")
else:
    print("Não inapto")








