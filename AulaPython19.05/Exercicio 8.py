idade = int(input("Insira a Idade do Usuario:"))

if idade < 12:
    print("O usuario é uma criança.")

elif idade >= 12 and idade <= 17:
    print("O usuario é um adolescente.")

elif idade >= 18 and idade <= 59:
    print("O usuario é um adulto.")

else:
    print("O usuario é um idoso.")