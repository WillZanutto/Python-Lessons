import pandas as pd

df = pd.read_csv('IMDB Top 250 Movies.csv', sep=',', encoding='utf-8', parse_dates = ['year'])

# Os 3 diretores mais recorrentes
top3 = df['directors'].value_counts()
print(top3.head(3))
print('--------------------------------------------------------------')

#Media das avaliações
media_avaliacoes = df.groupby('name')['rating'].mean()
print('A media das avaliações por filme são:')
print(media_avaliacoes)
print('--------------------------------------------------------------')

#Filmes mais antigos e mais recentes
ano = df.sort_values('year')
print(f'Os 5 filmes mais antigos foram: ')
print(ano.head(5))
print('--------------------------------------------------------------')

print(f'Os 5 filmes mais novos foram: ')
print(ano.tail(5))
print('--------------------------------------------------------------')


#Qual a média de duração dos filmes?
def to_minute(s):
    try:
        h, m = s.split('h')
        return int(h.strip()) * 60 + int(m.replace('m', '').strip())
    except:
        return None
    
df['run_time_minute'] = df.run_time.apply(to_minute).astype(float)

media = df.run_time_minute.sum() / len(df["run_time_minute"])
print(f'A média de duração dos filmes é {media:.2f} minutos ou {media / 60:.2f} horas')


