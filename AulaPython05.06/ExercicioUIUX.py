import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime
import sqlite3
import csv
import matplotlib.pyplot as plt
import seaborn as sns

#Cria DF
df = pd.read_csv('AulaPython05.06\dados_vendas_acai.csv', sep=',', encoding='utf-8', parse_dates=['data_venda'])


# 📦 Conecta (ou cria) o banco de dados SQLite
# conn = sqlite3.connect("AulaPython05.06/vendas-acai.db", check_same_thread=False)
# cursor = conn.cursor()

# # Criação da tabela clientes (DDL)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS vendas (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     data_venda TEXT NOT NULL,
#     cliente TEXT NOT NULL,
#     produto TEXT NOT NULL,
#     quantidade INTEGER NOT NULL,
#     forma_pagamento TEXT NOT NULL,
#     preco_unitario REAL NOT NULL,
#     valor_total REAL NOT NULL,
#     categoria TEXT NOT NULL
# )
# ''')

# cursor.execute("SELECT COUNT(*) FROM vendas")
# if cursor.fetchone()[0] == 0:
#     df_vendas = pd.read_csv('AulaPython05.06/dados_vendas_acai.csv')
#     df_vendas.to_sql('vendas', conn, if_exists='append', index=False)


st.title("Vendas de Açaí")

# df_group = pd.read_sql_query('''
#     SELECT
#         produto, quantidade
#     FROM vendas
#     GROUP BY quantidade
# ''', conn)

df_group_produto = df.groupby('produto').agg({
    'quantidade': 'sum',
    'preco_unitario': 'max',
    'valor_total': 'sum'
}).sort_values(['quantidade'], ascending=False)
st.write(df_group_produto)

vendas_por_produto = df.groupby('produto')['quantidade'].sum()

df_top5_vendas = df_group_produto.head(5)

st.write(vendas_por_produto)

# fig1, ax1 = plt.subplots()
# plt.figure(figsize=(8,8))
# vendas_por_produto.plot.pie(autopct='%1.1f%%', startangle=90, ax=ax1)
# plt.title('Produtos mais vendidos')
# plt.ylabel('')  # remove label do eixo y para deixar mais limpo
# st.pyplot(fig1)

# plt.figure(figsize=(8,8))
# plt.pie(vendas_por_produto['quantidade'], 
#         labels=vendas_por_produto['produto'], 
#         autopct='%1.1f%%', 
#         startangle=90)
# plt.title('Produtos mais vendidos')
# plt.show()

data = vendas_por_produto
labels = vendas_por_produto
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
sns.set_style("darkgrid")
plt.pie(data, labels=labels, colors=colors)

# Add title
plt.title("Distribution of Data")

# Show plot
plt.show()