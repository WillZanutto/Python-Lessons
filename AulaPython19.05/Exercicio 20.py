with open("pessoa.txt", "rt") as arquivo:
    leitura = arquivo.read()
    
separacao = leitura.split()
print(len(separacao))

