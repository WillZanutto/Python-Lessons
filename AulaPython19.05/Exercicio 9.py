senhabase = "senha"
senhausuario = ''

while senhausuario != senhabase:
    senhausuario = input("Favor inserir a senha: ")
    if senhausuario == senhabase:
        print("Usuario logado com sucesso!")
    
    else:
        print("Senha incorreta!")