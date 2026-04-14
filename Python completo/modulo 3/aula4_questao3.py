
ano = int(input("Digite um ano: "   ))


if ano % 400 == 0:
    print("Bissexto")

elif ano % 100 == 0:
    print("Não Bissexto")

elif ano % 4 == 0:
    print("Bissexto")
else:
    print("Não Bissexto")