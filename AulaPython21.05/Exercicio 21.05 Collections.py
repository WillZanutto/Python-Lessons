import csv
from collections import Counter
from collections import defaultdict

produtos = []
datas = []
qtdproduto = defaultdict(int)
precoproduto = defaultdict(list)
totalproduto = defaultdict(float)
vendas_distintas = defaultdict(int)
listavendascinco = []

#lê arquivo CSV e cria uma lista com os produtos
with open('vendas.csv', mode='r', encoding='utf-8',newline='') as vendas:
    leitor = csv.reader(vendas, delimiter=',')
    header = next(leitor)
    for linha in leitor:
        ordem = dict(zip(header, linha))

        #cria lista com todas as ocorrencias dos produtos
        nome_produto = linha[1]
        produtos.append(nome_produto)

        #calcula a quantidade total POR produto
        qtdproduto[ordem['produto']] += int(ordem['quantidade'])

        #calcula o total POR produto
        precoproduto[ordem['produto']].append(float(ordem['preco']))

        #calcula a quantidade total POR produto
        totalproduto[ordem['produto']] += float(ordem['preco'])

        #Verifica se a quantidade da venda foi maior que 5 e cria uma lista
        if int(ordem['quantidade']) > 5:
            listavendascinco.append(linha)

        #Cria dicionario com a quantidade de vendas distintas
        vendas_distintas[ordem['produto']] += 1

        data_venda = linha[0]
        datas.append(data_venda)

#Conta quantas vezes cada produto aparece na lista
frequencia_produtos = Counter(produtos)
print(frequencia_produtos)
print('-------------------------------------------------------------')

#Printa qual produto mais aparece na lista
print(frequencia_produtos.most_common(1))
print('-------------------------------------------------------------')


# #lê arquivo CSV
# with open('vendas.csv', mode='r', encoding='utf-8',newline='') as vendas:
#     leitor = csv.reader(vendas, delimiter=',')
#     header = next(leitor)
#     for linha in leitor:
#         ordem = dict(zip(header, linha))

#         #calcula a quantidade total POR produto
#         qtdproduto[ordem['produto']] += int(ordem['quantidade'])

#         #calcula o total POR produto
#         precoproduto[ordem['produto']].append(float(ordem['preco']))

#         #calcula a quantidade total POR produto
#         totalproduto[ordem['produto']] += float(ordem['preco'])

#         #Verifica se a quantidade da venda foi maior que 5 e cria uma lista
#         if int(ordem['quantidade']) > 5:
#             listavendascinco.append(linha)

#         #Cria dicionario com a quantidade de vendas distintas
#         vendas_distintas[ordem['produto']] += 1

#Printa a quantidade total POR produto
print(dict(qtdproduto))
print('-------------------------------------------------------------')

#Printa o total POR produto
print(dict(precoproduto))
print('-------------------------------------------------------------')

#Faz o Sort da Quantidade de Produtos
listaquantidade = sorted(qtdproduto.items(), key=lambda x: x[1], reverse=True)
print(listaquantidade)
print('-------------------------------------------------------------')

#Faz o Sort do Produtos por valor total vendido
listatotalprod = sorted(totalproduto.items(), key=lambda x: x[1], reverse=True)
print(listatotalprod)
print('-------------------------------------------------------------')

#Lista das vendas que foram maiores que 5
print(listavendascinco)
print('-------------------------------------------------------------')

#Printa o dicionario com a quantidade de vendas distintas
print(vendas_distintas)
print('-------------------------------------------------------------')

#Conta quantas vezes cada data aparece na lista
frequencia_datas = Counter(datas)
print(frequencia_datas)
print('-------------------------------------------------------------')