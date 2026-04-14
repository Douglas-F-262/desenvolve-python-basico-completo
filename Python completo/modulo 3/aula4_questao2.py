Nota = int(input("Insira a avaliação do filme (de 1 a 5): "))

# Estrutura de decisão para cada nota
if Nota == 5:
    print("Excelente!")
elif Nota == 4:
    print("Muito Bom!")
elif Nota == 3:
    print("Bom!")
elif Nota == 2:
    print("Regular.")
elif Nota == 1:
    print("Ruim.")
else:
    print("Nota inválida! Por favor, digite um número entre 1 e 5.")