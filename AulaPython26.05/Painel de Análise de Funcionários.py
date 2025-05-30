import pandas as pd
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
plt.hist(df['estado'], bins=10) # qtd de barras
plt.title("Distribuição de Estados")
plt.xlabel("Estado")
plt.ylabel("Frequência")
plt.show()

#Boxplot de salário por departamento
sns.boxplot(x='departamento', y='salario', data=df)
plt.show()

#Gráfico de dispersão entre idade e salario, colorido por departamento.
sns.scatterplot(x='idade', y='salario', hue='departamento', data=df)
plt.show()



#-----------------------------------------------------------------------------------------------------------------------------

