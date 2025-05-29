document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const resetButton = document.getElementById('reset-button');

    // Função para adicionar uma mensagem à caixa de chat
    function addMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `${sender}-message`);
        const html = marked.parse(message);
        messageElement.innerHTML = html;
        chatBox.appendChild(messageElement);
        // Rola para a mensagem mais recente
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // Função para enviar a mensagem para o backend
    async function sendMessage() {
        const message = userInput.value.trim();
        if (message === '') {
            return; // Não envia mensagens vazias
        }

        // Adiciona a mensagem do usuário à interface
        addMessage(message, 'user');
        userInput.value = ''; // Limpa o input

        // Adiciona uma mensagem de "digitando" ou indicador de carregamento
        const loadingMessage = document.createElement('div');
        loadingMessage.classList.add('message', 'bot-message', 'loading');
        loadingMessage.textContent = 'Digitando...'; // Ou um spinner, etc.
        chatBox.appendChild(loadingMessage);
        chatBox.scrollTop = chatBox.scrollHeight;


        try {
            // Envia a mensagem para a rota /chat no backend
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            });

            // Remove a mensagem de carregamento
            chatBox.removeChild(loadingMessage);

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Erro na resposta do servidor');
            }

            const data = await response.json();
            // Adiciona a resposta do bot à interface
            addMessage(data.response, 'bot');

        } catch (error) {
            console.error('Erro ao enviar mensagem:', error);
             // Remove a mensagem de carregamento se ainda estiver lá
            if (chatBox.contains(loadingMessage)) {
                 chatBox.removeChild(loadingMessage);
            }
            // Exibe uma mensagem de erro na interface
            addMessage('Erro: Não foi possível obter resposta.', 'bot');
        }
    }

    // Função para resetar o chat
    async function resetChat() {
         try {
            const response = await fetch('/reset', {
                method: 'POST',
            });

            if (!response.ok) {
                 const errorData = await response.json();
                throw new Error(errorData.error || 'Erro ao resetar chat no servidor');
            }

            // Limpa a caixa de chat (exceto a mensagem inicial)
            chatBox.innerHTML = '<div class="message bot-message">Olá! Como posso ajudar hoje?</div>';
            addMessage('Chat resetado. Podemos começar uma nova conversa.', 'bot');


         } catch (error) {
             console.error('Erro ao resetar chat:', error);
             addMessage('Erro: Não foi possível resetar o chat.', 'bot');
         }
    }


    // Adiciona listeners de evento
    sendButton.addEventListener('click', sendMessage);

    userInput.addEventListener('keypress', (event) => {
        // Envia a mensagem ao pressionar Enter
        if (event.key === 'Enter') {
            event.preventDefault(); // Previne a quebra de linha padrão
            sendMessage();
        }
    });

    resetButton.addEventListener('click', resetChat);

});