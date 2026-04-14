n = int(input("dê a quantidade de numeros"))
maior = 0

while n > 0 :
    
    x = float(input("dê o valor de x"))
   
    if x > maior:
        maior = x

    n = n - 1

print("O maior número digitado foi:", maior)   
