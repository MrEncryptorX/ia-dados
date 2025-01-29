from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
from app.services import data_processing, ai_service
from app.models.data_model import UploadedData

app = Flask(__name__)

# Configuração para upload de arquivos
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'json'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Página inicial
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Página "Home"
@app.route('/home')
def home_page():
    return render_template('home.html')

# Página "Login"
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Aqui você implementaria a lógica real de autenticação
        return jsonify({'username': username, 'status': 'Login recebido'})
    return render_template('login.html')

# Página "Cadastro"
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        # Aqui você implementaria a lógica real de cadastro
        return jsonify({'username': username, 'email': email, 'status': 'Usuário cadastrado'})
    return render_template('cadastro.html')

# Página "Upload de JSON"
@app.route('/importJson', methods=['GET', 'POST'])
def import_json():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "Nenhum arquivo enviado"}), 400
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result = data_processing.process_json(file_path)
            return jsonify(result), 200
    return render_template('importJson.html')

# Página "Upload de CSV"
@app.route('/importCsv', methods=['GET', 'POST'])
def import_csv():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "Nenhum arquivo enviado"}), 400
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result = data_processing.process_csv(file_path)
            return jsonify(result), 200
    return render_template('importCsv.html')

# Página "Relatórios"
@app.route('/relatorios')
def relatorios():
    # Aqui você pode adicionar lógica para gerar relatórios baseados nos dados processados
    return render_template('relatorios.html')

# Página "Chatbot"
@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.json.get('message')
        response = ai_service.chatbot_response(user_input)
        return jsonify({'response': response})
    return render_template('chatbot.html')

# Página "Base de Conhecimento"
@app.route('/baseConhecimento')
def base_conhecimento():
    # Aqui você pode adicionar lógica para recuperar e exibir a base de conhecimento
    return render_template('baseConhecimento.html')

# Nova rota para análise de dados
@app.route('/analisar', methods=['POST'])
def analisar_dados():
    data = request.json
    resultado_analise = ai_service.analisar_dados(data)
    return jsonify(resultado_analise)

if __name__ == '__main__':
    app.run(debug=True)