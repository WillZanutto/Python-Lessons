numero = 1
total = 0

while numero != 101:
    if (numero % 2) == 0:
        total = total + numero
        
    numero = numero + 1

print (f"O total dos numeros pares é {total}.")