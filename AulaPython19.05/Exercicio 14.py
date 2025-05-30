import random

randomizado = random.randint(1, 10)
numerousuario = 0

while numerousuario != randomizado:
    numerousuario = int(input("Adivinhe o numero: "))
    if numerousuario == randomizado:
        print("Parabéns!! Você acertou o numero!!")
    else:
        print("Numero Incorreto!")