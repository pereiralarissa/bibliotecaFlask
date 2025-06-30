import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Atualiza os nomes dos arquivos PDF corretos
cursor.execute("UPDATE livros SET pdf = 'aventuras_na_floresta.pdf' WHERE titulo = 'Aventuras na Floresta'")
cursor.execute("UPDATE livros SET pdf = 'contos_infantis.pdf' WHERE titulo = 'Contos infantis'")
cursor.execute("UPDATE livros SET pdf = 'o_misterio_da_casa_abandonada.pdf' WHERE titulo = 'O mistério da Casa Abandonada'")

# Salva e fecha
conn.commit()
conn.close()

print("Atualização concluída com sucesso!")
