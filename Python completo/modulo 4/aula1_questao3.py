Entrada = input("Digite n1,n2 e n3 separados por vírgula: ")

n1, n2, n3 = [float(item.strip()) for item in Entrada.split(',')]

m = (n1+n2+n3)/3

if m >= 60 :
    print("Aprovado")
elif m >= 40 :
    print("Recuperação")
else:
    print("reprovado")
