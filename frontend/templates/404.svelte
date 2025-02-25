<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Não Encontrada</title>
    <link rel="stylesheet" href="{{ url_for('serve_css', filename='404.css') }}">
    <script src="{{ url_for('serve_js', filename='back.js') }}"></script>
</head>
<body>
    <div class="noise"></div>
    <div class="overlay"></div>
    <div class="terminal">
        <h1>Erro <span class="errorcode">404</span></h1>
        <p class="output">A página que você está procurando pode ter sido movida, renomeada ou está temporariamente indisponível.</p>
        <p class="output">
            Por favor, tente <a href="javascript:goBack()">voltar</a> ou 
            <a href="{{ url_for('home') }}">retornar à página inicial</a>.
        </p>
        <p class="output">Boa sorte.</p>
    </div>
</body>
</html>