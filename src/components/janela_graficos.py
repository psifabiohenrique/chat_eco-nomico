import customtkinter as ctk
## Comentado por ter removido a Classe
#from src.components.calculos_consumo import GraficosConsumo
from src.components.graficos_economia import GraficosEconomia

class JanelaGraficos(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs) 
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
       ## Comentado por ter removido a Classe 
       # self.graficos_consumo = GraficosConsumo(self)
       # self.graficos_consumo.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.graficos_economia = GraficosEconomia(self)
        self.graficos_economia.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
    
    #Ao fechar a o sistema, os gráficos não são salvos    
    def on_close(self):
        self.master.janela_graficos_instancia = None 
        self.destroy()
        
    ## Atualiza na Tela os dados do gráfico
    def atualizar_dados_publico(self, valores_energia_consumo, valores_agua_consumo, valores_energia_economia, valores_agua_economia):
        if self.winfo_exists():
            ## Comentado por ter removido a Classe
            #self.graficos_consumo.atualizar_dados(valores_energia_consumo, valores_agua_consumo)
            self.graficos_economia.atualizar_dados(valores_energia_economia, valores_agua_economia)