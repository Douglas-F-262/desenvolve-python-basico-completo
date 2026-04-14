classe = input("Escolha a classe (guerreiro, mago ou arqueiro)"   )
forca = int(input("Digite os pontos de força (de 1 a 20):"))
magia = int(input("Digite os pontos de magia (de 1 a 20):"))


a = (forca >= 15) and (magia <=10) and (classe == "guerreiro")
b = (forca <= 10) and (magia >=15) and (classe == "mago")
c = (forca > 5) and (magia >5) and (forca < 15) and (magia <15) and (classe == "arqueiro")

if a:
    print("Sim, guerreiro apto")
elif b:
    print("Sim, mago apto")
elif c:
    print("Sim, arqueiro apto")
else:
    print("Não, requisitos não atingidos ou classe inválida")
