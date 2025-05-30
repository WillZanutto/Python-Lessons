import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime

# 📦 Conecta (ou cria) o banco de dados SQLite
conn = sqlite3.connect("AulaPython29.05/produtos.db", check_same_thread=False)
cursor = conn.cursor()

# 🏗️ Criação da tabela produtos (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL
)
''')

# 🏗️ Criação da tabela vendas (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    data_venda TEXT NOT NULL,
    FOREIGN KEY(produto_id) REFERENCES produtos(id)
)
''')
conn.commit()

# 📥 Inserção inicial de produtos (DML)
cursor.execute("SELECT COUNT(*) FROM produtos")
if cursor.fetchone()[0] == 0:
    produtos_iniciais = [
        ('Sorvete de Chocolate', 7.5, 'Sobremesa'),
        ('Picolé de Morango', 4.0, 'Sobremesa'),
        ('Água Mineral', 2.0, 'Bebida'),
        ('Refrigerante', 6.0, 'Bebida'),
        ('Café Gelado', 5.0, 'Bebida'),
    ]
    cursor.executemany("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)", produtos_iniciais)
    conn.commit()

# 🎓 Título principal
st.title("🎓 Fundamentos de SQL com Python + Streamlit + SQLite")

# 📋 SELECT * FROM produtos
st.subheader("📋 Tabela: SELECT * FROM produtos")
df = pd.read_sql_query("SELECT * FROM produtos", conn)
st.dataframe(df)

# 🔍 Filtro: WHERE preco > ...
st.subheader("🔍 Filtro: WHERE preco > ...")
valor_min = st.slider("Preço mínimo", 0.0, 10.0, 5.0, 0.5)
df_filtro = pd.read_sql_query("SELECT * FROM produtos WHERE preco > ?", conn, params=(valor_min,))
st.dataframe(df_filtro)

# 🧾 SELECT nome, preco
st.subheader("🧾 SELECT nome, preco")
df_select = pd.read_sql_query("SELECT nome, preco FROM produtos", conn)
st.dataframe(df_select)

# 📊 Funções agregadas
st.subheader("📊 Funções agregadas (AVG, SUM, COUNT)")
df_agregado = pd.read_sql_query('''
    SELECT
        ROUND(AVG(preco), 2) AS media,
        ROUND(SUM(preco), 2) AS soma,
        COUNT(*) AS total
    FROM produtos
''', conn)
st.dataframe(df_agregado)

# 📂 GROUP BY categoria
st.subheader("📂 GROUP BY categoria")
df_group = pd.read_sql_query('''
    SELECT categoria, COUNT(*) AS total_produtos, ROUND(AVG(preco), 2) AS media_preco
    FROM produtos
    GROUP BY categoria
''', conn)
st.dataframe(df_group)

# ➕ Inserir novo produto
st.subheader("➕ Inserir novo produto")
with st.form("form_inserir"):
    nome = st.text_input("Nome do produto")
    preco = st.number_input("Preço", min_value=0.0, step=0.5)
    categoria = st.selectbox("Categoria", ['Sobremesa', 'Bebida', 'Outros'])
    enviar = st.form_submit_button("Inserir")

    if enviar and nome and preco > 0:
        cursor.execute("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)",
                       (nome, preco, categoria))
        conn.commit()
        st.success(f"Produto '{nome}' inserido com sucesso!")
        st.rerun()

# 🧾 Registro de venda
st.subheader("🛒 Registrar nova venda")
produtos = pd.read_sql_query("SELECT id, nome FROM produtos", conn)
produto_nome = st.selectbox("Produto", produtos["nome"])
quantidade = st.number_input("Quantidade", min_value=1, step=1)
registrar = st.button("Registrar venda")

if registrar:
    produto_id = int(produtos[produtos["nome"] == produto_nome]["id"].values[0])
    data_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO vendas (produto_id, quantidade, data_venda) VALUES (?, ?, ?)",
                   (produto_id, quantidade, data_venda))
    conn.commit()
    st.success(f"Venda registrada: {quantidade}x {produto_nome}")
    st.rerun()

# 📦 Tabela de vendas com JOIN
st.subheader("📈 Histórico de vendas")
df_vendas = pd.read_sql_query('''
    SELECT v.id, p.nome AS produto, v.quantidade, v.data_venda
    FROM vendas v
    JOIN produtos p ON v.produto_id = p.id
    ORDER BY v.data_venda DESC
''', conn)
st.dataframe(df_vendas)

# 🔚 Fechando conexão
conn.close()
