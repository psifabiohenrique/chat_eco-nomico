import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()

def obter_resposta_gemini(input_usuario: str) -> tuple[str, int]:
    """
    Recebe obrigatóriamente um input de usuário. Envia para o GEMINI processar as entradas e retornar uma tupla, com a string de resultado no indice 0 e o inteiro do total de tokens no indice 1.
    """
    api_key = os.getenv("API_KEY")
    if api_key is None:
        raise Exception("A Chave de API não está configurada na variável de ambiente!")
    
    try:
        client = genai.Client(api_key=api_key)


        resposta = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=input_usuario,
        )
        contador_tokens_totais = resposta.usage_metadata.total_token_count # type: ignore
        texto_resposta = resposta.text

        return texto_resposta, contador_tokens_totais # type: ignore
    except errors.APIError as e:
        return e.__str__(), 0