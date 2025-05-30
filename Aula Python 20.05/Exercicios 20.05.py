#1
itens = ['Willian','Teste',1,5,15,33,42,True,6.5,'Euclides','Mauricio',False]
print(itens)

#2
itens.append('Eustacio')
print(itens)

#3
novos = [100, 200, 300]
itens.extend(novos)
print(itens)

#4
itens.insert(2, "meio")
print(itens)

#5
itens.remove(100)
print(itens)

#6
removido = itens.pop(3)
print(removido)

#7
itens.clear()
print(itens)

#8
frutas = ["maçã","banana","laranja","banana"]
print(frutas.index("banana"))

#9
print(frutas.count("banana"))

#10
frutas.reverse()
print(frutas)

#11
dividido = 'python,java,c++'.split(',')
print(dividido)

#12
juntando = '|'.join(["py", "js", "rb"])
print(juntando)

#13
hello = " Hello, World! ".strip()
print(hello)

#14
strfruta = " apple;banana;cherry; ".strip()
listafruta = strfruta.split(';')
listafruta.remove('')
print(listafruta)

#15
nums = [1,2,3,4,5]

while nums != []:
    removidonums = nums.pop()
    print(removidonums)

print(nums)

#16
strusuario = input("Digite uma frase:")
listastr = strusuario.split(" ")
listastr.reverse()
strreverse = '-'.join(listastr)
print(strreverse)

#17
with open('frutas.txt', 'rt') as arquivo:
    arqfrutas = arquivo.read()

print(arqfrutas)
arqfrutasrep = arqfrutas.replace(' ','')
print(arqfrutasrep)
listarqfrutas = arqfrutasrep.split(",")
print(listarqfrutas)


for i in listarqfrutas:
    if listarqfrutas.count(i) > 1:
        listarqfrutas.remove(i)

listarqfrutas.sort()
print(listarqfrutas)