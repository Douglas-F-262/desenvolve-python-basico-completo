
v_1 = int(input("Digite o primeiro número: "))
v_2 = int(input("Digite o segundo número: "))


soma = v_1 + v_2

if soma % 2 == 0:
    print(f"A soma é {soma}, que é um número PAR.")
else:
    print(f"A soma é {soma}, que é um número ÍMPAR.")