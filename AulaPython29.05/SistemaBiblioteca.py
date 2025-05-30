import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime

# 📦 Conecta (ou cria) o banco de dados SQLite
conn = sqlite3.connect("AulaPython29.05/biblioteca.db", check_same_thread=False)
cursor = conn.cursor()

# 🏗️ Criação da tabela autores (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

# 🏗️ Criação da tabela categorias (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

# 🏗️ Criação da tabela livros (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    ano TEXT NOT NULL,
    quantidade_disponivel INTEGER NOT NULL,
    FOREIGN KEY(autor_id) REFERENCES autores(id),
    FOREIGN KEY(categoria_id) REFERENCES categorias(id)
)
''')

# 🏗️ Criação da tabela emprestimos (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livro_id INTEGER NOT NULL,
    data_emprestimo TEXT NOT NULL,
    devolvido BOOLEAN NOT NULL,
    FOREIGN KEY(livro_id) REFERENCES livros(id)
)
''')
conn.commit()


# Popular tabela autores
cursor.execute("SELECT COUNT(*) FROM autores")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
        INSERT INTO autores (nome) VALUES (?)
        ''', [
            ('Machado de Assis',),
            ('Clarice Lispector',),
            ('Jorge Amado',),
            ('Carlos Drummond de Andrade',),
            ('Cecília Meireles',),
            ('Monteiro Lobato',),
            ('Graciliano Ramos',),
            ('Lygia Fagundes Telles',),
            ('Rubem Fonseca',),
            ('Paulo Coelho',),
            ('Erico Verissimo',)
        ])
    conn.commit()

# Popular tabela categorias
cursor.execute("SELECT COUNT(*) FROM categorias")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
    INSERT INTO categorias (nome) VALUES (?)
    ''', [
        ('Literatura Brasileira',),
        ('Romance',),
        ('Poesia',),
        ('Contos',),
        ('Infantil',),
        ('Ficção Científica',),
        ('Fantasia',),
        ('Biografia',),
        ('História',),
        ('Autoajuda',),
        ('Drama',)
    ])
    conn.commit()

# Popular tabela livros
cursor.execute("SELECT COUNT(*) FROM livros")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
    INSERT INTO livros (titulo, autor_id, categoria_id, ano, quantidade_disponivel) VALUES (?, ?, ?, ?, ?)
    ''', [
        ('Dom Casmurro', 1, 1, '1899', 5),
        ('A Hora da Estrela', 2, 2, '1977', 3),
        ('Capitães da Areia', 3, 1, '1937', 7),
        ('Claro Enigma', 4, 3, '1951', 4),
        ('Ou Isto ou Aquilo', 5, 3, '1964', 6),
        ('Reinações de Narizinho', 6, 5, '1931', 8),
        ('Vidas Secas', 7, 1, '1938', 2),
        ('As Meninas', 8, 11, '1973', 3),
        ('O Alienista', 1, 4, '1882', 5),
        ('O Alquimista', 10, 10, '1988', 9),
        ('Olhai os Lírios do Campo', 11, 2, '1938', 4)
    ])
    conn.commit()

# Popular tabela empréstimos
cursor.execute("SELECT COUNT(*) FROM emprestimos")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
    INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES (?, ?, ?)
    ''', [
        (1, '2023-01-15', True),    # Dom Casmurro - devolvido
        (3, '2023-02-20', False),   # Capitães da Areia - pendente
        (5, '2023-03-10', True),    # Ou Isto ou Aquilo - devolvido
        (2, '2023-04-05', False),   # A Hora da Estrela - pendente
        (7, '2023-05-12', True),    # Vidas Secas - devolvido
        (4, '2023-06-18', False),   # Claro Enigma - pendente
        (6, '2023-07-22', True),    # Reinações de Narizinho - devolvido
        (9, '2023-08-30', False),   # O Alienista - pendente
        (8, '2023-09-14', True),    # As Meninas - devolvido
        (10, '2023-10-25', False),  # O Alquimista - pendente
        (11, '2023-11-05', True)    # Olhai os Lírios do Campo - devolvido
    ])
    conn.commit()

#Começo do Stremalit
st.title("🎓 Sistema para Biblioteca")

# Todos os livros com nome do autor e da categoria.
st.subheader("Histórico de vendas", divider='grey')
df_livros = pd.read_sql_query('''
    SELECT l.id, l.titulo, a.nome AS nome_autor, c.nome AS categoria
    FROM livros l
    JOIN autores a ON l.autor_id = a.id
    JOIN categorias c ON l.categoria_id = c.id
    ORDER BY l.id ASC
''', conn)
st.dataframe(df_livros)
st.write('\n')
st.write('\n')


#Filtro de livros por ano de publicação.
st.subheader("Livros por Ano", divider='grey')
ano_publicacao = pd.read_sql_query("SELECT DISTINCT ano FROM livros ORDER BY ano ASC", conn)
ano_livro = st.selectbox("Produto", ano_publicacao["ano"])
pesquisar = st.button("Pesquisar Livros")

