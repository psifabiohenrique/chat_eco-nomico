import customtkinter as ctk

class BarraLateral(ctk.CTkFrame):
    def __init__(self, master, funcao_trocar_llm, funcao_abrir_graficos, **kwargs):
        super().__init__(master, **kwargs)
        
        self.funcao_trocar_llm = funcao_trocar_llm
        self.funcao_abrir_graficos = funcao_abrir_graficos 

        self.grid_columnconfigure(0, weight=1) 

        self.rotulo_titulo = ctk.CTkLabel(self, text="LLMs - CHAT ECO-NOMICO", font=ctk.CTkFont(size=16, weight="bold"))
        self.rotulo_titulo.grid(row=0, column=0, pady=10, padx=20, sticky="ew")

        self.botao_gemini = ctk.CTkButton(self, text="Gemini", command=lambda: self.funcao_trocar_llm("gemini"))
        self.botao_gemini.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        self.botao_ollama = ctk.CTkButton(self, text="Ollama", command=lambda: self.funcao_trocar_llm("ollama"))
        self.botao_ollama.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

        self.botao_graficos = ctk.CTkButton(self, text="Abrir Gráficos", 
                                            command=self.funcao_abrir_graficos, 
                                            fg_color="#0056b3") 
        self.botao_graficos.grid(row=3, column=0, pady=(20, 10), padx=20, sticky="ew")