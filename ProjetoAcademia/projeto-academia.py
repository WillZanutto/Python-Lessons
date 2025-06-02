import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime
import sqlite3
import csv

# 📦 Conecta (ou cria) o banco de dados SQLite
conn = sqlite3.connect("ProjetoAcademia/gym-system.db", check_same_thread=False)
cursor = conn.cursor()

# Criação da tabela clientes (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes_academia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    sexo TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL,
    plano_id INTEGER NOT NULL,
    FOREIGN KEY(plano_id) REFERENCES planos(id)
)
''')

# Criação da tabela instrutores (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS instrutores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especialidade TEXT NOT NULL
)
''')

# Criação da tabela planos (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS planos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco_mensal REAL NOT NULL,
    duracao_meses INTEGER NOT NULL
)
''')

# Criação da tabela exercicios (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS exercicios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    grupo_muscular TEXT NOT NULL
)
''')

# Criação da tabela treinos (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS treinos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    instrutor_id INTEGER NOT NULL,
    data_inicio TEXT NOT NULL,
    data_fim TEXT NOT NULL,
    plano_id INTEGER NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes_academia(id),
    FOREIGN KEY(instrutor_id) REFERENCES instrutores(id),
    FOREIGN KEY(plano_id) REFERENCES planos(id)
)
''')

# Criação da tabela treino_exercicio (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS treino_exercicios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    treino_id INTEGER NOT NULL,
    exercicio_id INTEGER NOT NULL,
    series TEXT NOT NULL,
    repeticoes INTEGER NOT NULL,
    FOREIGN KEY(treino_id) REFERENCES treinos(id),
    FOREIGN KEY(exercicio_id) REFERENCES exercicios(id)
)
''')