if pesquisar:
    df_livros = pd.read_sql_query('''
    SELECT l.id, l.titulo, a.nome AS nome_autor, c.nome AS categoria, l.ano
    FROM livros l
    JOIN autores a ON l.autor_id = a.id
    JOIN categorias c ON l.categoria_id = c.id
    WHERE l.ano = ?
    ORDER BY l.id ASC
''', conn, params=(ano_livro,))
    st.dataframe(df_livros)
    st.write('\n')
    st.write('\n')


#Quantidade total de livros, de empréstimos e devolvidos.
st.subheader("Quantidade Total de Livros, Emprestados e Devolvidos", divider='grey')
df_quantidade = pd.read_sql_query('''
    SELECT
        COUNT(DISTINCT l.id) AS total_livros,
        COUNT(CASE WHEN e.devolvido = 0 THEN 1 END) AS livros_emprestados,
        COUNT(CASE WHEN e.devolvido = 1 THEN 1 END) AS total_devolvidos
    FROM livros l
    LEFT JOIN emprestimos e ON l.id = e.livro_id
''', conn)
st.dataframe(df_quantidade)
st.write('\n')
st.write('\n')



#Número de livros por categoria (agrupado).
st.subheader("Quantidade de Livros por Categoria", divider='grey')
df_group = pd.read_sql_query('''
    SELECT c.nome AS nome_categoria, COUNT(l.titulo) AS total_livros
    FROM categorias c
    JOIN livros l ON c.id = l.categoria_id
    GROUP BY c.nome
''', conn)
st.dataframe(df_group)
st.write('\n')
st.write('\n')



#Formulário para registrar novo empréstimo ou novo livro.
st.subheader("Registrar novo livro ou novo empréstimo", divider='grey')
opcao_menu = st.selectbox('Escolha uma opção', ['Empréstimo', 'Novo'])

if opcao_menu == 'Empréstimo':
    with st.form("form_emprestimo"):
        menu_livro = pd.read_sql_query("SELECT * FROM livros ORDER BY titulo ASC", conn)
        livro = st.selectbox("Titulo do livro", menu_livro["titulo"])
        enviar = st.form_submit_button("Enviar")
    if enviar:
        try:
            livro_id = int(menu_livro[menu_livro["titulo"] == livro]["id"].values[0])
            data_emprestimo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES (?, ?, 0)",
                        (livro_id, data_emprestimo))
            
            cursor.execute('''
                        UPDATE livros
                        SET quantidade_disponivel = quantidade_disponivel - 1
                        WHERE titulo = ?
                    ''', (menu_livro,))
            
            conn.commit()
            st.success(f"Empréstimo feito com sucesso")
        except Exception as e:
            conn.rollback()
            st.error(f"Erro ao registrar empréstimo: {str(e)}")
else:
    with st.form("form_novo_livro", clear_on_submit=True):
        titulo_livro = st.text_input("Titulo do livro")
        menu_autor = pd.read_sql_query("SELECT * FROM autores ORDER BY nome ASC", conn)
        nome_autor = st.selectbox("Autor", menu_autor["nome"])
        # nome_autor = st.text_input("Nome do Autor")
        menu_categoria = pd.read_sql_query("SELECT * FROM categorias ORDER BY nome ASC", conn)
        nome_categoria = st.selectbox("Categoria", menu_categoria["nome"])
        ano_publicacao = st.text_input("Ano de Publicação(AAAA)")
        quantidade = st.number_input("Quantidade Disponível", min_value=1, value=1)
        inserir = st.form_submit_button("Inserir")
        if inserir:
            cursor.execute("SELECT COUNT(*) FROM livros WHERE titulo = ?", (titulo_livro,))
            if cursor.fetchone()[0] == 0:
                autor_id = int(menu_autor[menu_autor["nome"] == nome_autor]["id"].values[0])
                categoria_id = int(menu_categoria[menu_categoria["nome"] == nome_categoria]["id"].values[0])
                cursor.execute('''INSERT INTO livros
                               (titulo, autor_id, categoria_id, ano, quantidade_disponivel) 
                               VALUES(?, ?, ?, ?, ?)''', 
                               (titulo_livro, autor_id, categoria_id,ano_publicacao, quantidade))
                conn.commit()
                st.success(f"Livro Inserido com Sucesso!")
            else:
                st.error(f"Livro ja existe na Base de Dados!")
st.write('\n')
st.write('\n')



#Formulário para editar um autor (alterar o nome)
st.subheader("Alterar Nome dos Autores", divider='grey')
with st.form("form_editar_autor", clear_on_submit=True):
    menu_autor = pd.read_sql_query("SELECT * FROM autores ORDER BY nome ASC", conn)
    nome_autor = st.selectbox("Autor", menu_autor["nome"])
    novo_nome_autor = st.text_input("Digite o novo nome para o Autor")
    alterar = st.form_submit_button("Alterar")
    if alterar:
        autor_id = int(menu_autor[menu_autor["nome"] == nome_autor]["id"].values[0])
        cursor.execute('''
                            UPDATE autores
                            SET nome = ?
                            WHERE id = ?
                        ''', (novo_nome_autor, autor_id))
        conn.commit()
        st.success(f"Nome Autor alterado com Sucesso!")
