distancia = float(input("Distância (km): "))
peso = float(input("Peso (kg): "))

if distancia <= 100:
    frete = peso * 1.0
elif distancia <= 300:
    frete = peso * 1.5
else:
    frete = peso * 2.0

if peso > 10:
    frete += 10

print("Total: R$", frete)