<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>InsightAI</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Descubra o poder da análise de dados e previsões inteligentes com o InsightAI. Transforme dados em insights valiosos.">
    <meta name="keywords" content="análise de dados, previsões inteligentes, insightAI, business intelligence">
    <link rel="stylesheet" href="{{ url_for('serve_css', filename='style.css') }}">
    <link rel="stylesheet" href="{{ url_for('serve_css', filename='reset.css') }}">
</head>
<body class="background-image">
    <header class="cabecalho">
        <h2 class="logo">InsightAI</h2>
        <nav class="cabecalho_menu">
            <a href="{{ url_for('login') }}" class="menu_link">Login</a>
            <a href="{{ url_for('cadastro') }}" class="menu_link">Cadastre-se</a>
        </nav>
    </header>

    <main>
        <section class="container principal">
            <div>
                <h1 class="texto-transicao titulo_principal">
                    <span class="destaque_titulo">InsightAI:</span> Onde dados encontram resultados.
                </h1>
            </div>
        </section>

        <section class="container segundo">
            <div class="container_sobre">
                <h2 class="titulo_descricao">
                    Descubra o poder da análise de dados e previsões inteligentes com o InsightAI.
                </h2>
                <p class="sobreNos">
                    Nossa plataforma oferece ferramentas avançadas para transformar dados em insights valiosos.
                </p>
            </div>
            <img class="imagem_segundo" src="{{ url_for('serve_images', filename='lampada.svg') }}" alt="lâmpada mágica">
        </section>

        <section class="container terceiro">
            <div class="grid">
                <div class="card">
                    <span class="icon">
                        <img src="https://img.icons8.com/material-rounded/24/upload--v1.png" alt="upload--v1"/>
                    </span>
                    <h4>UPLOAD DE DADOS</h4>
                    <p>Carregue seus dados e comece a análise imediatamente.</p>
                </div>

                <div class="card">
                    <span class="icon">
                        <img src="https://img.icons8.com/ios-glyphs/30/analytics.png" alt="analytics"/>
                    </span>
                    <h4>VER ANÁLISE BÁSICA</h4>
                    <p>Explore métricas fundamentais para entender seus dados.</p>
                </div>

                <div class="card">
                    <span class="icon">
                        <img src="https://img.icons8.com/material-sharp/24/vision.png" alt="vision"/>
                    </span>
                    <h4>SOLICITAR PREVISÕES</h4>
                    <p>Utilize nossas ferramentas de previsão para tomar decisões.</p>
                </div>
            </div>
        </section>

        <section class="container quarto">
            <h2 class="titulo">PREÇO DE ASSINATURA</h2>
            <div class="planos">
                <div class="plano">
                    <h3 class="plano-titulo">DELUXE</h3>
                    <p class="plano-descricao">
                        • O plano básico com limites em uploads de dados e relatórios, ideal para empresas que estão começando.
                    </p>
                    <p class="plano-preco">R$ 1.000</p>
                </div>
                <div class="plano">
                    <h3 class="plano-titulo">PROFISSIONAL</h3>
                    <p class="plano-descricao">
                        • Um plano intermediário com mais funcionalidades e menos restrições, projetado para empresas em crescimento.
                    </p>
                    <p class="plano-preco">R$ 5.000</p>
                </div>
                <div class="plano">
                    <h3 class="plano-titulo">ELITE</h3>
                    <p class="plano-descricao">
                        • O plano completo com todas as funcionalidades disponíveis, sem limites, perfeito para empresas que precisam de análises extensivas.
                    </p>
                    <p class="plano-preco">R$ 10.000</p>
                </div>
            </div>
        </section>

        <section class="container quinto">
            <h2 class="tituloQuinto">Pronto para chegar ao resultados com a gente?</h2>
            <h3 class="subtituloQuinto">Nos envie uma mensagem!</h3>
            <div class="gridQuinto">
                <div class="cardQuinto">
                    <h4>TELEFONE</h4>
                    <p>+55 (41) 99999-9999</p>
                </div>
                <div class="cardQuinto">
                    <h4>E-MAIL</h4>
                    <p>personal_department@insightAi.com</p>
                </div>
                <div class="cardQuinto">
                    <h4>Social</h4> 
                    <p>Redes sociais</p>
                </div>
            </div>
        </section>
    </main>
</body>
</html>