import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_alunos_escola.csv', sep=',', encoding='utf-8')

st.title("Exercicio de Streamlit")

#Estatísticas Descritivas
#1. Calcule a média, mediana, moda, variância, amplitude e desvio padrão das notas de matemática, português e ciências.

st.subheader(f'Estatísticas Descritivas', divider = 'grey')

media_matematica = df['nota_matematica'].mean()
print(f"Média Matemática: {media_matematica:.2f}")
st.write(f"Média Matemática: {media_matematica:.2f}")
media_portugues = df['nota_portugues'].mean()
print(f"Média Português: {media_portugues:.2f}")
st.write(f"Média Português: {media_portugues:.2f}")
media_ciencias = df['nota_ciencias'].mean()
print(f"Média Ciências: {media_ciencias:.2f}")
st.write(f"Média Ciências: {media_ciencias:.2f}")
print('----------------------------------------------------')

mediana_matematica = df['nota_matematica'].median()
print(f"Mediana Matemática: {mediana_matematica:.2f}")
st.write(f"Mediana Matemática: {mediana_matematica:.2f}")
mediana_portugues = df['nota_portugues'].median()
print(f"Mediana Português: {mediana_portugues:.2f}")
st.write(f"Mediana Português: {mediana_portugues:.2f}")
mediana_ciencias = df['nota_ciencias'].median()
print(f"Mediana Ciências: {mediana_ciencias:.2f}")
st.write(f"Mediana Ciências: {mediana_ciencias:.2f}")
print('----------------------------------------------------')

moda_matematica = df['nota_matematica'].mode().values[0]
print(f"Moda Matemática: {moda_matematica:}")
st.write(f"Moda Matemática: {moda_matematica:}")
moda_portugues = df['nota_portugues'].mode().values[0]
print(f"Moda Português: {moda_portugues:}")
st.write(f"Moda Português: {moda_portugues:}")
moda_ciencias = df['nota_ciencias'].mode().values[0]
print(f"Moda Ciências: {moda_ciencias:}")
st.write(f"Moda Ciências: {moda_ciencias}")
print('----------------------------------------------------')

variancia_matematica = df['nota_matematica'].var()
print(f"Variancia Matemática: {variancia_matematica:.2f}")
st.write(f"Variancia Matemática: {variancia_matematica:.2f}")
variancia_portugues = df['nota_portugues'].var()
print(f"Variancia Português: {variancia_portugues:.2f}")
st.write(f"Variancia Português: {variancia_portugues:.2f}")
variancia_ciencias = df['nota_ciencias'].var()
print(f"Variancia Ciências: {variancia_ciencias:.2f}")
st.write(f"Variancia Ciências: {variancia_ciencias:.2f}")
print('----------------------------------------------------')

amplitude_matematica = df['nota_matematica'].max() - df['nota_matematica'].min()
print(f"Amplitude Matemática: {amplitude_matematica:.2f}")
st.write(f"Amplitude Matemática: {amplitude_matematica:.2f}")
amplitude_portugues = df['nota_portugues'].max() - df['nota_portugues'].min()
print(f"Amplitude Português: {amplitude_portugues:.2f}")
st.write(f"Amplitude Português: {amplitude_portugues:.2f}")
amplitude_ciencias = df['nota_ciencias'].max() - df['nota_ciencias'].min()
print(f"Amplitude Ciências: {amplitude_ciencias:.2f}")
st.write(f"Amplitude Ciências: {amplitude_ciencias:.2f}")
print('----------------------------------------------------')

desvio_matematica = df['nota_matematica'].std()
print(f"Desvio Padrão Matemática: {desvio_matematica:.2f}")
st.write(f"Desvio Padrão Matemática: {desvio_matematica:.2f}")
desvio_portugues = df['nota_portugues'].std()
print(f"Desvio Padrão Português: {desvio_portugues:.2f}")
st.write(f"Desvio Padrão Português: {desvio_portugues:.2f}")
desvio_ciencias = df['nota_ciencias'].std()
print(f"Desvio Padrão Ciências: {desvio_ciencias:.2f}")
st.write(f"Desvio Padrão Ciências: {desvio_ciencias:.2f}")
print('----------------------------------------------------')


#2. Qual é a frequência média dos alunos por série?
frequencia_serie = df.groupby('serie')['frequencia_%'].mean()
print(frequencia_serie)
st.write('\n')
st.write('Frequencia média por Série')
st.write(frequencia_serie)
print('----------------------------------------------------')




#------------------------------------------------------------------------------------------------------------------------------
#Filtros e Agrupamentos

st.subheader(f'Filtros e Agrupamentos', divider = 'grey')

