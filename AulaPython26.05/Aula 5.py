import pandas as pd

df = pd.read_csv('dados_estatistica_visualizacao.csv', sep=',', encoding='utf-8')
print(df.head())

#Média
df['idade'].mean()
print("Média:", df['idade'].mean(),'\n')

#mediana
df['idade'].median()
print("Mediana:", df['idade'].median(),'\n')

#moda
df['idade'].mode()
print("Moda:", df['idade'].mode(),'\n')

#desvio padrão
df['idade'].std()
print("Desvio Padrão:", df['idade'].std(),'\n')

#variância
df['idade'].var()
print("Variância:", df['idade'].var(),'\n')

#Amplitude (max - min)
df['idade'].max() - df['idade'].min()
print("Amplitude:", df['idade'].max() - df['idade'].min(),'\n')

#resumo geral
df['idade'].describe()
print("Resumo Geral:", df['idade'].describe(),'\n')



import matplotlib.pyplot as plt
import seaborn as sns

#Distribuição com histograma:
plt.hist(df['idade'], bins=20) # qtd de barras
plt.title("Distribuição de Idades")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.show()


#Gráfico de dispersão (scatter plot):
sns.scatterplot(x='departamento', y='salario', data=df)
plt.show()

plt.figure(figsize=(8, 12))

# Gráfico 1
#plt.subplot(n_linhas, n_colunas, índice)
plt.subplot(3, 1, 1)
sns.countplot(x='estado', data=df)
plt.title('Contagem por Estado')

# Gráfico 2
plt.subplot(3, 1, 2)
sns.countplot(x='departamento', data=df)
plt.title('Contagem por Departamento')

# Gráfico 3
plt.subplot(3, 1, 3)
sns.countplot(x='idade', data=df)
plt.title('Contagem por Idade')

plt.tight_layout()
plt.show()