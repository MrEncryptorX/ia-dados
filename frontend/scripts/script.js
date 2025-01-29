// script.js

const sendButton = document.getElementById('sendButton');
const userInput = document.getElementById('userInput');
const messagesContainer = document.getElementById('messages');

// Função para enviar mensagem e interagir com a OpenAI API
async function sendMessageToOpenAI(message) {
    const apiKey = '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';  // Substitua pela sua chave de API da OpenAI

    const requestData = {
        model: 'gpt-3.5-turbo',
        messages: [
            { role: 'user', content: message }
        ]
    };

    try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`,
            },
            body: JSON.stringify(requestData),
        });

        const data = await response.json();
        return data.choices[0].message.content;
    } catch (error) {
        console.error('Erro ao comunicar com a API da OpenAI:', error);
        return 'Desculpe, houve um erro ao tentar processar sua mensagem.';
    }
}

// Função para adicionar mensagens no chat
function addMessage(content, isUser = true) {
    const messageElement = document.createElement('div');
    messageElement.classList.add(isUser ? 'user-message' : 'ai-message');
    messageElement.innerText = content;
    messagesContainer.appendChild(messageElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Função do evento do botão de envio
sendButton.addEventListener('click', async () => {
    const message = userInput.value.trim();

    if (message) {
        // Exibir mensagem do usuário no chat
        addMessage(message, true);

        // Limpar a caixa de texto
        userInput.value = '';

        // Enviar mensagem para a OpenAI e exibir resposta
        const aiResponse = await sendMessageToOpenAI(message);
        addMessage(aiResponse, false);
    }
});
