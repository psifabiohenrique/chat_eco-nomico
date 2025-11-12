import customtkinter as ctk

class QuadroRespostas(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(3, weight=2)
        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self, text='Resposta Original').grid(row=0, column=0, sticky='nsew',  padx=10, pady=(10,5))
        self.caixa_texto_ollama = ctk.CTkTextbox(self, state="disabled", font=("Arial", 14))
        self.caixa_texto_ollama.grid(row=1, column=0, sticky='nsew', padx=10, pady=(10,5))


        ctk.CTkLabel(self, text='Resposta Novo Prompt').grid(row=2, column=0,  sticky='nsew', padx=10, pady=(10,5))
        self.caixa_texto_gemini = ctk.CTkTextbox(self, state="disabled", font=("Arial", 14))
        self.caixa_texto_gemini.grid(row=3, column=0, sticky='nsew', padx=10, pady=(10,5))
