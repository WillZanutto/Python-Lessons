import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

# st.markdown("<h1 style='text-align: center;'>Analise de Expectativa de Vida</h1>", unsafe_allow_html=True)

df = pd.read_csv('Life_Expectancy_Data.csv', sep=',', encoding='utf-8')

def clean_numeric_column(col):
    return col.str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

# Corrigir as colunas 'GDP' e 'percentage expenditure'
df['GDP'] = pd.to_numeric(df['GDP'].astype(str).str.replace('.', '', regex=False), errors='coerce')
df['percentage expenditure'] = pd.to_numeric(df['percentage expenditure'].astype(str).str.replace('.', '', regex=False), errors='coerce')

df_afghanistan = df.loc[(df['Country'] == 'Afghanistan')]
df_brazil = df.loc[(df['Country'] == 'Brazil') & (df['Adult Mortality'] >= 100)]
df_australia = df.loc[(df['Country'] == 'Australia')]
df_botswana = df.loc[(df['Country'] == 'Botswana')]

df_desenvolvimento = df.loc[(df['Status'] == 'Developing') & (df['Life expectancy'] <= 65)]

df_agrupado = df.groupby('Country').agg({
    'Life expectancy': 'mean',
    'Adult Mortality' : 'sum',
    'infant deaths' : 'sum',
    'Schooling' : 'mean'
})
#1. Os vários fatores de previsão inicialmente escolhidos realmente afetam a expectativa de vida? Quais são as variáveis de previsão que realmente afetam a expectativa de vida?
st.title('Análise de Expectativa de Vida')
st.subheader(f'Correlação entre Expectativa de Vida e Fatores de Previsão', divider = 'grey')
fig, ax = plt.subplots()
sns.lineplot(data=df_desenvolvimento, x="Year", y="Life expectancy", hue="Country", ax=ax, legend=False)
plt.title("Expectativa de Vida ao Longo dos Anos")
plt.xlabel("Ano")
plt.ylabel("Expectativa de Vida")
st.pyplot(fig)
st.write('Com base no gráfico acima, podemos ver que a Expectativa de Vida dos países em desenvolvimento no geral aumentou ao longo dos anos. Podemos concluir que os fatores de previsão' \
' inicialmente escolhidos realmente afetam a expectativa de vida. Pois podemos ver que a expectativa de vida aumentou ao longo dos anos, e isso pode ser devido a vários fatores' \
' como o aumento da renda, melhorias na saúde, educação, acesso a serviços de saúde, entre outros fatores. Portanto, podemos concluir que sim, os fatores de previsão afetam a expectativa de vida.')
st.write('\n')
st.write('\n')



#2. Um país com menor expectativa de vida (<65) deve aumentar seus gastos com saúde para melhorar sua expectativa de vida média?
st.subheader(f'Correlação entre Expectativa de Vida e Gastos com Saude', divider = 'grey')
fig1, ax1 = plt.subplots()
# sns.lineplot(data=df_desenvolvimento, x="Year", y="Life expectancy", hue="Country", legend=False)
sns.lineplot(data=df_afghanistan, x="Life expectancy", y="percentage expenditure", ax=ax1)
ax1.set_yscale('linear')
ax1.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
plt.title("Correlação entre Expectativa de Vida e Gastos com Saude do Afeganistão")
plt.xlabel("Expectativa de Vida")
plt.ylabel("Gastos")
st.pyplot(fig1)
st.write('Com base no gráfico acima sobre o Afeganistão. Podemos concluir que conforme o país aumentou seu gasto com saúde, a expectativa de vida também aumentou. Levando-nos' \
'à acreditar que Sim, o aumento de gastos com a saúde pode Sim aumentar a expectativa de vida da população.')
st.write('\n')
st.write('\n')



#3. Como as taxas de mortalidade infantil e adulta afetam a expectativa de vida?
st.subheader(f'Correlação entre Expectativa de Vida e Taxas de Mortalidade', divider = 'grey')
fig2, ax2 = plt.subplots()
sns.lineplot(data=df_brazil, x="Life expectancy", y="Adult Mortality", ax=ax2)
plt.title("Correlação entre Expectativa de Vida e Mortalidade Adulta do Brasil")
plt.xlabel("Expectativa de Vida")
plt.ylabel("Mortalidade Adulta")
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
sns.lineplot(data=df_brazil, x="Life expectancy", y="infant deaths", ax=ax3)
plt.title("Correlação entre Expectativa de Vida e Taxas de Mortalidade Infantil do Brasil")
plt.xlabel("Expectativa de Vida")
plt.ylabel("Mortalidade Infantil")
st.pyplot(fig3)
st.write('Com base nos gráficos acima sobre o Brasil. Podemos concluir que a taxa de mortalidade adulta e infantil tem relação direta com a expectativa de vida do País.')
st.write('\n')
st.write('\n')



