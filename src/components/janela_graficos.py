import customtkinter as ctk
from components.calculos_consumo import GraficosConsumo
from components.graficos_economia import GraficosEconomia

class JanelaGraficos(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.title("Gráficos de Consumo e Economia")
        self.geometry("550x650") 
        self.protocol("WM_DELETE_WINDOW", self.on_close) 

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.graficos_consumo = GraficosConsumo(self)
        self.graficos_consumo.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.graficos_economia = GraficosEconomia(self)
        self.graficos_economia.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
    
        self.after(10, self.master.atualizar_todos_graficos)
        
    def on_close(self):
        self.master.janela_graficos_instancia = None 
        self.destroy()

    def atualizar_dados_publico(self, valores_energia_consumo, valores_agua_consumo, valores_energia_economia, valores_agua_economia):
        if self.winfo_exists():
            self.graficos_consumo.atualizar_dados(valores_energia_consumo, valores_agua_consumo)
            self.graficos_economia.atualizar_dados(valores_energia_economia, valores_agua_economia)