#3. Filtre os alunos com frequência abaixo de 75% e calcule a média geral deles.
frequencia_75 = df[(df['frequencia_%'] < 75)]
print(f'A média dos alunos com frequencia menor que 75% é: {frequencia_75['frequencia_%'].mean():.2f}')  #printa no console
st.write((f'A média dos alunos com frequencia menor que 75% é: {frequencia_75['frequencia_%'].mean():.2f}')) #printa no Stremalit
print('----------------------------------------------------')


#4. Use groupby para obter a nota média por cidade e matéria.
media_cidade_matematica = df.groupby('cidade')['nota_matematica'].mean()
print('Média de notas por cidade para matematica:') #printa no console
print(media_cidade_matematica)
st.write('Média de notas por cidade para matematica:') #printa no Stremalit
st.write(media_cidade_matematica)
print('----------------------------------------------------')

media_cidade_portugues = df.groupby('cidade')['nota_portugues'].mean()
print('Média de notas por cidade para portugues:') #printa no console
print(media_cidade_portugues)
st.write('Média de notas por cidade para portugues:') #printa no Stremalit
st.write(media_cidade_portugues)
print('----------------------------------------------------')

media_cidade_ciencias = df.groupby('cidade')['nota_ciencias'].mean()
print('Média de notas por cidade para ciencias:') #printa no console
print(media_cidade_ciencias)
st.write('Média de notas por cidade para ciencias:') #printa no Stremalit
st.write(media_cidade_ciencias)
print('----------------------------------------------------')


#5. Crie a seguinte classificação:
#a. Nota menor que 3,0 = reprovado
#b. Nota menor que 6,0 = exame
#c. Nota acima de 6,0 = aprovado

def classifica_nota(nota):
    if nota < 3:
        return 'Reprovado'
    elif nota < 6:
        return 'Exame'
    else:
        return 'Aprovado'
    
df['media'] = (df['nota_matematica'] + df['nota_portugues'] + df['nota_ciencias']) / 3
df['classificacao'] = df['media'].apply(classifica_nota)


#6. Quantos alunos possuem a nota menor que 3,0?
media_menor_3 = df.loc[df['media'] < 3].value_counts()
print(f'A quantidade de alunos com nota menor que 3 é: {media_menor_3.count()}')
st.write(f'A quantidade de alunos com nota menor que 3 é: {media_menor_3.count()}')
print('----------------------------------------------------')


#7. Quantos alunos possuem a nota menor que 5,0?
media_menor_5 = df.loc[(df['media'] >= 3 ) & (df['media'] < 5 )].value_counts()
print(f'A quantidade de alunos com nota menor que 5 é: {media_menor_5.count()}')
st.write(f'A quantidade de alunos com nota menor que 5 é: {media_menor_5.count()}')
print('----------------------------------------------------')


#8. Quantos alunos possuem a nota menor que 7,0?
media_menor_7 = df.loc[(df['media'] >= 5 ) & (df['media'] < 7 )].value_counts()
print(f'A quantidade de alunos com nota menor que 7 é: {media_menor_7.count()}')
st.write(f'A quantidade de alunos com nota menor que 7 é: {media_menor_7.count()}')
print('----------------------------------------------------')


#9. Quantos alunos possuem a nota menor que 9,0?
media_menor_9 = df.loc[(df['media'] >= 7 ) & (df['media'] < 9 )].value_counts()
print(f'A quantidade de alunos com nota menor que 9 é: {media_menor_9.count()}')
st.write(f'A quantidade de alunos com nota menor que 9 é: {media_menor_9.count()}')
print('----------------------------------------------------')

# CODIGO PARA ENCONTRAR OS DOIS ALUNOS FALTANTES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# media_menor_10 = df.loc[(df['media'] >= 9 ) & (df['media'] < 10 )].value_counts()
# print(f'A quantidade de alunos com nota menor que 10 é: {media_menor_10.count()}')
# st.write(f'A quantidade de alunos com nota menor que 10 é: {media_menor_10.count()}')
# print('----------------------------------------------------')

#10. Quantos alunos possuem a nota igual a 10,0?
media_menor_10 = df.loc[(df['media'] == 10 )].value_counts()
print(f'A quantidade de alunos com nota igual a 10 é: {media_menor_10.count()}')
st.write(f'A quantidade de alunos com nota igual a 10 é: {media_menor_10.count()}')
print('----------------------------------------------------')


