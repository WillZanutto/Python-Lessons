import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_estatistica_visualizacao.csv', sep=',', encoding='utf-8')
print(df)
print('--------------------------------------------------')


#1. Resumo estatístico das colunas idade e salario.
#Média
print("Média idade:", df['idade'].mean(),'\n')
print("Média salario:", df['salario'].mean(),'\n')
print('--------------------------------------------------')

#moda
print("Moda idade:", df['idade'].mode(),'\n')
print("Moda salario:", df['salario'].mode(),'\n')
print('--------------------------------------------------')

#mediana
print("Mediana idade:", df['idade'].median(),'\n')
print("Mediana salario:", df['salario'].median(),'\n')
print('--------------------------------------------------')

#variância
print("Variância idade:", df['idade'].var(),'\n')
print("Variância salario:", df['salario'].var(),'\n')
print('--------------------------------------------------')

#Amplitude (max - min)
print("Amplitude idade:", df['idade'].max() - df['idade'].min(),'\n')
print("Amplitude salario:", df['salario'].max() - df['salario'].min(),'\n')
print('--------------------------------------------------')


#-----------------------------------------------------------------------------------------------------------------------------
#2. Criação de uma nova coluna "Faixa Etária"
def calcula_faixa_etaria(idade):
    if idade <= 25:
        return 'Jovem'
    elif 26 <= idade <= 45:
        return 'Adulto'
    else:
        return 'Sênior'
    

df['Faixa Etária'] = df['idade'].apply(calcula_faixa_etaria)
print(df)
print('--------------------------------------------------')



#-----------------------------------------------------------------------------------------------------------------------------
#3. Visualizações
#Gráfico de barras com a distribuição por estado.

# fig1, ax1 = plt.subplots()
plt.hist(df['estado'], bins=10) # qtd de barras
plt.title("Distribuição de Estados")
plt.xlabel("Estado")
plt.ylabel("Frequência")
# plt.show()
# st.pyplot(fig1)

# fig2, ax2 = plt.subplots()
#Boxplot de salário por departamento
sns.boxplot(x='departamento', y='salario', data=df)
# plt.show()
# st.pyplot(fig2)

#Gráfico de dispersão entre idade e salario, colorido por departamento.
sns.scatterplot(x='idade', y='salario', hue='departamento', data=df)
# plt.show()



#-----------------------------------------------------------------------------------------------------------------------------
# import streamlit as st

st.title("Painel de Análise de Funcionários")

coluna = st.sidebar.selectbox("Escolha uma coluna numérica", ['idade', 'salario', 'departamento'])

# st.subheader(f'Estatisticas de {coluna}', divider = True)
st.subheader(f'Estatisticas de {coluna}', divider = 'grey')
st.write(f'Média {coluna}: {df[coluna].mean()}')
st.write(f'Moda {coluna}: {df[coluna].mode()}')
st.write(f'Mediana {coluna}: {df[coluna].median()}')
st.write(f'Variância {coluna}: {df[coluna].var()}')
st.write(f'Amplitude {coluna}: {df[coluna].max() - df[coluna].min()}')


st.subheader('Gráfico de Distribuição de Estados', divider = 'grey')
fig1, ax1 = plt.subplots()
sns.countplot(x='estado', data=df, ax=ax1)
st.pyplot(fig1)


st.subheader('Gráfico de Salário Por Departamento', divider = 'grey')
fig2, ax2 = plt.subplots()
sns.boxplot(x='departamento', y='salario', data=df, ax=ax2)
st.pyplot(fig2)


st.subheader('Gráfico de dispersão entre idade e salario, colorido por departamento', divider = 'grey')
fig3, ax3 = plt.subplots()
sns.scatterplot(x='idade', y='salario', hue='departamento', data=df)
st.pyplot(fig3)

