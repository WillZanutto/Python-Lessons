import pandas as pd

#Le o arquivo CSV e cria um DataFrame
df = pd.read_csv('vendas.csv', sep=',', encoding='utf-8', parse_dates=['data'])

#calcula a quantidade total de vendas
total_vendas = len(df)
print(f'O total de vendas foi: {total_vendas}')
print('---------------------------------------------')

#calcula o total do faturamento
faturamento = (df['quantidade'] * df['preco']).sum()
print(f'O faturamento foi: {faturamento:.2f}')
print('---------------------------------------------')

#calcula o valor médio por venda
valor_medio_venda = faturamento / total_vendas
print(f'O valor médio das vendas foi: {valor_medio_venda:.2f}')
print('---------------------------------------------')

#Mostra os 3 mais vendidos
top3 = df['produto'].value_counts('quantidade').head(3)
print(f'Os 3 produtos mais vendidos foram: {top3}')
print('---------------------------------------------')

#Cria uma coluna com o Total e mostra as 5 maiores vendas
df['total'] = df['preco'] * df['quantidade']
# top5 = df['total'].sort_values(ascending=False).head(5)
top5 = df.nlargest(5, 'total')
print('As 5 maiores vendas foram:')
print(top5)
print('---------------------------------------------')

#Filtra apenas as vendas do mês de Abril e cria um novo arquivo CSV
abril = df.loc[df['data'].dt.month == 4]
relatorio_abril = abril.copy()

relatorio_abril.to_csv('relatórioabril.csv', index=False)
