import threading

import customtkinter as ctk

from src.components.quadro_respostas import QuadroRespostas
from src.components.barra_lateral import BarraLateral
from src.components.quadro_chat import QuadroChat
from src.components.janela_graficos import JanelaGraficos
from src.services.GerenciadorEstados import GerenciadorEstados
from src.services.ia_gemini import obter_resposta_gemini


class Janelas:
    INICIO = 'INICIO'
    RESPOSTAS = 'RESPOSTAS'
    GRAFICOS = 'GRAFICOS'


class App(ctk.CTk):
    """Classe responsável por inicializar a interface gráfica e gerenciar os estados da aplicação"""

    def __init__(self):
        super().__init__()

        self.JANELAS = Janelas()

        self.title("Chat ECO-nômico")
        self.geometry("1000x700")
        """
        =============================================
        Cálculos de gastos conforme estudo (Making AI Less Thirsty: Uncovering 
        and Addressing the Seccret Water Footprint of AI Models)
        feito pela Universidade da Califórnia em Riverside e 
        da Universidade do Texas - 519ml de água e
        0,14kWh de energia (em média) para cada
        100 palavras geradas. 
        ===========================================
        
        """

        self.meu_estado = GerenciadorEstados()

        self.CUSTO_ENERGIA_KWH_100_PALAVRAS = 0.14
        self.CUSTO_AGUA_ML_100_PALAVRAS = 0.500


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)

        self.barra_lateral = BarraLateral(self,
                                          funcao_trocar_llm=self.ao_trocar_llm)
        self.barra_lateral.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.ao_trocar_llm(self.JANELAS.INICIO)

    def abrir_janela_graficos(self):
        if self.janela_graficos_instancia is None:
            print("[App] Criando nova janela de gráficos...")
            self.janela_graficos_instancia = JanelaGraficos(self)
        else:
            print("[App] Focando na janela de gráficos existente...")
            self.janela_graficos_instancia.focus()

    def atualizar_todos_graficos(self):
        if self.janela_graficos_instancia:
            print("[App] Enviando dados atualizados para a janela de gráficos...")
            # valores_energia_consumo = [self.total_energia_gemini_kwh, self.total_energia_ollama_kwh]
            # valores_agua_consumo = [self.total_agua_gemini_ml, self.total_agua_ollama_ml]
            valores_energia_economia = [self.total_energia_padrao_kwh, self.total_energia_gemini_kwh]
            valores_agua_economia = [self.total_agua_padrao_ml, self.total_agua_gemini_ml]

            self.janela_graficos_instancia.atualizar_dados_publico(
                # valores_energia_consumo, valores_agua_consumo,
                valores_energia_economia, valores_agua_economia
            )
        """
        REALIZANDO A SEPARAÇÃO DAS PALAVRAS POR ESPAÇO EM BRANCO
        """

    def contar_palavras(self, texto: str) -> int:
        return len(texto.split())

    def ao_trocar_llm(self, nome_llm: str):
        if nome_llm == self.JANELAS.INICIO:
            self.quadro_resp = QuadroChat(self, self.meu_estado, self.processar_prompt)
            self.quadro_resp.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)
        elif nome_llm == self.JANELAS.RESPOSTAS:
            self.quadro_resp = QuadroRespostas(self, self.meu_estado)
            self.quadro_resp.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)
        elif nome_llm == self.JANELAS.GRAFICOS:
            self.quadro_resp = JanelaGraficos(self)
            self.quadro_resp.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)

    def processar_prompt(self):
        self.meu_estado.resposta_original = 'Começando a processar com o GEMINI'
        self.meu_estado.resposta_processada = 'Começando a processar com o GEMINI'
        threading.Thread(target=self.processar_prompt_background).start()

    def processar_prompt_background(self):
        self.meu_estado.resposta_original, self.meu_estado.contador_tokens_original = obter_resposta_gemini(
            self.meu_estado.prompt_original)
        self.meu_estado.resposta_processada, self.meu_estado.contador_tokens_processado = obter_resposta_gemini(
            self.meu_estado.prompt_processado)
        self.ao_trocar_llm(self.JANELAS.RESPOSTAS)


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
