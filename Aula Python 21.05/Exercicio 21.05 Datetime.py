import csv
from datetime import date, datetime, timedelta
from collections import defaultdict, Counter

#pega a data de hoje
hoje = datetime.today()
tempo = timedelta(days=30)
vendastrintadias = []
vendasmes = defaultdict(int)
vendasmaio = []

#lê arquivo CSV e cria uma lista com os produtos
with open('vendas.csv', mode='r', encoding='utf-8',newline='') as vendas:
    leitor = csv.reader(vendas, delimiter=',')
    header = next(leitor)
    for linha in leitor:
        ordem = dict(zip(header, linha))

        #Converte a string Data para Datetime e Printa
        data = ordem['data']
        dt = datetime.strptime(data, "%Y-%m-%d")
        print(dt)

        #printa a diferença entre a Data do Arquivo e a Data de Hoje
        print(f"A diferença de tempo para a data de hoje é: {hoje - dt}")
        print('-------------------------------------------------------------')

        #Valida se a venda foi feita nos ultimos 30 dias e adiciona à lista
        if (hoje - dt) < tempo:
            vendastrintadias.append(ordem)

        ano_mes = datetime.strftime(dt, '%Y-%m')
        vendasmes[ano_mes] += 1

        if ano_mes == '2025-05':
            vendasmaio.append(ordem)

#Printa a Lista com as vendas dos ultimos 30 dias
print(vendastrintadias)
print('-------------------------------------------------------------')

#Printa a quantidade de vendas por mes
print(vendasmes)
print('-------------------------------------------------------------')

#printa a quantidade de vendas em Maio
print(vendasmaio)
print('-------------------------------------------------------------')


#calcula a duração do expediente
#início do expediente
inicio = datetime.strptime('09:00', '%H:%M')

#fim do expediente
fim = datetime.strptime('17:30', '%H:%M')

#calcula a duração do expediente
duracao = fim - inicio
print(f'A duração do expediente é: {duracao}')
print('-------------------------------------------------------------') 


#Retorna o dia da semana em português
def dia_da_semana(data_str):
    dias_pt = {
        'Monday': 'Segunda-feira',
        'Tuesday': 'Terça-feira',
        'Wednesday': 'Quarta-feira',
        'Thursday': 'Quinta-feira',
        'Friday': 'Sexta-feira',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }
    data = datetime.strptime(data_str, "%Y-%m-%d")
    dia_en = data.strftime("%A")
    return dias_pt[dia_en]

#Recebe data no formato YYYY-MM-DD do usuario
data_semana = input("Digite a data no formato YYYY-MM-DD: ")
print('-------------------------------------------------------------')

# Chama a função e imprime o resultado:
print(dia_da_semana(data_semana))
print('-------------------------------------------------------------')



# Cria uma lista com os proximos 15 dias
hoje = datetime.today()
proximos_dias = []

# Monta a lista com os proximos 15 dias
for i in range(1, 16):
    proximo_dia = hoje + timedelta(days=i)
    proximos_dias.append(proximo_dia.strftime("%Y-%m-%d"))

# Printa a lista com os proximos 15 dias
print(proximos_dias)
print('-------------------------------------------------------------')  


hoje = datetime.today()
garantia = timedelta(days=90)

#lê arquivo CSV e verifica se a venda está dentro dos 90 dias de garantia
with open('vendas.csv', mode='r', encoding='utf-8',newline='') as vendas:
    leitor = csv.reader(vendas, delimiter=',')
    header = next(leitor)
    for linha in leitor:
        ordem = dict(zip(header, linha))

        #Converte a string Data para Datetime
        data = ordem['data']
        dt = datetime.strptime(data, "%Y-%m-%d")

        if (hoje - dt) < garantia:
            print(f"Produto {ordem['produto']} está dentro da garantia. Data da compra: {dt}")
            print('-------------------------------------------------------------')


#Calcula a média de dias entre vendas de cada produto
def media_dias_entre_vendas(caminho_csv):
    datas_por_produto = defaultdict(list)

    # Ler o CSV e agrupar datas por produto
    with open('vendas.csv', mode='r', encoding='utf-8',newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            produto = linha['produto']
            data = datetime.strptime(linha['data'], "%Y-%m-%d")
            datas_por_produto[produto].append(data)

    # Calcular média de dias entre vendas para cada produto
    medias = {}
    for produto, datas in datas_por_produto.items():
        datas.sort()  # Ordenar datas do produto
        if len(datas) < 2:
            medias[produto] = None  # Sem média com apenas uma venda
        else:
            diferencas = [
                (datas[i] - datas[i-1]).days for i in range(1, len(datas))
            ]
            media = sum(diferencas) / len(diferencas)
            medias[produto] = media

    return medias

# Exemplo de uso
medias = media_dias_entre_vendas('vendas.csv')
for produto, media in medias.items():
    if media is not None:
        print(f"{produto}: média de {media:.2f} dias entre vendas")
    else:
        print(f"{produto}: apenas uma venda registrada")
        
print('-------------------------------------------------------------')