import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Verifica se a coluna 'pdf' já existe
cursor.execute("PRAGMA table_info(livros)")
colunas = [coluna[1] for coluna in cursor.fetchall()]

if 'pdf' not in colunas:
    cursor.execute("ALTER TABLE livros ADD COLUMN pdf TEXT")
    print("Coluna 'pdf' adicionada com sucesso.")
else:
    print("A coluna 'pdf' já existe.")

conn.commit()
conn.close()
