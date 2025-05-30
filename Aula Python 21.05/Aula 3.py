# import csv

# # 1. Abre o arquivo CSV em modo de leitura
# with open('vendas.csv', mode='r', encoding='utf-8',newline='') as f:
#     # 2. Crie um leitor CSV que separa campos por vírgula
#     leitor = csv.reader(f, delimiter=',')
#     # 3. Le a primeira linha (cabeçalho) para obter os nomes das colunas
#     header = next(leitor)
#     print('Colunas encontradas:', header)
#     # 4. Percorre cada linha restante do arquivo
#     for linha in leitor:
#         # 5. Emparelha nomes de colunas e valores em um dicionário
#         ordem = dict(zip(header, linha))
#         # 6. Acessa valores pelas chaves e exiba-os
#         print(f"Data: {ordem['data']} | Produto: {ordem['produto']} | Quantidade: {ordem['quantidade']} | Preço: {ordem['preco']}")


# # Conta quantas vezes cada elemento aparece
# from collections import Counter

# vendas = ['camisa','calça','camisa','boné','calça','camisa']
# qtd_itens_vend = Counter(vendas)
# print(qtd_itens_vend)
# print(qtd_itens_vend.most_common(3))
# print(qtd_itens_vend.most_common(2))
# print(qtd_itens_vend.most_common(1))


# #DEFAULTDICT

# # Sem defaultdict
# vendas_tuplas = [('camisa',3), ('calça',2), ('camisa',1)]
# soma = {}  # dicionário vazio

# for prod, qtd in vendas_tuplas:
#     # 1. Verificar se já existe a chave prod em soma
#     if prod in soma:
#         soma[prod] += qtd    # se existe, soma a quantidade
#     else:
#         soma[prod] = qtd     # se não existe, cria a chave com qtd

# print(soma)  # {'camisa': 4, 'calça': 2}


# #Com defaultdict
# from collections import defaultdict

# vendas_tuplas = [('camisa',3), ('calça',2), ('camisa',1)]
# soma = defaultdict(int)   # Cria o defaultdict que retorna 0 para chaves novas
# for prod, qtd in vendas_tuplas:
#     soma[prod] += qtd # se prod não existir, vira 0 + qtd
# print(soma)  # {'camisa':4, 'calça':2}


# #Defaultdict com List
# from collections import defaultdict

# pedidos = [
#     ('Ana',    'camisa'),
#     ('Bruno',  'calça'),
#     ('Ana',    'boné'),
#     ('Ana',    'chinelo'),
#     ('Ana',    'vestido'),
#     ('Bruno',    'camisa')
# ]

# agrupado = defaultdict(list)

# for cliente, produto in pedidos:
#     agrupado[cliente].append(produto)

# print(dict(agrupado))
# print(agrupado)
# # {'Ana': ['camisa', 'boné'], 'Bruno': ['calça']}

#Trabalhando com Datas: Datetime
from datetime import date, datetime, timedelta

#Criando uma data atual
hoje = date.today()
print(hoje)

#Criando uma data específica
aniversario = date(1999, 3, 15)
print(aniversario)

#Criando um timestamp (data + hora)
agora = datetime.now()
print(agora)

#Criando um datetime específico
dt_evento = datetime(2025, 5, 20, 14, 30, 0)
print(dt_evento)


# #Converter String para Datetime (Parsing)
# from datetime import datetime

# texto = "2025-05-20 14:30"
# formato = "%Y-%m-%d %H:%M"
# dt = datetime.strptime(texto, formato) #“string parse time”.
# print(dt)

# #Converter Datetime em String
# from datetime import date, datetime

# hoje = date.today()
# # formata como "21/05/2025"
# print(hoje.strftime("%d/%m/%Y"))


# #para datetime completo
# agora = datetime.now()
# # ex.: "21-05-2025 14:45"
# print(agora.strftime("%d-%m-%Y %H:%M"))


# Criar e usar timedelta (diferenças e incrementos)
from datetime import date, datetime, timedelta
#Criar duração de dias, horas, etc.
dia = timedelta(days=1)
horas = timedelta(hours=7,minutes=15,seconds=47)

print(dia,horas)


#Somar/subtrair datas com timedelta

amanha = hoje + dia
anteontem = hoje - timedelta(days=2)

print("Amanhã:", amanha)
print("Anteontem:", anteontem)


#Diferença entre dois datetime
inicio = datetime(2025,5,20,9,0)
fim    = datetime(2025,5,20,17,30)
duracao = fim - inicio
print(duracao)                # 8:30:00
print(duracao.total_seconds())# 30600.0 segundos
