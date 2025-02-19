document.addEventListener('DOMContentLoaded', function() {
    // Seleciona todos os containers de input que contêm campos de senha
    const passwordContainers = document.querySelectorAll('.input-container');

    // Itera sobre cada container de input de senha
    passwordContainers.forEach(container => {
        // Seleciona o campo de input de senha dentro deste container
        const passwordInput = container.querySelector('input[type="password"]');

        // Seleciona o botão de alternância de senha dentro deste container
        const togglePasswordButton = container.querySelector('.toggle-password');

        // Verifica se o campo de input de senha e o botão de alternância existem
        if (passwordInput && togglePasswordButton) {
            // Adiciona um ouvinte de evento de clique ao botão de alternância de senha
            togglePasswordButton.addEventListener('click', function(event) {
                // Impede o comportamento padrão do botão (se for um link ou botão)
                event.preventDefault();

                // Alterna a visibilidade da senha
                togglePasswordVisibility(passwordInput, this);
            });
        }
    });

    // Função para alternar a visibilidade da senha
    function togglePasswordVisibility(inputField, button) {
        // Obtém o tipo atual do campo de input
        const type = inputField.type === 'password' ? 'text' : 'password';

        // Define o novo tipo do campo de input
        inputField.type = type;

        // Alterna as classes CSS para mudar o ícone
        if (type === 'password') {
            button.classList.remove('bx-hide');
            button.classList.add('bx-show');
        } else {
            button.classList.remove('bx-show');
            button.classList.add('bx-hide');
        }
    }
});