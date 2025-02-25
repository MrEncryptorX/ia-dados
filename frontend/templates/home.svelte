<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>Home - InsightAI</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../styles/home.css">
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
                <a href="#" class="logo">InsightAI</a>
            </header>

            <main class="principal" role="main">
                <section class="welcome" aria-labelledby="welcome-header">
                    <h1 id="welcome-header">Acesse as funcionalidades principais abaixo.</h1>
                    <p>Bem-vindo ao seu painel de controle. Explore as ferramentas e recursos disponíveis para otimizar suas análises e previsões.</p>
                </section>

                <!-- Card "Base de Conhecimento" -->
                <section class="card-container" aria-labelledby="knowledge-header">
                    <article class="card">
                        <h2 id="knowledge-header">Base de Conhecimento</h2>
                        <p>Acesse artigos, tutoriais e guias detalhados para aproveitar ao máximo o InsightAI. Encontre respostas para suas perguntas e aprenda novas técnicas.</p>
                        <a href="{{ url_for('BaseDeConhecimento') }}" class="btn-acessar">Acessar</a>
                    </article>
                </section>

                <section class="container-arquivos" aria-labelledby="arquivos-header">
                    <h2 id="arquivos-header" class="sr-only">Importar Arquivos</h2>
                    <div class="arquivos">
                        <div class="arquivo">
                            <a href="../templates/importJson.html">
                                <img alt="Importar Arquivo JSON" src="{{ url_for('serve_images', filename='arquivo-json.png') }}">
                            </a>
                            <p>JSON</p> <!-- Adicionado texto para identificar o tipo de arquivo -->
                        </div>
                        <div class="arquivo">
                            <a href="../templates/importCsv.html">
                                <img alt="Importar Arquivo CSV" src="{{ url_for('serve_images', filename='csv.png') }}">
                            </a>
                            <p>CSV</p> <!-- Adicionado texto para identificar o tipo de arquivo -->
                        </div>
                        <div class="seta" aria-hidden="true">
                            <img alt="Seta para a direita" src="{{ url_for('serve_images', filename='seta-direita-de-linha-reta-fina.png') }}">
                        </div>
                        <div class="arquivo" aria-hidden="true">
                            <img alt="Imagem do Dashboard" src="{{ url_for('serve_images', filename='painel.png') }}">
                        </div>
                    </div>
                </section>
                
            </main>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>