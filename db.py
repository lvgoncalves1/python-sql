import sqlite3

def conectar():
    conn = sqlite3.connect("escola.db")
    return conn

def criar_tabela_estudante():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER
        )
    """
    )
    conn.commit()
    conn.close()