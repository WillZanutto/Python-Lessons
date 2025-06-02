import streamlit as st
import sqlite3
import hashlib

# =========================
# 1. Funções auxiliares
# =========================

# def conectar_banco():
#     """Conecta ao banco de dados SQLite"""
#     return sqlite3.connect("sistema_academia.db", check_same_thread=False)

# 📦 Conecta (ou cria) o banco de dados SQLite
conn = sqlite3.connect("ProjetoAcademia/gym-system.db", check_same_thread=False)
cursor = conn.cursor()

# """Cria a tabela de usuários se não existir"""
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL
    )
''')
conn.commit()

def hash_senha(senha):
    # """Retorna o hash SHA256 da senha"""
    return hashlib.sha256(senha.encode()).hexdigest()


# """Popula a tabela com 5 usuários, se estiver vazia"""
cursor.execute("SELECT COUNT(*) FROM usuarios")
if cursor.fetchone()[0] == 0:
    usuarios = [
        ("Alice Santos", "alice@email.com", "senha123"),
        ("Bruno Silva", "bruno@email.com", "segredo"),
        ("Carlos Lima", "carlos@email.com", "academia"),
        ("Diana Costa", "diana@email.com", "fitness"),
        ("Eduarda Reis", "eduarda@email.com", "malhacao")
    ]
    for nome, email, senha in usuarios:
        senha_hash = hash_senha(senha)
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                        (nome, email, senha_hash))
    conn.commit()

def autenticar_usuario(email, senha):
    # """Autentica o usuário pelo email e senha (com hash)"""
    senha_hash = hash_senha(senha)
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha_hash))
    return cursor.fetchone()


# =========================
# 2. Interface do Streamlit
# =========================

# Controle de sessão
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = None

# Se não estiver logado, mostra tela de login
if not st.session_state.logado:
    st.title("Login de Usuário")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        usuario = autenticar_usuario(email, senha)
        if usuario:
            st.session_state.logado = True
            st.session_state.usuario = usuario
            st.success(f"Bem-vindo, {usuario[1]}!")
            st.rerun()
        else:
            st.error("Email ou senha incorretos. Tente novamente.")

# Se estiver logado, mostra conteúdo protegido
else:
    st.sidebar.success(f"Logado como: {st.session_state.usuario[1]}")
    st.title("Dashboard da Academia")
    st.write("Aqui você pode acessar informações de treinos, pagamentos, etc.")

    if st.sidebar.button("Sair"):
        st.session_state.logado = False
        st.session_state.usuario = None
        st.rerun()