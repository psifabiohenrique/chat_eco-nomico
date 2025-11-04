import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    print("AVISO: API_KEY não encontrada no .env. A API do Gemini falhará.")

try:
   
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("[API] Modelo 'gemini-1.5-flash' carregado com sucesso.")
except Exception as e:
    print(f"ERRO ao carregar o modelo: {e}")
    model = None

def obter_resposta_gemini(prompt: str) -> str:
    if not model:
        return "Erro: modelo não carregado."

    try:
        resposta = model.generate_content(prompt)

        try:
            return resposta.text.strip()
        except:
            return resposta.candidates[0].content.parts[0].text.strip()

    except Exception as e:
        return f"Erro na API do Gemini: {e}"
