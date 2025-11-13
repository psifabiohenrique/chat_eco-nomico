import ollama

def checa_ollama_esta_executando() -> bool:
    try:
        ollama.ps()
        return True
    except ollama.RequestError:
        return False
    except Exception:
        return False

def requisicao_ollama(input_usuario: str, input_sistema: str | None = None) -> str:
    mensagens = []
    if input_sistema is not None:
        mensagens.append({"role": "system", "content": input_sistema})
    else:
        mensagens.append({"role": "system", "content": "Resuma o texto que o usuário enviou, sem interagir com ele"})

    mensagens.append({"role": "user", "content": input_usuario})

    modelo_usado = "llama3.1:8b" 
    # modelo_usado = "phi3:mini"

    try:
        resposta = ollama.chat(model=modelo_usado, messages=mensagens)
        
        if 'message' in resposta and 'content' in resposta['message']:
            return resposta['message']['content']
            
        return "Resposta do Ollama em formato inesperado."
        
    except ollama.ResponseError as e:
        if "model not found" in e.error:
            return f"Erro: Modelo '{modelo_usado}' não encontrado. Execute 'ollama pull {modelo_usado}' no terminal."
        return f"Erro na resposta do Ollama: {e.error}"
    except Exception as e:
        return f"Erro desconhecido ao chamar Ollama: {e}"

def obter_resposta_ollama(input_usuario: str) -> str:
    if not checa_ollama_esta_executando():
        return "Erro: O servidor do Ollama não está em execução. Por favor, inicie o Ollama."
    
    return requisicao_ollama(input_usuario=input_usuario, input_sistema=None)