st.write('\n')
st.write('\n')


# # Formulário para editar um livro (alterar titulo, nome, categoria, quantidade disponivel)

menu_livro = pd.read_sql_query("SELECT * FROM livros ORDER BY titulo ASC", conn)
menu_autor = pd.read_sql_query("SELECT * FROM autores ORDER BY nome ASC", conn)
menu_categoria = pd.read_sql_query("SELECT * FROM categorias ORDER BY nome ASC", conn)

# Seleção do livro fora do formulário
titulo_livro = st.selectbox("Selecione o livro a editar", menu_livro["titulo"])

# Recupera dados do livro selecionado
livro_info = menu_livro[menu_livro["titulo"] == titulo_livro].iloc[0]
livro_id = int(livro_info["id"])
titulo_atual = livro_info["titulo"]
autor_id_atual = int(menu_livro[menu_livro["titulo"] == titulo_livro]["autor_id"].values[0])
categoria_id_atual = int(menu_livro[menu_livro["titulo"] == titulo_livro]["categoria_id"].values[0])
ano_atual = livro_info["ano"]
quantidade_atual = int(livro_info["quantidade_disponivel"])

# Exibe o formulário com valores prontos
with st.form("form_editar_livro", clear_on_submit=True):
    st.markdown(f"**Editando:** `{titulo_atual}`")

    novo_titulo = st.text_input("Novo Titulo do Livro", value="")
    autores_opcoes = ["-- Manter Atual --"] + menu_autor["nome"].tolist()
    nome_autor_atual = menu_autor[menu_autor["id"] == autor_id_atual]["nome"].values[0]
    novo_autor = st.selectbox("Novo Autor", autores_opcoes, index=autores_opcoes.index("-- Manter Atual --"))
    categorias_opcoes = ["-- Manter Atual --"] + menu_categoria["nome"].tolist()
    nome_categoria_atual = menu_categoria[menu_categoria["id"] == categoria_id_atual]["nome"].values[0]
    nova_categoria = st.selectbox("Nova Categoria", categorias_opcoes, index=categorias_opcoes.index("-- Manter Atual --"))
    novo_ano = st.text_input("Novo Ano de Publicação (AAAA)", value="")
    nova_quantidade = quantidade_atual
    nova_quantidade = st.number_input("Nova Quantidade Disponível", min_value=1, value=quantidade_atual)
    editar = st.form_submit_button("Salvar Alterações")

    if editar:
        # Verifica cada campo
        titulo_final = novo_titulo.strip() if novo_titulo.strip() else titulo_atual
        autor_id_final = autor_id_atual
        if novo_autor != "-- Manter Atual --":
            autor_id_final = int(menu_autor[menu_autor["nome"] == novo_autor]["id"].values[0])

        categoria_id_final = categoria_id_atual
        if nova_categoria != "-- Manter Atual --":
            categoria_id_final = int(menu_categoria[menu_categoria["nome"] == nova_categoria]["id"].values[0])

        ano_final = novo_ano.strip() if novo_ano.strip() else ano_atual
        quantidade_final = nova_quantidade

        # Atualiza no banco
        cursor.execute('''
            UPDATE livros
            SET titulo = ?, autor_id = ?, categoria_id = ?, ano = ?, quantidade_disponivel = ?
            WHERE id = ?
        ''', (titulo_final, autor_id_final, categoria_id_final, ano_final, quantidade_final, livro_id))
        conn.commit()
        st.success("Livro alterado com sucesso!")
st.write('\n')
st.write('\n')



# Formulário para Deletar um livro ou autor
st.subheader("Deletar Livro ou Autor", divider='grey')

menu_deletar = st.selectbox("Deletar", ["Livro", "Autor"])
with st.form("form_deletar", clear_on_submit=True):

    
    if menu_deletar == "Livro":
        menu_livro = pd.read_sql_query("SELECT * FROM livros ORDER BY titulo ASC", conn)
        menu_livro = menu_livro.reset_index(drop=True)
        titulo_livro = st.selectbox("Titulo do livro", menu_livro["titulo"])
        deletar = st.form_submit_button("Deletar Livro")
        if deletar:
            livro_id = int(menu_livro[menu_livro["titulo"] == titulo_livro]["id"].values[0])
            cursor.execute('DELETE FROM livros WHERE id = ?', (livro_id,))
            conn.commit()
            st.success(f"Livro {titulo_livro} deletado com sucesso!")
    
    elif menu_deletar == "Autor":
        menu_autor = pd.read_sql_query("SELECT * FROM autores ORDER BY nome ASC", conn)
        menu_autor = menu_autor.reset_index(drop=True)
        nome_autor = st.selectbox("Autor", menu_autor["nome"])
        deletar = st.form_submit_button("Deletar Autor")
        if deletar:
            autor_id = int(menu_autor[menu_autor["nome"] == nome_autor]["id"].values[0])
            cursor.execute('DELETE FROM autores WHERE id = ?', (autor_id,))
            conn.commit()
            st.success(f"Autor {nome_autor} deletado com sucesso!")