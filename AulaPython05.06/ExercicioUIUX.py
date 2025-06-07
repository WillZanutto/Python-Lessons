import pandas as pd
import streamlit as st
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

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
    return mes_str[data_mes]



# Filtros
st.sidebar.header("Filtros")

data_min = df['data_venda'].min()
data_max = df['data_venda'].max()
data_selec = st.sidebar.date_input("data_venda", [data_min, data_max], min_value=data_min, max_value=data_max)

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

produtos_selec = st.sidebar.multiselect(
    "Produtos",
    options=sorted(df['produto'].unique()),
    default=None
)

# Filtragem dos dados
dff = df.copy()
# Filtra data
if len(data_selec) == 2:
    dff = dff[(dff['data_venda'] >= pd.to_datetime(data_selec[0])) & (dff['data_venda'] <= pd.to_datetime(data_selec[1]))]

# Filtra forma_pagamento
if formas_selec:
    dff = dff[dff['forma_pagamento'].isin(formas_selec)]

# Filtra cliente
if clientes_selec:
    dff = dff[dff['cliente'].isin(clientes_selec)]

if produtos_selec:
    dff = dff[dff['produto'].isin(produtos_selec)]

st.title("Dashboard Sorveteria")



#BIG NUMBERS
total_clientes = dff['cliente'].nunique()
vendas_por_produto = dff.groupby('produto')['quantidade'].sum().sort_values(ascending=False)
produto_mais_vendido = vendas_por_produto.index[0]
vendas_total_por_produto = dff.groupby('produto')['valor_total'].sum().sort_values(ascending=False)
produto_mais_lucrativo = vendas_total_por_produto.index[0]
total_vendas = dff['valor_total'].sum()
ticket_medio = dff['valor_total'].mean()
quantidade_vendida = dff['quantidade'].sum()

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col1.metric('Quantidade de Clientes', f'{total_clientes}')
col2.metric('Produto mais vendido', f'{produto_mais_vendido}')
col3.metric('Produto mais lucrativo', f'{produto_mais_lucrativo}')
col4.metric('Valor total de vendas', f'R$ {total_vendas:.2f}')
col5.metric('Ticket médio', f'R$ {ticket_medio:.2f}')
col6.metric('Quantidade total vendida', f'{quantidade_vendida}')



#Gráfico com evolução dos meses
col7, col8 = st.columns(2)
dff['mes'] = dff['data_venda'].dt.month_name()
dff['mes'] = dff['mes'].apply(mes)

mes_ordem = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
dff['mes'] = pd.Categorical(dff['mes'], categories=mes_ordem, ordered=True)
evolucao_meses = dff.groupby('mes')['valor_total'].sum().reset_index()
with col7:
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
n = len(vendas_por_produto)
with col8:
    paleta = sns.light_palette("purple", n_colors=n, reverse=True)
    fig1, ax1 = plt.subplots(figsize=(10,5))
    vendas_por_produto.plot.pie(
        autopct='%1.1f%%',
        startangle=90,
        labels=None,  
        colors=paleta,
        ax=ax1,
        subplots=True
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
col9, col10 = st.columns(2)
# vendas_por_categoria = dff.groupby('categoria')['valor_total'].sum()
vendas_por_categoria = dff.groupby('categoria').agg({
    'valor_total': 'sum'
})

with col9:
    #Total de venda por categoria
    fig2, ax2 = plt.subplots()
    sns.barplot(data=vendas_por_categoria, x='categoria',y='valor_total', ax=ax2)
    # plt.xticks(rotation=90)
    plt.title("Valor Total de Vendas por Categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Valor Total")
    st.pyplot(fig2)
    st.write('\n')
    st.write('\n')



#Clientes que mais compram (Top clientes)
with col10:
    vendas_por_cliente = df.groupby('cliente')['quantidade'].sum().sort_values(ascending=False)
    top_5 = vendas_por_cliente.head(5)
    paleta = sns.light_palette("purple", n_colors=n, reverse=True)
    fig3, ax3 = plt.subplots()
    ax3.pie(
        top_5.values,
        labels=top_5.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=paleta  # paleta de cores
    )
    plt.title('Top 5 Clientes Por Quantidade Vendida')
    ax3.axis('equal')  # mantém o gráfico em forma de círculo

    # Exibir gráfico
    st.pyplot(fig3)



#Vendas por hora do dia
dff['hora_venda'] = dff['data_venda'].dt.hour
vendas_por_hora = dff.groupby('hora_venda')['quantidade'].sum().reset_index()

st.subheader("Gráfico de Vendas por Hora do Dia", divider='grey')
st.bar_chart(vendas_por_hora.set_index(f'hora_venda'))
st.write('\n')
st.write('\n')



#Ticket médio por forma de pagamento
media_vendas_por_cliente = df.groupby('forma_pagamento')['valor_total'].mean().sort_values(ascending=False)
st.subheader('Média de Ticket por forma de pagamento', divider='grey')
st.write(media_vendas_por_cliente)
st.write('\n')
st.write('\n')




#Ticket médio por cliente
media_vendas_por_cliente = dff.groupby('cliente')['valor_total'].mean().reset_index(name='media_venda')
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
st.write('\n')
st.write('\n')



#Tabela dinâmica com agrupamentos por cliente, categoria, mês
tabela_dinamica = dff.pivot_table(
    index=['cliente', 'categoria'],
    columns='mes',
    values='valor_total',
    aggfunc='sum',
    fill_value=0
).reset_index()
st.subheader('Tabela Dinâmica de Vendas', divider='grey')
st.write(tabela_dinamica)