# Criação da tabela pagamentos (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS pagamento_clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    plano_id INTEGER NOT NULL,
    valor_pago REAL NOT NULL,
    data_pagamento TEXT NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes_academia(id),
    FOREIGN KEY(plano_id) REFERENCES planos(id)
)
''')
conn.commit()


cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute("SELECT COUNT(*) FROM exercicios")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('ProjetoAcademia/exercicios.csv')
    df_exercicios.to_sql('exercicios', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM instrutores")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('ProjetoAcademia/instrutores.csv')
    df_exercicios.to_sql('instrutores', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM planos")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('ProjetoAcademia/planos.csv')
    df_exercicios.to_sql('planos', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM clientes_academia")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('ProjetoAcademia/clientes_academia.csv')
    df_exercicios.to_sql('clientes_academia', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM pagamento_clientes")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('ProjetoAcademia/pagamento_clientes.csv')
    df_exercicios.to_sql('pagamento_clientes', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM treinos")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('ProjetoAcademia/treinos.csv')
    df_exercicios.to_sql('treinos', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM treino_exercicios")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('ProjetoAcademia/treino_exercicios.csv')
    df_exercicios.to_sql('treino_exercicios', conn, if_exists='append', index=False)


#Começo do Stremalit
st.title("🎓 Sistema para Academia")

st.subheader("Fazer Novo Cadastro", divider='grey')
opcao_menu = st.selectbox('Escolha uma opção para cadastrar', ['Cliente', 'Pagamento', 'Treino', 'Exercicios por Treino'])

if opcao_menu == 'Cliente':
    st.write('Cliente')
    with st.form("form_cliente", clear_on_submit=True):
        nome_cliente = st.text_input("Nome Cliente")
        idade_cliente = st.text_input("Idade Cliente")
        sexo_cliente = st.text_input("Sexo Cliente(M/F)")
        email_cliente = st.text_input("E-mail Cliente")
        telefone_cliente = st.text_input("Telefone Cliente")
        menu_planos = pd.read_sql_query("SELECT * FROM planos ORDER BY id ASC", conn)
        plano = st.selectbox("Planos", menu_planos["nome"])
        cadastrar = st.form_submit_button("Cadastrar")
    if cadastrar:
            plano_id = int(menu_planos[menu_planos["nome"] == plano]["id"].values[0])
            cursor.execute('''
                           INSERT INTO clientes_academia 
                           (nome, idade, sexo, email, telefone, plano_id) VALUES (?, ?, ?, ?, ?, ?)
                        ''',(nome_cliente, idade_cliente, sexo_cliente, email_cliente, telefone_cliente, plano_id)
                        )
            
            conn.commit()
            st.success(f"Cadastro feito com sucesso")
elif opcao_menu == 'Pagamento':
    st.write('Pagamento')
    menu_cliente = pd.read_sql_query("SELECT * FROM clientes_academia ORDER BY nome ASC", conn)
    menu_planos = pd.read_sql_query("SELECT * FROM clientes_academia ORDER BY nome ASC", conn)
    with st.form("form_pagamento", clear_on_submit=True):
        clientes_opcao = ["-- Selecione o Cliente --"] + menu_cliente["nome"].tolist()
        nome_cliente = st.selectbox("Selecione o Cliente para Pagamento", clientes_opcao)
        pagar = st.form_submit_button("Pago")
        if pagar:
            if (nome_cliente != '-- Selecione o Cliente --'):
                id_cliente = int(menu_cliente[menu_cliente["nome"] == nome_cliente]["id"].values[0])
                id_plano_cliente = int(menu_cliente[menu_cliente["nome"] == nome_cliente]["plano_id"].values[0])
                data_pagamento = datetime.now().strftime("%Y-%m-%d")
                df_valor_plano = pd.read_sql_query("SELECT preco_mensal FROM planos WHERE id = ?", conn, params=(id_plano_cliente,))
                preco_plano = df_valor_plano['preco_mensal'].iloc[0]
                cursor.execute("INSERT INTO pagamento_clientes (cliente_id, plano_id, valor_pago, data_pagamento) VALUES (?, ?, ?, ?)",
                    (id_cliente, id_plano_cliente, preco_plano, data_pagamento))
                conn.commit()
                st.success(f"Pagamento feito com sucesso")
            else:
                st.error(f"Favor selecionar um cliente.")
if opcao_menu == 'Treino':
    st.write('Treino')
    # with st.form("form_emprestimo"):
    #     menu_livro = pd.read_sql_query("SELECT * FROM livros ORDER BY titulo ASC", conn)
    #     livro = st.selectbox("Titulo do livro", menu_livro["titulo"])
    #     enviar = st.form_submit_button("Enviar")
    # if enviar:
    #     try:
    #         livro_id = int(menu_livro[menu_livro["titulo"] == livro]["id"].values[0])
    #         data_emprestimo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #         cursor.execute("INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES (?, ?, 0)",
    #                     (livro_id, data_emprestimo))
            
    #         cursor.execute('''
    #                     UPDATE livros
    #                     SET quantidade_disponivel = quantidade_disponivel - 1
    #                     WHERE titulo = ?
    #                 ''', (menu_livro,))
            
    #         conn.commit()
    #         st.success(f"Empréstimo feito com sucesso")
    #     except Exception as e:
    #         conn.rollback()
    #         st.error(f"Erro ao registrar empréstimo: {str(e)}")
elif opcao_menu == 'Exercicios por Treino':
    st.write('Exercicios por Treino')
    with st.form("form_novo_exercicio_treino", clear_on_submit=True):
        menu_treino = pd.read_sql_query("SELECT * FROM treinos", conn)
        numero_treino = st.selectbox("Treino", menu_treino["id"])
        menu_exercicio = pd.read_sql_query("SELECT * FROM exercicios", conn)
        nome_exercicio = st.selectbox("Exercicio", menu_exercicio["nome"])
        qtd_serie = st.text_input("Quantidade de Séries")
        qtd_repeticoes = st.text_input("Quantidade de Repetições")
        cadastrar_exercicio = st.form_submit_button("Cadastrar")
        if cadastrar_exercicio:
            treino_id = int(menu_treino[menu_treino["id"] == numero_treino]["id"].values[0])
            id_exercicio = int(menu_exercicio[menu_exercicio["nome"] == nome_exercicio]["id"].values[0])
            cursor.execute('''INSERT INTO treino_exercicios
                            (treino_id, exercicio_id, series, repeticoes) 
                            VALUES(?, ?, ?, ?)''', 
                            (treino_id, id_exercicio, qtd_serie,qtd_repeticoes))
            conn.commit()
            st.success(f"Exericio {nome_exercicio} cadastrado com sucesso para o treino {treino_id}!")
st.write('\n')
st.write('\n')