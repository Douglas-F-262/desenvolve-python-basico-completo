## Escreva e execute seu código aqui


usuarios = {
    "admin": ("admin123", "Administrador"),
    "usuario1": ("senha123", "Usuário Comum"),
    "visitante1": ("guest2024", "Visitante")
}

while True:
    
    nome = input("insira seu nome de usuario   ")
        
    senha = input("Senha:  ")


    if nome in usuarios:
        senha_correta, nivel = usuarios[nome] 
        
        if senha == senha_correta:
            print("Autorizado! Acesso de:", nivel)
        else:
            print("Não autorizado")
    else:
        print("Não autorizado")