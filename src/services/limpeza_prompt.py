import re

LISTA_PALAVRAS_REMOVER = [
    "por favor", "por gentileza", "se possível", "você poderia",
    "me diga", "me fala", "me responda", "me ajuda",
    "olá", "oi", "e aí", "opa",
    "bom dia", "boa tarde", "boa noite",
    "tchau", "até logo", "até mais",
    "obrigado", "obrigada", "valeu", "grato", "grata",
    "certo", "ok", "entendido", "entendi", "compreendi",
    "sabe", "tipo", "né", "tá", "ta",
    "ééé", "eee", "hmm", "hm"
]

def limpar_prompt(texto_original: str) -> str:
    texto_limpo = texto_original.lower()
    
    padrao_re = r'\b(' + '|'.join(re.escape(p) for p in LISTA_PALAVRAS_REMOVER) + r')\b'
    texto_limpo = re.sub(padrao_re, '', texto_limpo, flags=re.IGNORECASE)
    
    texto_limpo = re.sub(r'[?!.,;]+', '', texto_limpo)
    
    texto_limpo = re.sub(r'\s+', ' ', texto_limpo).strip()
    
    return texto_limpo if texto_limpo else texto_original