#11. Qual cidade tem a melhor nota em Matemática, português e ciências? E a Pior nota?
order_matematica = df.sort_values('nota_matematica', ascending=False)
print(f'A cidade com a melhor nota de matematica é: {order_matematica['cidade'].head(1).squeeze()}')
print(f'A cidade com a pior nota de matematica é: {order_matematica['cidade'].tail(1).squeeze()}')
st.write(f'A cidade com a melhor nota de matematica é: {order_matematica['cidade'].head(1).squeeze()}')
st.write(f'A cidade com a pior nota de matematica é: {order_matematica['cidade'].tail(1).squeeze()}')
st.write('\n')
print('----------------------------------------------------')

order_portugues = df.sort_values('nota_portugues', ascending=False)
print(f'A cidade com a melhor nota de portugues é: {order_portugues['cidade'].head(1).squeeze()}')
print(f'A cidade com a pior nota de portugues é: {order_portugues['cidade'].tail(1).squeeze()}')
st.write(f'A cidade com a melhor nota de portugues é: {order_portugues['cidade'].head(1).squeeze()}')
st.write(f'A cidade com a pior nota de portugues é: {order_portugues['cidade'].tail(1).squeeze()}')
st.write('\n')
print('----------------------------------------------------')

order_ciencias = df.sort_values('nota_ciencias', ascending=False)
print(f'A cidade com a melhor nota de ciencias é: {order_ciencias['cidade'].head(1).squeeze()}')
print(f'A cidade com a pior nota de ciencias é: {order_ciencias['cidade'].tail(1).squeeze()}')
st.write(f'A cidade com a melhor nota de ciencias é: {order_ciencias['cidade'].head(1).squeeze()}')
st.write(f'A cidade com a pior nota de ciencias é: {order_ciencias['cidade'].tail(1).squeeze()}')
st.write('\n')
print('----------------------------------------------------')



#--------------------------------------------------------------------------------------------------------------------------------------
#Visualizações

st.subheader(f'Visualizações', divider = 'grey')

#5. Crie um histograma das notas de todas as matérias.
fig1, ax1 = plt.subplots()
plt.hist(df['nota_matematica'], bins=10)
plt.title("Distribuição de Notas de Matematica")
plt.xlabel("Notas")
plt.ylabel("Frequência")
# plt.show()
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
plt.hist(df['nota_portugues'], bins=10)
plt.title("Distribuição de Notas de Portugues")
plt.xlabel("Notas")
plt.ylabel("Frequência")
# plt.show()
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
plt.hist(df['nota_ciencias'], bins=10)
plt.title("Distribuição de Notas de Ciencia")
plt.xlabel("Notas")
plt.ylabel("Frequência")
# plt.show()
st.pyplot(fig3)


#6. Gere um boxplot comparando notas de português por série.
fig4, ax4 = plt.subplots()
sns.boxplot(x='serie', y='nota_portugues', data=df, ax=ax4)
plt.title("Boxplot de Notas de Português por Série")
plt.xlabel("Série")
plt.ylabel("Notas de Português")
st.pyplot(fig4)

#7. Gere um boxplot comparando notas de matemática por série.
fig5, ax5 = plt.subplots()
sns.boxplot(x='serie', y='nota_matematica', data=df, ax=ax5)
plt.title("Boxplot de Notas de Matematica por Série")
plt.xlabel("Série")
plt.ylabel("Notas de Matematica")
st.pyplot(fig5)

#8. Gere um boxplot comparando notas de ciências por série.
fig6, ax6 = plt.subplots()
sns.boxplot(x='serie', y='nota_ciencias', data=df, ax=ax6)
plt.title("Boxplot de Notas de Ciências por Série")
plt.xlabel("Série")
plt.ylabel("Notas de Ciências")
st.pyplot(fig6)

#9. Crie um gráfico de barras com a quantidade de alunos por cidade.
fig7, ax7 = plt.subplots()
cidade_counts = df['cidade'].value_counts()
sns.barplot(x=cidade_counts.index, y=cidade_counts.values, ax=ax7)
plt.xticks(rotation=45)
plt.title("Quantidade de Alunos por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Quantidade de Alunos")
st.pyplot(fig7)

#10. Faça um gráfico de dispersão entre frequencia_% e nota por matéria
fig8, ax8 = plt.subplots()
sns.scatterplot(x='frequencia_%', y='nota_matematica', data=df, ax=ax8, label='Matematica')
sns.scatterplot(x='frequencia_%', y='nota_portugues', data=df, ax=ax8, label='Portugues')
sns.scatterplot(x='frequencia_%', y='nota_ciencias', data=df, ax=ax8, label='Ciencias')
plt.title("Gráfico de Dispersão entre Frequência e Notas")
plt.xlabel("Frequência (%)")
plt.ylabel("Notas")
st.pyplot(fig8)