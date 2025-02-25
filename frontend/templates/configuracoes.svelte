<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>Configurações - InsightAI</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('serve_css', filename='configuracoes.css') }}">
</head>
<body>
    <div class="container">
        <!-- Menu lateral -->
        <aside class="menu-lateral" aria-label="Menu Lateral">
            <nav>
                <ul class="menu-principal">
                    <li><a href="{{ url_for('home') }}">Dashboard</a></li>
                    <li><a href="#">Upload de Dados</a></li>
                    <li><a href="{{ url_for('chatbot') }}">Chatbot</a></li>
                    <li><a href="{{ url_for('relatorios') }}">Relatórios</a></li>
                </ul>
                <ul class="menu-secundario">
                    <li><a href="{{ url_for('configuracoes') }}">Configurações</a></li>
                    <li><a href="{{ url_for('index') }}">Sobre Nós</a></li>
                    <li><a href="{{ url_for('index') }}">Sair</a></li>
                </ul>
            </nav>
        </aside>

        <!-- Conteúdo principal -->
        <div class="conteudo">
            <header class="cabecalho" role="banner">
                <a href="{{ url_for('home') }}" class="logo">InsightAI</a>
            </header>

            <main class="principal" role="main">
                <section class="configuracoes" aria-labelledby="configuracoes-header">
                    <h1 id="configuracoes-header">Configurações do Sistema</h1>
                    <form action="#" method="post">
                        <div class="form-group">
                            <label for="btn-theme-select">Tema:</label>
                            <select id="btn-theme-select" name="theme">
                                <option value="dark">Escuro</option>
                                <option value="light">Claro</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="btn-language-select">Idioma:</label>
                            <select id="btn-language-select" name="language">
                                <option value="pt-br">Português</option>
                                <option value="en">Inglês</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="notifications-toggle">Notificações:</label>
                            <input type="checkbox" id="notifications-toggle" name="notifications" checked>
                        </div>
                        <button type="submit" class="btn-submit">Salvar Alterações</button>
                    </form>
                </section>
            </main>
        </div>
    </div>

    <script src="{{ url_for('serve_js', filename='script.js') }}"></script>
</body>
</html>