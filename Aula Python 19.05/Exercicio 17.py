def maior(numero1,numero2):
    if numero1 > numero2:
        return(numero1)
    else:
        return(numero2)
    
numusuario1 = int(input("Insira o Primeiro Numero: "))
numusuario2 = int(input("Insira o Segundo Numero: "))

nummaior = maior(numusuario1,numusuario2)

print(f"O maior numero é o {nummaior}")