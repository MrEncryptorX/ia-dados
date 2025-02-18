document.addEventListener('DOMContentLoaded', function() {
    // Seleciona os campos de input de senha e confirmação de senha
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirm-password');

    // Seleciona todos os botões de alternância de senha
    const togglePasswordButtons = document.querySelectorAll('.toggle-password');

    // Adiciona um ouvinte de evento de clique a cada botão de alternância de senha
    togglePasswordButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            // Impede o comportamento padrão do botão (se for um botão)
            event.preventDefault();
            // Alterna a visibilidade da senha
            togglePasswordVisibility(this);
        });
    });

    // Função para alternar a visibilidade da senha
    function togglePasswordVisibility(button) {
        // Obtém o campo de input de senha correspondente ao botão
        const inputField = button.previousElementSibling;

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