#Quantos filmes há por década?
df['decada'] = (df.year.dt.year // 10) * 10   #Cria uma coluna Década
print('A quantidade de filmes por década é:')
print(df.decada.value_counts())


# Qual gênero é mais frequente?
genero_frequente = df['genre'].value_counts()
print('O genero mais frequente é: ')
print(genero_frequente.head(1))
print('--------------------------------------------------------------')


#Filmes com mais de 3 horas de duração
print('Os filmes com mais de 3 horas de duração são:')
print(df.loc[df.run_time_minute > 180])
print('--------------------------------------------------------------')



#-----------------------------------------------------------------------------------------------------------------------------
#1. Análise de décadas

#1.2.Quais são os 10 melhores filmes de acordo com as avaliações? E os 10 piores?
df_ordenado = df.sort_values('rating', ascending=False)
print('Os 10 melhores filmes de acordo com as avaliações são:')
print(df_ordenado.head(10))
print('Os 10 piores filmes de acordo com as avaliações são:')
print(df_ordenado.tail(10))
print('--------------------------------------------------------------')


#1.3.Qual foi a década com mais filmes no Top 250?
print('A década com mais filmes foi a:')
print(df.decada.value_counts().head(1))
print('--------------------------------------------------------------')


#1.4.Para cada década, calcule a nota média e duração média dos filmes
media_avaliacoes_decada = df.groupby('decada')[['rating', 'run_time_minute']].mean()
print('A média de avaliações e duração(em minutos) dos filmes por década é:')
print(media_avaliacoes_decada)
print('--------------------------------------------------------------')


#1.5. Salve esse resumo em um novo CSV chamado resumo_decadas.csv.
media_avaliacoes_decada.to_csv('resumo_decadas.csv')





#-----------------------------------------------------------------------------------------------------------------------------
#2. Diretores e frequência

#2.1. Quantos diretores diferentes existem na lista?
qtd_diretores = df['directors'].str.split(',').explode().str.strip()
qtd_diretores_unicos = len(qtd_diretores.unique())
print(f'A quantidade de diretos diferentes na lista é: {qtd_diretores_unicos}')
print('--------------------------------------------------------------')


#2.2. Quais são os 5 diretores mais frequentes (com mais filmes no Top 250)?
print(df.directors.value_counts().head(5))
print('--------------------------------------------------------------')


#2.3. Qual é a nota média dos filmes de cada diretor (exibir só quem tem 3 ou mais filmes)?
df_diretores = df.copy()

df_diretores['directors'] = df_diretores['directors'].str.split(',')
df_diretores = df_diretores.explode('directors')
df_diretores['directors'] = df_diretores['directors'].str.strip()
conta_diretores = df_diretores['directors'].value_counts()
diretores_mais3 = conta_diretores[conta_diretores >= 3].index
media_nota_diretores = df_diretores.groupby('directors')['rating'].mean().sort_values()
media_nota_diretores2 = media_nota_diretores.loc[diretores_mais3]
print('A média de notas dos diretores com mais de 3 filmes é:')
print(media_nota_diretores2.sort_values(ascending=False))
print('--------------------------------------------------------------')


#2.4. Qual diretor tem filme mais bem avaliado?
diretores_classificados = df_diretores.sort_values(by='rating', ascending=False)
diretor_bem_avaliado = diretores_classificados.head(1)
print(f'O diretor mais bem avaliado foi o: {diretor_bem_avaliado['directors']}')
print('--------------------------------------------------------------')


#2.5. Exporte para CSV um ranking com diretor, quantidade de filmes, nota média.
csv_diretores = df_diretores.groupby('directors').agg(
    qtd_filmes=('name', 'count'),
    nota_media=('rating', 'mean')
).reset_index()
csv_diretores.to_csv('ranking_diretores.csv',index=False)




#-----------------------------------------------------------------------------------------------------------------------------
#3. Filmes por duração

#3.1. Crie uma coluna chamada Categoria_Duracao com base nas regras:
df_duracao = df.copy()

def categoria_duracao(duracao):
    if duracao < 90:
        return 'Curto'
    elif 90 <= duracao <= 150:
        return 'Médio'
    else:
        return 'Longo'

df_duracao['Categoria_Duracao'] = df_duracao['run_time_minute'].apply(categoria_duracao)


#3.2. Mostre quantos filmes tem em cada categoria.
count_categoria = df_duracao['Categoria_Duracao'].value_counts()
print(count_categoria)
print('--------------------------------------------------------------')


#3.3. Qual a nota média de cada categoria?
media_nota_categoria = df_duracao.groupby('Categoria_Duracao')['rating'].mean().sort_values()
print('A nota média de cada categoria é:')
print(media_nota_categoria)
print('--------------------------------------------------------------')


#3.4. Qual categoria é mais comum no Top 250?
print(count_categoria.head(1))
print('--------------------------------------------------------------')




#-----------------------------------------------------------------------------------------------------------------------------
#4. Filmes por ano

df_ano = pd.read_csv('IMDB Top 250 Movies.csv', sep=',', encoding='utf-8')

#4.1. Quantos filmes foram lançados em cada ano?
count_filme_ano = df_ano['year'].value_counts()
print('A quantidade de filmes lançados por ano foi:')
print(count_filme_ano)
print('--------------------------------------------------------------')


#4.2. Qual ano teve mais filmes no Top 250?
print('O ano com mais filmes lançados foi: ')
print(count_filme_ano.head(1))
print('--------------------------------------------------------------')


#4.3. Quais os filmes lançados entre 1990 e 1999 com nota acima de 3?
filmes_decada_90 = df_ano[(df_ano['year'] >= 1990) & (df_ano['year'] <= 1999) & (df_ano['rating'] > 3)]
print('Os filmes da decada de 1990 e nota maior que 3 são:')
print(filmes_decada_90)
print('--------------------------------------------------------------')


#4.4. Exporte esses filmes para filmes_anos_90.csv
filmes_decada_90.to_csv('filmes_anos_90.csv', index=False)




#-----------------------------------------------------------------------------------------------------------------------------
#5. Análise textual (coluna “Title”)



#5.1. Quantos filmes contêm a palavra "Love" no título?
df_texto = pd.read_csv('IMDB Top 250 Movies.csv', sep=',', encoding='utf-8')

filmes_com_love = df_texto['name'].str.contains('Love', case=False, na=False)
print(f'A quantidade de filmes com a palavra "Love" no Nome é: {filmes_com_love.sum()}')
print('--------------------------------------------------------------')


#5.2. Liste os filmes que têm a palavra "War", "God" ou "King" no título.
padrao = 'War|God|King'
filmes_war_god_king = df_texto['name'].str.contains(padrao, case=False, na=False)
print(f'A quantidade de filmes com a palavra "War", "God" e "King" no Nome é: {filmes_war_god_king.sum()}')
print('--------------------------------------------------------------')


#5.3. Crie uma nova coluna chamada titulo_maiusculo com os títulos em letras maiúsculas.
df_texto['titulo_maisculo'] = df_texto['name'].str.upper()


#5.4. Quantos títulos têm mais de 25 caracteres?
lista_titulos = df_diretores['name']
def tamanho_nome(nome):
    return len(nome)

df_texto['tamanho_titulo'] = df_duracao['name'].apply(tamanho_nome)
print(df_texto[['name', 'tamanho_titulo']])
print('--------------------------------------------------------------')


#5.5. Qual o título mais longo da lista?
titulo_mais_longo = df_texto.sort_values('tamanho_titulo',ascending=False)
print('O filme com o nome mais longo é o:')
print(titulo_mais_longo.head(1))
print('--------------------------------------------------------------')





#-----------------------------------------------------------------------------------------------------------------------------
#6. Filtros múltiplos

df_filtro = pd.read_csv('IMDB Top 250 Movies.csv', sep=',', encoding='utf-8')

#6.1.
def to_minute(s):
    try:
        h, m = s.split('h')
        return int(h.strip()) * 60 + int(m.replace('m', '').strip())
    except:
        return None
    
df_filtro['run_time'] = df.run_time.apply(to_minute).astype(float)

filmes_pos_2000 = df_ano[(df_filtro['year'] > 2000) & (df_filtro['run_time'] <= 100) & (df_filtro['rating'] >= 8)]
print('Lista de filmes com nota maior ou igual à 8, duração menor ou igual à 100 minutos e lançados após o ano 2000:')
print(filmes_pos_2000)
print('--------------------------------------------------------------')


#6.2
filtra_duracao = df_filtro[(df_filtro['run_time'] >= 120) & (df_filtro['run_time'] <= 150) & (df_filtro['directors'] == 'Christopher Nolan') & (df_filtro['rank'] <= 50)]
print(filtra_duracao)
filtra_duracao.to_csv('filmes_nolan.csv', index=False)
print('--------------------------------------------------------------')


#6.3. Mostre os filmes com título iniciado pela letra “A” e nota acima de 8.0.
filtra_filme_A = df_filtro[(df_filtro['name'].str[0] == 'A') & (df_filtro['rating'] > 8)]
print('Lista de filmes que começam com a Letra "A" e possuem Rating maior que 8')
print(filtra_filme_A)
print('--------------------------------------------------------------')


#6.4. Liste todos os filmes que não foram dirigidos por “Steven Spielberg”.
filmes_sem_spielberg = df_filtro[df_filtro['directors'] != 'Steven Spielberg']
print(filmes_sem_spielberg)
filmes_sem_spielberg.to_csv('filmes_sem_spielberg.csv', index=False)