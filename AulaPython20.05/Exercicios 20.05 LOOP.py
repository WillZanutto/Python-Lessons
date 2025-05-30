#1
lista = list(range(1, 51))
print(lista)

for i in range(len(lista)):
    print(lista[i]*2)

#2
print('-----------')
listanomes = ['João', 'José', 'Marcelino', 'Kalil', 'Jamil', 'Jamelão', 'Rovaldino', 'Rosiscleisson', 'Judith', 'Jurisvalda', 'Jusiscleide', 'Eunice', 'Eustacio', 'Euripides', 'Euclides']
print(listanomes)

lista_maiuscula = [string.upper() for string in listanomes]

print(lista_maiuscula)

#3
print('-----------')
listapreco = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(listapreco)
listaajustada = []

for preco in listapreco:
    listaajustada.append(preco * 1.1)

print(listaajustada)

#4
print('-----------')
listanumeros = [1, 4, -5, 2, 0, -6, -7, -2, 10, 11, 45, -50, -33, 0, -3]
print(listanumeros)

for num in range(len(listanumeros)):
    if listanumeros[num] < 0:
        listanumeros[num] = 0

print(listanumeros)

#5
print('-----------')
listaemails = ['wilzaso', 'teste1', 'juninhomotovlog']
print(listaemails)
listagmail = []

for email in listaemails:
    listagmail.append(email + '@gmail.com')

print(listagmail)

#6
print('-----------')
listaelementos = [12,58,46,None,69,47,None,None,None,100]
print(listaelementos)

for elemento in range(len(listaelementos)):
    if listaelementos[elemento] == None:
        listaelementos[elemento] = "Indefinido"

print(listaelementos)

#7
print('-----------')
listagigantesca = list(range(1, 50001))
contador = 0

for num in listagigantesca:
    if num % 2:
        contador += 1

print(contador)

#8
print('-----------')
listanumeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(listanumeros)
listadobro = []

for preco in listapreco:
    listadobro.append(preco * 2)

print(listadobro)

#9
print('-----------')
frase = input("Digite um frase: ")

listafrase = frase.split(' ')
print(listafrase)

for item in range(len(listafrase)):
    if len(listafrase[item]) > 5:
        listafrase[item] = "LONGA"

print(listafrase)

#10
print('-----------')
listapalavras = ["aranha", "banana", "agua", "butina", "cachorro", "anel", "aliança", "cabrito", "zebra", "cola", "azul", "amarelo", "roxo", "rosa"]
print(listapalavras)

for item in range(len(listapalavras)):
    if (listapalavras[item][0] == 'a'):
        listapalavras[item] = "***"

print(listapalavras)

#11
print('-----------')
listafrutas = ['banana', 'maçã', 'banana', 'laranja']
print(listafrutas)

for fruta in range(len(listafrutas)):
    if listafrutas[fruta] == 'banana':
        listafrutas[fruta] = 'abacaxi'

print(listafrutas)

#12
print('-----------')
listagigantesca2 = list(range(1, 50001))
total = 0

for num in range(len(listagigantesca2)):
    total = total + listagigantesca2[num]

print(total)

#13
print('-----------')
listanumeros2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 50, 51, 65, 75, 70]
print(listanumeros2)
listamaiores = []

for num in range(len(listanumeros2)):
    if listanumeros2[num] > 50:
        listamaiores.append(listanumeros2[num])

print(listamaiores)

#14
print('-----------')
listanomes = ['João', 'José', 'Marcelino', 'Kalil', 'Jamil', 'Jamelão', 'Rovaldino', 'Rosiscleisson', 'Judith', 'Jurisvalda', 'Jusiscleide', 'Eunice', 'Eustacio', 'Euripides', 'Euclides']
listasaudacao =[]
print(listanomes)

for nome in range(len(listanomes)):
    listasaudacao.append('Olá, ' + listanomes[nome] + '.')

print(listasaudacao)

#15
print('-----------')
listanotas = [6, 7, 4, 7, 8, 2, 1, 9, 10]

for nota in range(len(listanotas)):
    if listanotas[nota] >= 6:
        print(f"Nota {listanotas[nota]}. Aprovado!")
    else:
        print(f"Nota {listanotas[nota]}. Reprovado!")