<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro InsightAI</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/cadastro.css') }}">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <script src="{{ url_for('static', filename='scripts/cadastro.js') }}"></script>
</head>
<body>
    <section class="container cadastro-section">
        <div class="left-panel">
            <h1>Junte-se ao InsightAI</h1>
            <h2>Explore novas possibilidades</h2>
        </div>

        <div class="right-panel">
            <div class="cadastro-box">
                <h2>Crie sua Conta</h2>
                <form method="POST" action="{{ url_for('cadastro') }}">
                    {{ form.csrf_token }}
                    <div class="input-container">
                        <i class="bx bxs-envelope"></i>
                        {{ form.email(placeholder="Digite seu e-mail", required=true) }}
                        {% if form.email.errors %}
                            <ul class="errors">
                                {% for error in form.email.errors %}
                                    <li>{{ error }}</li>
                                {% endfor %}
                            </ul>
                        {% endif %}
                    </div>
                    <div class="input-container">
                        <i class="bx bxs-lock-alt"></i>
                        {{ form.password(placeholder="Digite sua senha", required=True, id="password") }}
                        <span class="password-toggle">
                            <i class="bx bx-show toggle-password"></i>
                        </span>
                        {% if form.password.errors %}
                            <ul class="errors">
                                {% for error in form.password.errors %}
                                    <li>{{ error }}</li>
                                {% endfor %}
                            </ul>
                        {% endif %}
                    </div>
                    
                    <div class="input-container">
                        <i class="bx bxs-lock-alt"></i>
                        {{ form.confirm_password(placeholder="Confirme sua senha", required=True, id="confirm-password") }}
                        <span class="password-toggle">
                            <i class="bx bx-show toggle-password"></i>
                        </span>
                        {% if form.confirm_password.errors %}
                            <ul class="errors">
                                {% for error in form.confirm_password.errors %}
                                    <li>{{ error }}</li>
                                {% endfor %}
                            </ul>
                        {% endif %}
                    </div>
                    <button type="submit" class="btn-primary">Criar Conta</button>
                    <a href="{{ url_for('login') }}" class="btn-secondary">Já possui uma conta? Faça o login</a>
                </form>
            </div>
        </div>
    </section>
</body>
</html>