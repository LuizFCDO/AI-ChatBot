# AI-ChatBot

Este projeto é um chatbot simples integrado a uma página web, demonstrando a integração de um Large Language Model (LLM) em uma interface web própria. Desenvolvido com propósitos educacionais, a estrutura pode ser facilmente adaptada para diversas aplicações, como suporte ao cliente em sites de vendas, assistente pessoal, ou ferramentas de geração de conteúdo.

## Tecnologias Utilizadas

*   **Backend:**
    *   Python
    *   Flask (Framework Web)
    *   `google-generativeai` (Biblioteca para integração com a API Google Gemini)
*   **Frontend:**
    *   HTML
    *   CSS
    *   JavaScript
*   **Gerenciamento de Dependências:**
    *   `requirements.txt`
*   **Configuração:**
    *   Variáveis de Ambiente (`.env`)

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

*   Python 3.6 ou superior
*   pip (gerenciador de pacotes do Python)

## Obtenção da API Key do Google Gemini

Para rodar este projeto, você precisará de uma chave de API do Google Gemini. Você pode obter uma gratuitamente através do **Google AI Studio**. Siga as instruções no site oficial para gerar sua chave.

## Configuração e Instalação

Siga os passos abaixo para configurar e rodar o projeto localmente:

1.  Clone este repositório:

    ```bash
    git clone https://github.com/LuizFCDO/AI-ChatBot.git
    cd AI-ChatBot
    ```

2.  (Opcional, mas recomendado) Crie um ambiente virtual para isolar as dependências:

    ```bash
    python -m venv venv
    ```

3.  Ative o ambiente virtual:

    *   No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   No macOS e Linux:
        ```bash
        source venv/bin/activate
        ```

4.  Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

5.  Crie um arquivo `.env` na raiz do projeto (no mesmo diretório de `app.py`) e adicione suas chaves de API e secreta:

    ```dotenv
    GEMINI_API_KEY=SUA_CHAVE_DA_API_DO_GOOGLE_GEMINI
    SECRET_KEY=UMA_CHAVE_SECRETA_ALEATORIA_PARA_SESSAO_DO_FLASK
    ```
    *(Nota: Substitua `SUA_CHAVE_DA_API_DO_GOOGLE_GEMINI` pela sua chave real da API Google Gemini e `UMA_CHAVE_SECRETA_ALEATORIA_PARA_SESSAO_DO_FLASK` por qualquer string aleatória e segura).*

## Como Rodar a Aplicação

1.  Certifique-se de que você está no diretório raiz do projeto e que o ambiente virtual está ativado (se você o criou).
2.  Execute o script principal do Flask:

    ```bash
    python app.py
    ```

3.  O servidor Flask será iniciado. Abra seu navegador web e acesse o endereço fornecido no terminal (geralmente `http://127.0.0.1:5000/`).

## Uso

Após acessar a aplicação no navegador:

*   Digite sua mensagem na caixa de texto na parte inferior da tela.
*   Pressione `Enter` ou clique no botão "Enviar" para enviar sua mensagem ao chatbot.
*   O chatbot responderá na área de chat acima.
*   O chatbot mantém o contexto da conversa, permitindo interações mais naturais e contínuas.
*   Clique no botão "Novo Chat" para limpar o histórico da conversa e iniciar uma nova interação.

## Estrutura do Projeto

A estrutura principal do projeto é organizada da seguinte forma:

```
AI-ChatBot/
├── app.py              # Script principal do Flask, backend
├── requirements.txt    # Dependências Python
├── .env.example        # Exemplo do arquivo .env (NÃO inclua seu .env real no Git!)
├── static/             # Arquivos estáticos (CSS, JS)
│   ├── style.css       # Estilos CSS
│   └── script.js       # Lógica JavaScript do frontend
└── templates/          # Arquivos HTML
    └── index.html      # Template principal da página
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para usar este projeto como base para suas próprias aplicações ou para propor melhorias.

Algumas ideias para contribuição incluem:

*   Melhorias na interface do usuário (UI) e experiência do usuário (UX).
*   Adicionar novas funcionalidades ao chatbot.
*   Explorar a integração com outros modelos de linguagem ou APIs.
*   Adaptar o chatbot para casos de uso específicos (e-commerce, educação, etc.).

Para contribuir, você pode:

1.  Fazer um fork do repositório.
2.  Criar uma branch para sua feature (`git checkout -b feature/NomeDaFeature`).
3.  Fazer commit das suas mudanças (`git commit -am 'Adiciona NomeDaFeature'`).
4.  Fazer push para a branch (`git push origin feature/NomeDaFeature`).
5.  Abrir um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

A Licença MIT é uma licença de software livre permissiva que permite reutilizar o código para qualquer propósito, com poucas restrições.

## Agradecimentos

*   Ao Google AI Studio pela plataforma para obter a API Key do Gemini.
*   Ao Cody (AI Coding Assistant da Sourcegraph) pelo auxílio na elaboração deste README e no desenvolvimento do código.

```