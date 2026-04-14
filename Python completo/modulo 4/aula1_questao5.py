n = int(input("Digite a quantidade de respondentes: "))

soma_idades = 0
contador = n 

while n > 0:
    idade = int(input("Digite a idade: "))
    soma_idades = soma_idades + idade 
    n = n - 1 

# Cálculo da média
media = soma_idades / contador

print("A média de idade dos respondentes é:", media)