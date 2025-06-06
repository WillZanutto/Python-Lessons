import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Simulação de dados (mesmo esquema anterior)
np.random.seed(42)
n_vendas = 500
datas = pd.date_range(start='2024-01-01', end='2024-04-30')
formas_pagamento = ['Dinheiro', 'Cartão', 'Pix', 'Boleto']
clientes = [f'Cliente {i}' for i in range(1, 51)]
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros']
produtos_por_categoria = {
    'Eletrônicos': ['Smartphone', 'Notebook', 'Fone de Ouvido'],
    'Roupas': ['Camisa', 'Calça', 'Tênis'],
    'Alimentos': ['Arroz', 'Feijão', 'Macarrão'],
    'Livros': ['Ficção', 'Não Ficção', 'Quadrinhos']
}

dados = []
for _ in range(n_vendas):
    data = np.random.choice(datas)
    forma = np.random.choice(formas_pagamento)
    cliente = np.random.choice(clientes)
    categoria = np.random.choice(categorias)
    produto = np.random.choice(produtos_por_categoria[categoria])
    quantidade = np.random.randint(1, 5)
    preco_unit = np.random.uniform(10, 500)
    valor_total = round(preco_unit * quantidade, 2)
    dados.append([data, forma, cliente, categoria, produto, quantidade, preco_unit, valor_total])

df = pd.DataFrame(dados, columns=['data', 'forma_pagamento', 'cliente', 'categoria', 'produto', 'quantidade', 'preco_unit', 'valor_total'])
df['data'] = pd.to_datetime(df['data'])

# Título
st.title("Dashboard de Vendas Interativo")

# Filtros
st.sidebar.header("Filtros")

data_min = df['data'].min()
data_max = df['data'].max()
data_selec = st.sidebar.date_input("Período", [data_min, data_max], min_value=data_min, max_value=data_max)

formas_selec = st.sidebar.multiselect(
    "Forma de Pagamento",
    options=sorted(df['forma_pagamento'].unique()),
    default=None
)

clientes_selec = st.sidebar.multiselect(
    "Clientes",
    options=sorted(df['cliente'].unique()),
    default=None
)

# Filtragem dos dados
dff = df.copy()
# Filtra data
if len(data_selec) == 2:
    dff = dff[(dff['data'] >= pd.to_datetime(data_selec[0])) & (dff['data'] <= pd.to_datetime(data_selec[1]))]

# Filtra forma_pagamento
if formas_selec:
    dff = dff[dff['forma_pagamento'].isin(formas_selec)]

# Filtra cliente
if clientes_selec:
    dff = dff[dff['cliente'].isin(clientes_selec)]

# Indicadores
total_vendas = dff['valor_total'].sum()
ticket_medio = dff['valor_total'].mean() if not dff.empty else 0
quantidade_vendida = dff['quantidade'].sum()
num_clientes = dff['cliente'].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Vendas (R$)", f"{total_vendas:,.2f}")
col2.metric("Ticket Médio (R$)", f"{ticket_medio:,.2f}")
col3.metric("Quantidade Vendida", f"{quantidade_vendida}")
col4.metric("Clientes Únicos", f"{num_clientes}")

st.markdown("---")

# Gráfico 1: Evolução das vendas
vendas_por_data = dff.groupby('data')['valor_total'].sum().reset_index()
fig_evolucao = px.line(vendas_por_data, x='data', y='valor_total', title='Evolução das Vendas', labels={'valor_total':'Valor Total (R$)', 'data':'Data'})
st.plotly_chart(fig_evolucao, use_container_width=True)

# Gráfico 2: Top 5 produtos mais vendidos (quantidade)
top_produtos = dff.groupby('produto')['quantidade'].sum().sort_values(ascending=False).head(5).reset_index()
fig_top_produtos = px.bar(top_produtos, x='produto', y='quantidade', title='Top 5 Produtos Mais Vendidos (Quantidade)', labels={'quantidade':'Quantidade Vendida', 'produto':'Produto'})
st.plotly_chart(fig_top_produtos, use_container_width=True)

# Gráfico 3: Vendas por categoria (valor total)
vendas_categoria = dff.groupby('categoria')['valor_total'].sum().reset_index().sort_values(by='valor_total', ascending=False)
fig_categoria = px.pie(vendas_categoria, names='categoria', values='valor_total', title='Vendas por Categoria (Valor Total)')
st.plotly_chart(fig_categoria, use_container_width=True)

# Gráfico 4: Ticket médio por forma de pagamento
ticket_forma = dff.groupby('forma_pagamento')['valor_total'].mean().reset_index().sort_values(by='valor_total', ascending=False)
fig_ticket_forma = px.bar(ticket_forma, x='forma_pagamento', y='valor_total', title='Ticket Médio por Forma de Pagamento', labels={'valor_total':'Ticket Médio (R$)', 'forma_pagamento':'Forma de Pagamento'})
st.plotly_chart(fig_ticket_forma, use_container_width=True)
