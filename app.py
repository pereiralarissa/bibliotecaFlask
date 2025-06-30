from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'segredo'  # segredo para sessão do usuário

# Caminho da pasta de PDFs
CAMINHO_PDF = os.path.join('static', 'pdfs')

# Rota inicial: mostra a lista de livros
@app.route('/')
def index():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, autor, pdf FROM livros")
    livros = cursor.fetchall()
    conn.close()
    return render_template('index.html', livros=livros)

# Rota para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario == 'admin' and senha == '123':
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:
            return 'Login inválido!'
    return render_template('login.html')

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

# Rota para adicionar livro
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        pdf = request.files['pdf']
        nome_pdf = ''

        if pdf:
            nome_pdf = pdf.filename
            caminho = os.path.join(CAMINHO_PDF, nome_pdf)
            pdf.save(caminho)

        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO livros (titulo, autor, pdf) VALUES (?, ?, ?)", (titulo, autor, nome_pdf))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('adicionar.html')

# Rota para ler o PDF
@app.route('/ler/<nome_pdf>')
def ler(nome_pdf):
    return send_from_directory(CAMINHO_PDF, nome_pdf)
