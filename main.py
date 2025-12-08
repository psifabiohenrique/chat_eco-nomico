import threading
import customtkinter as ctk

from src.components.quadro_respostas import QuadroRespostas
from src.components.barra_lateral import BarraLateral
from src.components.quadro_chat import QuadroChat
from src.components.janela_graficos import JanelaGraficos
from src.services.GerenciadorEstados import GerenciadorEstados
from src.services.ia_gemini import obter_resposta_gemini


class Janelas:
    INICIO = "INICIO"
    RESPOSTAS = "RESPOSTAS"
    GRAFICOS = "GRAFICOS"


class App(ctk.CTk):
    """Classe responsável por inicializar a interface gráfica e gerenciar os estados da aplicação. Herda de ctk.CTk"""

    def __init__(self):
        """Construtor da classe"""
        super().__init__()

        self.JANELAS = Janelas()

        self.title("Chat ECO-nômico")
        self.geometry("1000x700")

        """
        =============================================
        Cálculos de gastos conforme estudo (Making AI Less Thirsty: Uncovering 
        and Addressing the Secret Water Footprint of AI Models).
        
        Valores de referência para cada 100 unidades (neste caso, adaptado para Tokens):
        - 0.14 kWh de energia
        - 500 mL de água
        ===========================================
        """

        self.meu_estado = GerenciadorEstados()

        self.CUSTO_ENERGIA_KWH_100_TOKENS = 0.14
        self.CUSTO_AGUA_ML_100_TOKENS = 0.500

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)

        self.barra_lateral = BarraLateral(self, funcao_trocar_llm=self.ao_trocar_llm)
        self.barra_lateral.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Variável para controlar o quadro atual exibido na direita
        self.quadro_resp = None

        # Inicia na tela inicial
        self.ao_trocar_llm(self.JANELAS.INICIO)

    def ao_trocar_llm(self, nome_llm: str):
        """Função responsável por alterar os componentes exibidos (i.e., janela de inicio, de respostas e de gráficos).
        
        Params:
            nome_llm: string
        Return:
            None"""
        # Limpa o quadro anterior da memória e da tela antes de criar o novo
        if self.quadro_resp is not None:
            self.quadro_resp.destroy()

        if nome_llm == self.JANELAS.INICIO:
            self.quadro_resp = QuadroChat(self, self.meu_estado, self.processar_prompt)
            self.quadro_resp.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)

        elif nome_llm == self.JANELAS.RESPOSTAS:
            self.quadro_resp = QuadroRespostas(self, self.meu_estado)
            self.quadro_resp.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)

        elif nome_llm == self.JANELAS.GRAFICOS:
            # Passa o estado atualizado para a janela de gráficos
            self.quadro_resp = JanelaGraficos(self, self.meu_estado)
            self.quadro_resp.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)

    def processar_prompt(self):
        """Inicia o processamento dos prompts com threads para não travar a interface"""
        self.meu_estado.resposta_original = "Começando a processar com o GEMINI..."
        self.meu_estado.resposta_processada = "Começando a processar com o GEMINI..."
        threading.Thread(target=self.processar_prompt_background).start()

    def processar_prompt_background(self):
        """Processa os prompts com o gemini. Deve ser executada dentro de uma thread"""
        # 1. Obtém as respostas da IA (O return já traz: texto_resposta, total_tokens)
        # A função obter_resposta_gemini já retorna o total de tokens da transação (input + output)
        (
            self.meu_estado.resposta_processada,
            self.meu_estado.contador_tokens_processado,
        ) = obter_resposta_gemini(self.meu_estado.prompt_processado)

        (
            self.meu_estado.resposta_original,
            self.meu_estado.contador_tokens_original,
        ) = obter_resposta_gemini(self.meu_estado.prompt_original)

        # ==============================================================================
        # CÁLCULO 1: CENÁRIO PADRÃO (Baseado em TOKENS)
        # ==============================================================================
        total_tokens_padrao = self.meu_estado.contador_tokens_original

        # Fórmula: (Total Tokens / 100) * Custo Unitário
        self.meu_estado.energia_padrao = (
            total_tokens_padrao / 100
        ) * self.CUSTO_ENERGIA_KWH_100_TOKENS
        self.meu_estado.agua_padrao = (
            total_tokens_padrao / 100
        ) * self.CUSTO_AGUA_ML_100_TOKENS

        # ==============================================================================
        # CÁLCULO 2: CENÁRIO OTIMIZADO (Baseado em TOKENS)
        # ==============================================================================
        total_tokens_otimizado = self.meu_estado.contador_tokens_processado

        self.meu_estado.energia_otimizada = (
            total_tokens_otimizado / 100
        ) * self.CUSTO_ENERGIA_KWH_100_TOKENS
        self.meu_estado.agua_otimizada = (
            total_tokens_otimizado / 100
        ) * self.CUSTO_AGUA_ML_100_TOKENS
        print(f"Total tokens padrão: {total_tokens_padrao}")
        print(f"Total tokens otimizado: {total_tokens_otimizado}")

        self.after(0, lambda: self.ao_trocar_llm(self.JANELAS.RESPOSTAS))


if __name__ == "__main__":
    try:
        import customtkinter
    except ImportError:
        print("Erro: Pacote 'customtkinter' não encontrado.")
        print("Por favor, instale com: pip install customtkinter")
        exit()

    try:
        import matplotlib
    except ImportError:
        print("Erro: Pacote 'matplotlib' não encontrado.")
        print("Por favor, instale com: pip install matplotlib")
        exit()

    ctk.set_appearance_mode("dark")

    app = App()
    app.mainloop()
