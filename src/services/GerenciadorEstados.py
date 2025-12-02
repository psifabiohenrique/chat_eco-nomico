class GerenciadorEstados:
    def __init__(self):
        self.prompt_original = ''
        self.prompt_processado = ''
        self.resposta_original = ''
        self.resposta_processada = ''
        self.contador_tokens_original = 0
        self.contador_tokens_processado = 0
        
        self.energia_padrao = 0.0
        self.agua_padrao = 0.0
        self.energia_otimizada = 0.0
        self.agua_otimizada = 0.0
