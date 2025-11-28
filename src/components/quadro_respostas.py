import customtkinter as ctk

from src.services.GerenciadorEstados import GerenciadorEstados


class QuadroRespostas(ctk.CTkFrame):
    def __init__(self, master, estado: GerenciadorEstados):
        super().__init__(master)

        self.meu_estado = estado

        # self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(3, weight=2)
        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self, text='Resposta Processada').grid(row=0, column=0, sticky='nsew',  padx=10, pady=(10,5))
        self.caixa_texto_processado = ctk.CTkTextbox(self, state="normal", font=("Arial", 14))
        self.caixa_texto_processado.insert('0.0', self.meu_estado.resposta_processada)
        self.caixa_texto_processado.configure(state="disabled")
        self.caixa_texto_processado.grid(row=1, column=0, sticky='nsew', padx=10, pady=(10, 5))


        ctk.CTkLabel(self, text='Resposta Novo Prompt').grid(row=2, column=0,  sticky='nsew', padx=10, pady=(10,5))
        self.caixa_texto_original = ctk.CTkTextbox(self, state="normal", font=("Arial", 14))
        self.caixa_texto_original.insert('0.0', self.meu_estado.resposta_original)
        self.caixa_texto_original.configure(state="disabled")
        self.caixa_texto_original.grid(row=3, column=0, sticky='nsew', padx=10, pady=(10,5))
