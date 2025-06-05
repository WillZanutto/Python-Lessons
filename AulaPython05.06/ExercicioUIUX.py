import sqlite3
import pandas as pd
import streamlit as st
import datetime as dt
import sqlite3
import csv
import matplotlib.pyplot as plt
import seaborn as sns

#Cria DF
df = pd.read_csv('AulaPython05.06\dados_vendas_acai.csv', sep=',', encoding='utf-8', parse_dates=['data_venda'])



st.title("Vendas de Açaí")

#Produtos mais vendidos (Top 5 ou Top 10)
#Grafico de Pizza com os Produto Mais Vendidos!
vendas_por_produto = df.groupby('produto')['quantidade'].sum()
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



#Ticket médio por forma de pagamento
media_vendas_por_cliente = df.groupby('forma_pagamento')['valor_total'].mean().sort_values(ascending=False)
st.subheader('Média de Ticket por forma de pagamento')
st.write(media_vendas_por_cliente)
st.write('\n')
st.write('\n')



#Clientes que mais compram (Top clientes)
vendas_por_cliente = df.groupby('cliente')['quantidade'].sum().sort_values(ascending=False)
st.subheader('Top 5 clientes que mais compram por quantidade')
st.write(vendas_por_cliente.head(5))
st.write('\n')
st.write('\n')




#Ticket médio por cliente
media_vendas_por_cliente = df.groupby('cliente')['valor_total'].mean().reset_index(name='media_venda')
media_vendas_por_cliente = media_vendas_por_cliente.sort_values(by='media_venda', ascending=True)
st.subheader('Média de Ticket por cliente')
st.write(media_vendas_por_cliente)
st.write('\n')
st.write('\n')



#Comparativo entre formas de pagamento (volume e valor)
vendas_por_categoria = df.groupby('forma_pagamento').agg(
    valor_total=('valor_total', 'sum'),
    quantidade_vendas=('valor_total', 'count')  # ou qualquer outra coluna
)
st.subheader('Comparativo entre formas de pagamento')
st.write(vendas_por_categoria)


#Comparação mês a mês
df_mês = df
df_mês['ano_mes'] = df_mês['data_venda'].dt.to_period('M')

vendas_mensais = df.groupby('ano_mes')['valor_total'].sum().reset_index()
vendas_mensais['ano_mes'] = vendas_mensais['ano_mes'].astype(str)

st.write(vendas_mensais)