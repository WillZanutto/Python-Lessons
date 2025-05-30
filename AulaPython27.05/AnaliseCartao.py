import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# st.title("Analise Cancelamento Cartões")
st.markdown("<h1 style='text-align: center;'>Analise Cancelamento Cartões</h1>", unsafe_allow_html=True)

df = pd.read_csv('clientes.csv', sep=',', encoding='utf-8')

df_cancelados = df.loc[(df['Categoria'] == 'Cancelado')]
df_cancelados.to_csv('clientes_cancelados.csv')


st.subheader(f'Distribuição do Tempo de Inatividade', divider = 'grey')
fig1, ax1 = plt.subplots()
sns.countplot(data=df, x='Inatividade 12m', hue='Categoria', ax=ax1)
plt.title("Distribuição do Tempo de Inatividade por Categoria")
plt.xlabel("Meses Inativos")
plt.ylabel("Quantidade de Clientes")
st.pyplot(fig1)
st.write('Com base no gráfico de Inatividade por Categoria. Podemos concluir que o tempo de inatividade nos ultimos 12 meses pode ser um fator que leva ao cancelamento.' \
'Pois muitos clientes cancelados apresentam mais meses de inatividade. E muitos cancelamentos ocorrem entre os meses 2 e 4 de inatividade.')
st.write('\n')
st.write('\n')


ordem = ['Less than $40K', '$40K - $60K', '$60K - $80K', '$80K - $120K', '$120K +', 'Não informado']

st.subheader(f'Distribuição da Faixa Salarial por Categoria', divider = 'grey')
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x='Faixa Salarial Anual', hue='Categoria', order=ordem, ax=ax2)
plt.xticks(rotation=45)
plt.title("Distribuição da Faixa Salarial por Categoria")
plt.xlabel("Faixa Salarial")
plt.ylabel("Quantidade de Clientes")
st.pyplot(fig2)
st.write('Com esse gráfico podemos concluir que clientes com menor renda anual estão mais propensos a cancelar o cartão, talvez por dificuldades financeiras ou menor relevância ' \
'do cartão no cotidiano. A maior parte dos cancelamento estão na faixa salarial à baixa dos $40k anual.')
st.write('\n')
st.write('\n')


st.subheader(f'Distribuição Nivel de Educação dos Cancelados', divider = 'grey')
fig3, ax3 = plt.subplots()
sns.countplot(data=df_cancelados, x='Educação', ax=ax3)
plt.xticks(rotation=90)
plt.title("Distribuição Nivel de Educação dos Cancelados")
plt.xlabel("Nivel Educação")
plt.ylabel("Quantidade de Clientes")
st.pyplot(fig3)
st.write('Com esse gráfico podemos concluir que existe um volume maior de cancelamentos em clientes com nível educacional intermediário, o que pode indicar menor fidelização ' \
'ou menor acesso a benefícios mais atrativos do cartão.')
st.write('\n')
st.write('\n')


st.subheader(f'Distribuição Quantidade de Contatos nos Ultimos 12m', divider = 'grey')
fig3, ax3 = plt.subplots()
sns.countplot(data=df, x='Contatos 12m', hue='Categoria', ax=ax3)
plt.title("Distribuição Quantidade de Contatos nos Ultimos 12m")
plt.xlabel("Numero de Contatos")
plt.ylabel("Quantidade de Clientes")
st.pyplot(fig3)
st.write('Nesse gráfico podemos verificar que os cliente cancelados tendem a ter mais interações com o banco antes de sair. ' \
'Os picos de contato nos valores mais altos (ex: 4, 5, 6 contatos) são fortemente associados a cancelamento. Um aumento nos contatos com o atendimento pode ser um sinal ' \
'de insatisfação ou tentativa de resolver problemas antes de cancelar')

st.write('\n')
st.write('\n')
st.write('\n')
st.subheader(f'Conclusões', divider = 'grey')
st.write('1. Baixa utilização do cartão (em transações e limite) está fortemente associada ao cancelamento.')
st.write('2. Clientes com renda mais baixa e uso esporádico do cartão são os que mais cancelam.')
st.write('3. Muitos contatos recentes com o banco sugerem uma experiência negativa ou tentativa de resolução de problemas.')
st.write('4. A inatividade por 2 ou mais meses é um claro sinal de risco.')

st.write('\n')
st.write('\n')
st.write('\n')
st.subheader(f'Plano de Ação', divider = 'grey')
st.write('Campanhas de engajamento personalizadas devem focar em:')
st.write('1. Clientes inativos nos últimos 2 meses')
st.write('2. Clientes que realizaram múltiplos contatos.')
st.write('3. Clientes com baixo uso do limite e transações reduzidas.')
st.write('4. Faixas salariais até $60K.')