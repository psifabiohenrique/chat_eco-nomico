import customtkinter as ctk
from PIL import Image

class BarraLateral(ctk.CTkFrame):
    """Classe responsável pelo componente do menu lateral da aplicação"""
    def __init__(self, master, funcao_trocar_llm, **kwargs):
        """Método construtor do componente.
        Params:
            master: App
            funcao_trocar_llm: função que altera o componente principal exibido
        """
        super().__init__(master, **kwargs)
        
        self.funcao_trocar_llm = funcao_trocar_llm

        self.grid_columnconfigure(0, weight=1) 

        self.rotulo_titulo = ctk.CTkLabel(self, text="LLMs - CHAT ECO-NOMICO", font=ctk.CTkFont(size=16, weight="bold"))
        self.rotulo_titulo.grid(row=0, column=0, pady=10, padx=20, sticky="ew")

        self.botao_gemini = ctk.CTkButton(self, text="Início", command=lambda: self.funcao_trocar_llm(self.master.JANELAS.INICIO))
        self.botao_gemini.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        self.botao_ollama = ctk.CTkButton(self, text="Respostas", command=lambda: self.funcao_trocar_llm(self.master.JANELAS.RESPOSTAS))
        self.botao_ollama.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

        self.botao_graficos = ctk.CTkButton(self, text="Abrir Gráficos", 
                                            command=lambda: self.funcao_trocar_llm(self.master.JANELAS.GRAFICOS), 
                                            fg_color="#0056b3") 
        self.botao_graficos.grid(row=3, column=0, pady=(20, 10), padx=20, sticky="ew")

        img = Image.open('./imagens/logo-unb.png')
        imagem = ctk.CTkImage(img, size=(300, 100))
        ctk.CTkLabel(self, image=imagem, text='').grid(row=4, column=0, pady=(20, 10))