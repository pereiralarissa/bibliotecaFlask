from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Inicializa o banco de dados
def init_db():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute('SELECT * FROM livros')
    livros = c.fetchall()
    conn.close()
    return render_template('index.html', livros=livros)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    titulo = request.form['titulo']
    autor = request.form['autor']
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute('INSERT INTO livros (titulo, autor) VALUES (?, ?)', (titulo, autor))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
