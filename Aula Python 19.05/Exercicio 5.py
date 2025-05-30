numero1 = float(input("Digite o Primeiro Numero:"))
numero2 = float(input("Digite o Segundo Numero:"))
operador = input("Digite a Operadoração(+, -, /, *):")

if operador == '+':
    print(f"O resultado da adição é: {numero1 + numero2}")

elif operador == '-':
    print(f"O resultado da subtração é: {numero1 - numero2}")

elif operador == '/':
    print(f"O resultado da divisão é: {numero1 / numero2}")

elif operador == '*':
    print(f"O resultado da multiplicação é: {numero1 * numero2}")

else:
    print(f"Operador Incorreto!")