#4. A expectativa de vida tem correlação positiva ou negativa com hábitos alimentares, estilo de vida, exercícios, fumo, consumo de álcool etc.
st.subheader(f'Correlação entre Expectativa de Vida e Hábitos Alimentares', divider = 'grey')
fig4, ax4 = plt.subplots()
sns.scatterplot(data=df_afghanistan, x="Life expectancy", y="BMI", ax=ax4, label='Afeganistão')
sns.scatterplot(data=df_brazil, x="Life expectancy", y="BMI", ax=ax4, label='Brasil')
sns.scatterplot(data=df_australia, x="Life expectancy", y="BMI", ax=ax4, label='Australia')
sns.scatterplot(data=df_botswana, x="Life expectancy", y="BMI", ax=ax4, label='Botswana')
ax4.set_yscale('linear')
ax4.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
ax4.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
plt.title("Correlação entre Expectativa de Vida e Hábitos Alimentares")
plt.xlabel("Expectativa de Vida")
plt.ylabel("Índice de Massa Corporal (BMI)")
st.pyplot(fig4)
st.write('Com base no gráfico acima. Podemos ver que o Índice de Massa Corporal (BMI) pode sim ter relação com o aumento ou diminuição da expectativa de vida. Porém não é um fator decisivo, ' \
'ja que podemos ver que o Afeganistão possui um BMI baixo e uma baixa Expectativa de Vida. Ja a Australia, possui um BMI mais alto, porém também possui uma Expectativa de Vida mais alta.')
st.write('\n')
st.write('\n')



#5. Qual é o impacto da escolaridade na expectativa de vida dos seres humanos?
df_escolaridade = df.groupby('Country').agg({
    'Life expectancy': 'mean',
    'Schooling' : 'mean'
})

st.subheader(f'Correlação entre Expectativa de Vida e Taxa Escolaridade', divider = 'grey')
fig5, ax5 = plt.subplots()
sns.lineplot(data=df_escolaridade, x="Life expectancy", y="Schooling", ax=ax5, legend=False)
plt.title("Correlação entre Expectativa de Vida e Taxa Escolaridade dos Paises")
plt.xlabel("Expectativa de Vida")
plt.ylabel("Taxa de Escolaridade")
st.pyplot(fig5)
st.write('Com base no gráfico acima. Podemos ver que a taxa de escolaridade pode sim ter relação com o aumento ou diminuição da expectativa de vida.')
st.write('\n')
st.write('\n')



#6. A expectativa de vida tem relação positiva ou negativa com o consumo de álcool?
st.subheader(f'Correlação entre Expectativa de Vida e Consumo de Alcool', divider = 'grey')
fig6, ax6 = plt.subplots()
sns.lineplot(data=df_afghanistan, x="Life expectancy", y="Alcohol", ax=ax6)
plt.title("Correlação entre Expectativa de Vida e o Consumo de Alcohol no Afeganistão")
plt.xlabel("Expectativa de Vida")
plt.ylabel("Consumo de Alcohol")
st.pyplot(fig6)

fig7, ax7 = plt.subplots()
sns.lineplot(data=df_australia, x="Life expectancy", y="Alcohol", ax=ax7)
plt.title("Correlação entre Expectativa de Vida e o Consumo de Alcohol na Australia")
plt.xlabel("Expectativa de Vida")
plt.ylabel("Consumo de Alcohol")
st.pyplot(fig7)
st.write('Com base nos gráficos acima. Podemos ver que a Consumo de Alcohol pode sim ter relação com o aumento ou diminuição da expectativa de vida. Porém não é um fator decisivo, ' \
'ja que podemos ver que o Afeganistão possui uma baixa Taxa de Consumo de Alcohol e uma baixa Expectativa de Vida. Ja a Australia, possui uma Taxa de Consumo de Alcohol mais ' \
'alta, porém também possui uma Expectativa de Vida mais alta.')
st.write('\n')
st.write('\n')



#7. Países densamente povoados tendem a ter menor expectativa de vida?
df_concat = pd.concat([df_brazil, df_botswana, df_afghanistan, df_australia], ignore_index=True)

st.subheader(f'Correlação entre Densidade Populacional e a Expectativa de Vida', divider = 'grey')
fig8, ax8 = plt.subplots()
sns.scatterplot(data=df_concat, x="Life expectancy", y="Population", hue='Country', ax=ax8)
ax8.set_yscale('linear')
ax8.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
ax8.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
plt.title("Correlação entre Expectativa de Vida e a Densidade Populacional do Brasil")
plt.xlabel("Expectativa de Vida")
plt.ylabel("Densidade Populacional")
st.pyplot(fig8)
st.write('Com base no gráfico acima. Podemos ver que a densidade populacional não necessariamente tem relação com a Expectativa de vida. Pois podemos ver paises com baixa ' \
'densidade populacional que possuem baixa expectativa de vida, assim como paises com alta expectativa de vida. Também podemos ver paises com alta densidade populacional' \
'que possuem expectativa de vida mais alta.')
st.write('\n')
st.write('\n')


#8. Qual é o impacto da cobertura de imunização na expectativa de vida?
df_agrupado2 = df.groupby('Country').agg({
    'Life expectancy': 'mean',
    'Hepatitis B' : 'mean',
    'Measles' : 'mean',
    'Polio' : 'mean',
    'Diphtheria' : 'mean',
    'HIV/AIDS' : 'mean'
})

st.subheader(f'Tabela com Correlação entre a Expectativa de Vida e a Cobertura de Imunização', divider = 'grey')
st.write(df_agrupado2)
st.write('Com base na tabela acima, podemos analisar que a Cobertura de Imunização de um país pode sim influenciar na expectativa de vida de um país. Pois quanto maior a taxa' \
' de vacinação, menores as chances de aumentar a taxa de mortalidade por causa da doença.')


