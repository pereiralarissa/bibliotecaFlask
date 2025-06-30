import sqlite3

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

# Criar tabela de livros
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    pdf TEXT
)
''')

# Criar tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
''')

conexao.commit()
conexao.close()
print("Banco de dados criado com sucesso.")
