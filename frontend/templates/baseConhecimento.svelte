<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>Documentação - InsightAI</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../styles/baseConhecimento.css">
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
                <a href="../templates/home.html" class="logo" aria-label="Ir para a Página Inicial do InsightAI">InsightAI</a>
            </header>
            <main class="principal" role="main">
                <section class="welcome" aria-labelledby="welcome-header">
                    <h1 id="welcome-header">Bem-vindo à Documentação do InsightAI</h1>
                    <p>Aqui você encontrará informações detalhadas sobre como usar o InsightAI de forma eficiente e aproveitar todos os recursos da plataforma.</p>
                </section>
            
                <section class="documentacao" aria-labelledby="overview-header">
                    <h2 id="overview-header">Visão Geral</h2>
                    <p>O InsightAI é uma ferramenta poderosa para análise de dados e criação de relatórios automatizados. Abaixo, você pode explorar os principais recursos da plataforma.</p>
            
                    <h2 id="features-header">Funcionalidades</h2>
                    <ul aria-labelledby="features-header">
                        <li><strong>Dashboard:</strong> Acesse a visão geral dos seus dados e resultados.</li>
                        <li><strong>Upload de Dados:</strong> Carregue seus arquivos JSON e CSV para análise.</li>
                        <li><strong>Chatbot:</strong> Interaja com nosso assistente inteligente para tirar dúvidas e automatizar tarefas.</li>
                        <li><strong>Relatórios:</strong> Gere relatórios personalizados com base nos dados analisados.</li>
                        <li><strong>Configurações:</strong> Personalize a plataforma conforme as suas necessidades.</li>
                    </ul>
            
                    <h2 id="using-header">Como Utilizar</h2>
                    <p>Aqui estão os passos para utilizar a plataforma de forma eficiente:</p>
                    <ol aria-labelledby="using-header">
                        <li><strong>Faça o upload de seus dados:</strong> Carregue arquivos JSON ou CSV para iniciar a análise.</li>
                        <li><strong>Explore os relatórios:</strong> Visualize gráficos e relatórios gerados automaticamente.</li>
                        <li><strong>Use o chatbot:</strong> Tire dúvidas sobre como utilizar as funcionalidades ou obtenha suporte técnico.</li>
                        <li><strong>Configure a plataforma:</strong> Ajuste preferências e configurações conforme sua necessidade.</li>
                    </ol>
            
                    <h2 id="important-header">Importante</h2>
                    <p>Certifique-se de que os dados carregados estejam formatados corretamente para garantir que as análises e relatórios sejam precisos. Em caso de dúvidas, consulte nossa seção de FAQ ou entre em contato com o suporte técnico.</p>
                </section>
            </main>
        </div>
    </div>
            
    <script src="script.js"></script>
</body>
</html>