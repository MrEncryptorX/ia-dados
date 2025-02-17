document.addEventListener('DOMContentLoaded', (event) => {
    const togglePassword = document.getElementById('togglePassword');
    const password = document.getElementById('password');
    const form = document.querySelector('form');
    const errorMessage = document.getElementById('error-message');
    const btnCadastro = document.getElementById('btnCadastro');
    const btnAcessar = document.querySelector('.btn-primary'); // Seleciona o botão "Acessar"

    // Função para alternar a visibilidade da senha
    togglePassword.addEventListener('click', function () {
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type);
        this.classList.toggle('bxs-show');
        this.classList.toggle('bxs-hide');
    });

    // Função para validar o formulário no lado do cliente
    window.validateForm = function () {
        const email = document.getElementById('email').value;
        const passwordValue = password.value;

        // Expressão regular para validar o formato do e-mail
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            showError('Por favor, insira um e-mail válido.');
            return false;
        }

        // Validação da senha (pelo menos 8 caracteres)
        if (passwordValue.length < 8) {
            showError('A senha deve ter pelo menos 8 caracteres.');
            return false;
        }

        clearError(); // Limpa a mensagem de erro se tudo estiver válido
        return true;
    };

    // Função para exibir mensagens de erro
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
    }

    // Função para limpar mensagens de erro
    function clearError() {
        errorMessage.textContent = '';
        errorMessage.style.display = 'none';
    }

    // Adicionando um ouvinte de evento para o botão "Acessar"
    btnAcessar.addEventListener('click', function(event) {
        event.preventDefault(); // Previne o comportamento padrão do link
        if (validateForm()) {
            form.submit(); // Envia o formulário se a validação for bem-sucedida
        }
    });

    // Log para o botão "Criar minha conta" (opcional, para debug)
    if (btnCadastro) {
        btnCadastro.addEventListener('click', function() {
            console.log('Link de cadastro clicado');
        });
    }
});