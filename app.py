from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
import os
import google.generativeai as genai # Import recomendado para a API Gemini

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configurações da API e do Flask
api_key = os.getenv('GEMINI_API_KEY')
secret_key = os.getenv('SECRET_KEY')
# IMPORTANTE: Verifique se "gemini-2.0-flash" é um nome de modelo válido e disponível para sua API Key.
# Modelos comuns incluem "gemini-1.5-flash-latest", "gemini-pro", etc.
# Usarei o que você forneceu, mas pode precisar de ajuste.
model_name = "gemini-2.0-flash"
system_instruction_text = "Você é um chatbot de suporte ao cliente, que sempre responde de forma sucinta mas informativa."

# Verifica se as chaves estão definidas
if not api_key:
    print("Erro: A variável de ambiente 'GEMINI_API_KEY' não está definida.")
    exit()
if not secret_key:
    print("Erro: A variável de ambiente 'SECRET_KEY' não está definida.")
    exit()

# Configura a API Key do Gemini
genai.configure(api_key=api_key)

# Configura o Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key # Configura a chave secreta para sessões

# Rota principal que serve a página HTML
@app.route('/')
def index():
    # Ao carregar a página, limpa o histórico da sessão para iniciar um novo chat.
    # Se você quiser que o chat persista entre atualizações da página (enquanto a sessão Flask estiver ativa),
    # você pode remover esta linha ou movê-la para uma lógica de "novo chat" mais explícita.
    session.pop('chat_history', None)
    return render_template('index.html')

# Rota para resetar o chat
@app.route('/reset', methods=['POST'])
def reset_chat():
    session.pop('chat_history', None)
    return jsonify({"status": "Chat resetado"})

@app.route('/chat', methods=['POST'])
def chat_route(): # Renomeado para evitar conflito com a variável 'chat' local
    user_message_text = request.json.get('message')
    if not user_message_text:
        return jsonify({"error": "Mensagem vazia"}), 400

    try:
        # Recupera o histórico da sessão Flask.
        # O histórico será uma lista de dicionários no formato que a API espera.
        chat_history_from_session = session.get('chat_history', [])

        # Configura o modelo generativo com a instrução de sistema
        model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_instruction_text
        )

        # Inicia uma sessão de chat com o histórico recuperado
        # A biblioteca `google-genai` pode converter a lista de dicionários em objetos `Content` internamente.
        chat_session_obj = model.start_chat(history=chat_history_from_session)

        # Envia a nova mensagem do usuário
        response = chat_session_obj.send_message(user_message_text)

        # Atualiza o histórico na sessão Flask.
        # `chat_session_obj.history` contém a lista completa de mensagens (objetos Content).
        # Precisamos convertê-los para um formato serializável para a sessão (lista de dicts).
        updated_history_for_session = []
        for content in chat_session_obj.history:
            # Garante que estamos extraindo texto das partes de forma segura
            parts_text = "".join(part.text for part in content.parts if hasattr(part, 'text'))
            updated_history_for_session.append({
                "role": content.role,
                "parts": [{"text": parts_text}]
            })
        session['chat_history'] = updated_history_for_session

        # Retorna a resposta do modelo
        bot_response_text = ""
        if hasattr(response, 'text') and response.text:
            bot_response_text = response.text
        elif response.parts:
            bot_response_text = "".join(part.text for part in response.parts if hasattr(part, 'text'))
        else:
            # Se não houver texto, pode ser um bloqueio ou outro problema
            print(f"Resposta do modelo sem texto: {response.prompt_feedback}")
            if response.prompt_feedback and response.prompt_feedback.block_reason:
                 return jsonify({"error": f"Mensagem bloqueada: {response.prompt_feedback.block_reason_message or response.prompt_feedback.block_reason}"}), 500
            return jsonify({"error": "Resposta do modelo não contém texto utilizável."}), 500
            
        return jsonify({"response": bot_response_text})

    except Exception as e:
        print(f"Erro ao interagir com a API Gemini: {e}")
        # Você pode querer registrar o erro de forma mais detalhada aqui
        return jsonify({"error": "Ocorreu um erro ao processar sua mensagem."}), 500

# Executa o aplicativo Flask
if __name__ == '__main__':
    # Use debug=True apenas para desenvolvimento
    app.run(debug=True)