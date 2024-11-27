import sqlite3

def conectar():
    return sqlite3.connect("banco.db")

def tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            data DATETIME DEFAULT CURRENT_TIMESTAMP,
            actualizar DATETIME DEFAULT CURRENT_TIMESTAMP,
            concluida BOOLEAN DEFAULT FALSE
        )
    """)

    conexao.commit()
    conexao.close()
