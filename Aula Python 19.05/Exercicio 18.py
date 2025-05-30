senha = input("Digite uma nova Senha:")

if len(senha) < 8:
    print("Senha deve possuir pelo menos 8 caracteres!")
else:
    digito = any(char.isdigit() for char in senha)
    if digito:
        print("Senha OK!")
    else:
        print("Senha deve conter pelo menos um numero!")
    
