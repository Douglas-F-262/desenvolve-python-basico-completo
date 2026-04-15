
n = int(input("Numero de experimentos : "))
cont = 0
sapo, rato, coelho = 0, 0, 0

while cont < n:
    total = int(input("insira a quantidade de cobaias :  "))
    tipo = input("Insira tipo de cobaia S, R, C :  ")

    if tipo == 'S':
        sapo += total

    elif tipo == 'R':
        rato += total
    
    elif tipo == 'C':
        coelho += total


    cont += 1


print("total de cobaias", sapo+rato+coelho)
print("total de sapos", sapo)
print("total de ratos", rato)
print("total de coelhos", coelho)

    



