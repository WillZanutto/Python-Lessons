import csv
from collections import defaultdict

qtdlinhas = 0
total = 0
totallinha = 0
qtdproduto = defaultdict(int)
totalprods = 0
menor = 999999
maior = 0


#lê arquivo CSV
with open('vendas.csv', mode='r', encoding='utf-8',newline='') as vendas:
    leitor = csv.reader(vendas, delimiter=',')
    header = next(leitor)
    for linha in leitor:
        ordem = dict(zip(header, linha))
        
        #calcula o valor total do pedido
        totallinha = float(int(ordem['quantidade']) * float(ordem['preco']))
        
        #printa Produto | Preço | Total
        print(f"Produto: {ordem['produto']} | Preço: {ordem['preco']} | Total: {totallinha}")
        
        #conta linhas
        qtdlinhas += 1
        
        #calcula o preço total
        total += float(ordem['preco'])
        
        #calcula a quantidade total POR produto
        qtdproduto[ordem['produto']] += int(ordem['quantidade'])
        
        #calcula o total da quantidade de produtos
        totalprods += int(ordem['quantidade'])
        
        #valida maior e menor quantidade
        if float(ordem['quantidade']) > maior:
            maior = float(ordem['quantidade'])
        elif float(ordem['quantidade']) < menor:
            menor = float(ordem['quantidade'])

#lê arquivo CSV para gravação
with open('vendas.csv', mode='r', encoding='utf-8',newline='') as vendas:
    leitor = csv.reader(vendas, delimiter=',')
    header = next(leitor)

#grava arquivo CSV
    with open('alto_valor.csv', mode='w', encoding='utf-8',newline='') as alto_valor:
        #marca como arquivo para gravação
        arquivo = csv.writer(alto_valor)

        #grava header
        arquivo.writerow(header)

        #valida se Preço > 100 e grava no arquivo novo
        for linha in leitor:
            if float(linha[3]) > 100:
                arquivo.writerow(linha)

print('-------------------------------------------------------------')
print(f"Quantidade de Linhas no Arquivo: {qtdlinhas}")
print('-------------------------------------------------------------')
print(f"Valor total dos produtos: {total}")
print('-------------------------------------------------------------')
print(dict(qtdproduto))
print('-------------------------------------------------------------')
print(f'A média do valor dos produtos é: {totalprods / qtdlinhas}')
print('-------------------------------------------------------------')
print(f"A maior quantidade é: {maior}")
print('-------------------------------------------------------------')
print(f"A menor quantidade é: {menor}")
print('-------------------------------------------------------------')



listadic = []

#lê arquivo CS para criação de Lista
with open('vendas.csv', mode='r', encoding='utf-8',newline='') as vendas:
    leitor = csv.reader(vendas, delimiter=',')
    header = next(leitor)
    
    #adiciona o dicionario à lista
    for linha in leitor:
        dicionario = dict(zip(header, linha))
        listadic.append(dicionario)

#printa a lista de forma  estruturada
for i in listadic:
    print(i)