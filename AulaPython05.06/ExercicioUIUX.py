import sqlite3
import pandas as pd
import streamlit as st
import datetime as dt
import sqlite3
import csv
import matplotlib.pyplot as plt
import seaborn as sns

#Cria DF
df = pd.read_csv('AulaPython05.06/dados_vendas_acai.csv', sep=',', encoding='utf-8', parse_dates=['data_venda'])

def mes(data_mes):
    mes_str = {
        'January': 'Janeiro',
        'February': 'Fevereiro',
        'March': 'Março',
        'April': 'Abril',
        'May': 'Maio',
        'June': 'Junho',
        'July': 'Julho',
        'August': 'Agosto',
        'September': 'Setembro',
        'October': 'Outubro',
        'November': 'Novembro',
        'December': 'Dezembro'
    }
    # data = dt.strptime(data_completa, "%Y-%m-%d %H:%M:%S")
    # mes_num = data.strftime("%M")
    return mes_str[data_mes]

# conn = sqlite3.connect("AulaPython29.05/biblioteca.db", check_same_thread=False)
# cursor = conn.cursor()
# # 🏗️ Criação da tabela livros (DDL)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS livros (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     titulo TEXT NOT NULL,
#     autor_id INTEGER NOT NULL,
#     categoria_id INTEGER NOT NULL,
#     ano TEXT NOT NULL,
#     quantidade_disponivel INTEGER NOT NULL,
#     FOREIGN KEY(autor_id) REFERENCES autores(id),
#     FOREIGN KEY(categoria_id) REFERENCES categorias(id)
# )
# ''')

st.title("Dashboard Sorveteria")

#BIG NUMBERS
total_clientes = df['cliente'].nunique()
vendas_por_produto = df.groupby('produto')['quantidade'].sum().sort_values(ascending=False)
produto_mais_vendido = vendas_por_produto.index[0]
vendas_total_por_produto = df.groupby('produto')['valor_total'].sum().sort_values(ascending=False)
produto_mais_lucrativo = vendas_total_por_produto.index[0]
total_vendas = df['valor_total'].sum()
ticket_medio = df['valor_total'].mean()
quantidade_vendida = df['quantidade'].sum()

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col1.metric('Quantidade de Clientes', f'{total_clientes}')
col2.metric('Produto mais vendido', f'{produto_mais_vendido}')
col3.metric('Produto mais lucrativo', f'{produto_mais_lucrativo}')
col4.metric('Valor total de vendas', f'R$ {total_vendas:.2f}')
col5.metric('Ticket médio', f'R$ {ticket_medio:.2f}')
col6.metric('Quantidade total vendida', f'{quantidade_vendida}')



#Gráfico com evolução dos meses
df['mes'] = df['data_venda'].dt.month_name()
df['mes'] = df['mes'].apply(mes)

mes_ordem = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
df['mes'] = pd.Categorical(df['mes'], categories=mes_ordem, ordered=True)
evolucao_meses = df.groupby('mes')['valor_total'].sum().reset_index()
st.write(evolucao_meses)
plt.figure(figsize=(10, 5))
sns.lineplot(data=evolucao_meses, x='mes', y='valor_total', marker='o')
plt.title('Evolução Mensal das Vendas')
plt.xlabel('Mês')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=45)

# Mostrar gráfico no Streamlit
st.pyplot(plt.gcf())
plt.clf()



#Produtos mais vendidos (Top 5 ou Top 10)
#Grafico de Pizza com os Produto Mais Vendidos!
st.write(vendas_por_produto)

n = len(vendas_por_produto)
paleta = sns.light_palette("purple", n_colors=n, reverse=True)
fig1, ax1 = plt.subplots(figsize=(6,6))
vendas_por_produto.plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    labels=None,  
    colors=paleta,
    ax=ax1
)
plt.title('Produtos mais vendidos')
ax1.legend(
    labels=vendas_por_produto.index,
    loc='center left',  
    bbox_to_anchor=(1, 0.5)  
)
ax1.set_xlabel('')
ax1.set_ylabel('')
st.pyplot(fig1)
st.write('\n')
st.write('\n')


#Categorias mais lucrativas
# vendas_por_categoria = df.groupby('categoria')['valor_total'].sum()
vendas_por_categoria = df.groupby('categoria').agg({
    'valor_total': 'sum'
})
st.write(vendas_por_categoria)

fig2, ax2 = plt.subplots()
sns.barplot(data=vendas_por_categoria, x='categoria',y='valor_total', ax=ax2)
# plt.xticks(rotation=90)
plt.title("Valor Total de Vendas por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Valor Total")
st.pyplot(fig2)
st.write('\n')
st.write('\n')



#Vendas por hora do dia
df['hora_venda'] = df['data_venda'].dt.hour
vendas_por_hora = df.groupby('hora_venda')['quantidade'].sum().reset_index()

st.subheader("Gráfico de Vendas por Hora", divider='grey')
st.bar_chart(vendas_por_hora.set_index(f'hora_venda'))



#Ticket médio por forma de pagamento
media_vendas_por_cliente = df.groupby('forma_pagamento')['valor_total'].mean().sort_values(ascending=False)
st.subheader('Média de Ticket por forma de pagamento', divider='grey')
st.write(media_vendas_por_cliente)
st.write('\n')
st.write('\n')



#Clientes que mais compram (Top clientes)
vendas_por_cliente = df.groupby('cliente')['quantidade'].sum().sort_values(ascending=False)
st.subheader('Top 5 clientes que mais compram por quantidade', divider='grey')
st.write(vendas_por_cliente.head(5))
st.write('\n')
st.write('\n')




#Ticket médio por cliente
media_vendas_por_cliente = df.groupby('cliente')['valor_total'].mean().reset_index(name='media_venda')
media_vendas_por_cliente = media_vendas_por_cliente.sort_values(by='media_venda', ascending=True)
st.subheader('Média de Ticket por cliente', divider='grey')
st.write(media_vendas_por_cliente)
st.write('\n')
st.write('\n')



#Comparativo entre formas de pagamento (volume e valor)
vendas_por_categoria = df.groupby('forma_pagamento').agg(
    valor_total=('valor_total', 'sum'),
    quantidade_vendas=('valor_total', 'count')  # ou qualquer outra coluna
)
st.subheader('Comparativo entre formas de pagamento', divider='grey')
st.write(vendas_por_categoria)


#Comparação mês a mês
df_mês = df
df_mês['ano_mes'] = df_mês['data_venda'].dt.to_period('M')

vendas_mensais = df.groupby('ano_mes')['valor_total'].sum().reset_index()
vendas_mensais['ano_mes'] = vendas_mensais['ano_mes'].astype(str)
st.subheader('Comparativo Mês a Mês', divider='grey')
st.write(vendas_mensais)