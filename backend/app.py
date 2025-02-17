import os
import secrets
import logging
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash, abort
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from flask_bcrypt import Bcrypt
import sqlite3

# Configuração do Flask
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Chave secreta para sessões e CSRF
app.template_folder = os.path.join('..', 'frontend', 'templates')
app.static_folder = os.path.join('..', 'frontend')  # Diretório para arquivos estáticos
app.config['DATABASE'] = 'users.db'

# Proteção CSRF
csrf = CSRFProtect(app)

# Instância do Bcrypt para hashing de senhas
bcrypt = Bcrypt(app)

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Conexão com o banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

# Inicializar banco de dados
def init_db():
    conn = get_db_connection()
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
    conn.close()

# Formulários com Flask-WTF
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password', message='As senhas devem ser iguais')])
    submit = SubmitField('Cadastrar')

    def validate_email(self, email):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email.data,)).fetchone()
        conn.close()
        if user is not None:
            raise ValidationError('Já existe um usuário com este email.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

# Página inicial
@app.route('/')
def index():
    logging.info("Página inicial acessada")
    return render_template('index.html')

# Página de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Hash da senha
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Inserir o usuário no banco de dados
        conn = get_db_connection()
        try:
            with conn:
                conn.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email já cadastrado. Tente outro.', 'error')
        finally:
            conn.close()

    return render_template('cadastro.html', form=form)

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Verificar credenciais
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user['password'], password):
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Credenciais inválidas. Tente novamente.', 'error')

    return render_template('login.html', form=form)

# Página home
@app.route('/home')
def home():
    logging.info("Página home acessada")
    return render_template('home.html')

# Outras rotas
@app.route('/basedeconhecimento')
def BaseDeConhecimento():
    return render_template('baseConhecimento.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/importacaocsv')
def importcsv():
    return render_template('importCsv.html')

@app.route('/importacaojson')
def importjson():
    return render_template('importJson.html')

@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

# Servir arquivos estáticos
app.static_folder = os.path.join('..', 'frontend')

@app.route('/styles/<path:filename>')
def serve_css(filename):
    return send_from_directory(os.path.join('..', 'frontend', 'styles'), filename)

@app.route('/imagens/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join('..', 'frontend', 'assets', 'imagens'), filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(os.path.join('..', 'frontend', 'scripts'), filename)

# Tratamento de erros
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    logging.error(f"Erro interno: {error}")
    return render_template('500.html'), 500

# Inicializar a aplicação
if __name__ == '__main__':
    init_db()  # Configura o banco de dados
    app.run(debug=True)