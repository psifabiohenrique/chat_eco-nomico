import customtkinter as ctk
from src.components.graficos_economia import GraficosEconomia
from src.services.GerenciadorEstados import GerenciadorEstados

class JanelaGraficos(ctk.CTkFrame):
    """Classe do componente da janela de gráficos"""
    def __init__(self, master, estado: GerenciadorEstados, **kwargs):
        """Construtor da classe.
        Params:
            master: App
            estado: GerenciadorEstados
        Return:
            None"""
        super().__init__(master, **kwargs)
        
        # Configuração do Grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Inicializa o componente gráfico
        self.graficos_economia = GraficosEconomia(self)
        self.graficos_economia.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
    
        # Pega os valores DIRETAMENTE do estado passado
        valores_energia = [estado.energia_padrao, estado.energia_otimizada]
        valores_agua = [estado.agua_padrao, estado.agua_otimizada]
        
        # Atualiza o gráfico imediatamente
        self.graficos_economia.atualizar_dados(valores_energia, valores_agua)

    