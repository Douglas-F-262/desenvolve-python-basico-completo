genero=input("Genero? M/F :  ")
idade=int(input("Idade?   "))
temp_serv=int(input("Tempo de serviço    "))


a = (genero == 'F' and idade >= 60) or (genero == 'M' and idade >= 65)
b = temp_serv > 30
c = idade >= 60 and temp_serv >= 25

aposentar = a or b or c
 

if aposentar:
    print("Sim apto")
else:
    print("Não inapto")