import pandas as pd

df = pd.read_csv('feedbacks.csv', sep=',', encoding='utf-8', parse_dates=['data'])

#Printa a média de notas por curso
total_notas = df.groupby('curso')['nota'].mean()
print('A média de notas por curso foi:')
print(total_notas)
print('--------------------------------------------------------------')

#Sumariza as notas por curso
sum_nota = df.groupby('curso')['nota'].sum()

#Printa o curso com a melhor avaliação
print(f'O curso com a maior nota foi o {sum_nota.idxmax()}, com {sum_nota.max()}')
print('--------------------------------------------------------------')

#Printa o curso com a pior avaliação
print(f'O curso com a menor nota foi o {sum_nota.idxmin()}, com {sum_nota.min()}')
print('--------------------------------------------------------------')


#Contar quantas pessoas recomendaram cada curso
recomendaria = (df.loc[df.recomendaria == "Sim"])    #pega as avalicações que recomendariam
conta_recomendacao = recomendaria.groupby('curso')['recomendaria'].count()    # agrupa por curso
print('A quantidade de pessoas que recomendariam o curso é:')
print(conta_recomendacao)
print('--------------------------------------------------------------')


#Ver quantidade de feedbacks por dia
avaliacoes_por_dia = df.groupby('data').size()
print('Quantidade de avaliações por dia:')
print(avaliacoes_por_dia)
print('--------------------------------------------------------------')

#Apenas avaliações negativas <=2
relatorio_negativo = df.loc[df.nota <= 2]
print(relatorio_negativo)

#Salva em um novo relatório
relatorio_negativo.to_csv('feedbacks_negativos.csv', index=False)
