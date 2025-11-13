import customtkinter as ctk

class QuadroChat(ctk.CTkFrame):
    def __init__(self, master, funcao_enviar_prompt, **kwargs):
        super().__init__(master, **kwargs)
        
        self.funcao_enviar_prompt = funcao_enviar_prompt

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.caixa_texto = ctk.CTkTextbox(self, state="disabled", font=("Arial", 14))
        self.caixa_texto.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))

        self.campo_entrada = ctk.CTkEntry(self, placeholder_text="Digite sua mensagem...", font=("Arial", 14))
        self.campo_entrada.grid(row=1, column=0, sticky="ew", padx=10, pady=(5, 10))
        
        self.campo_entrada.bind("<Return>", self.ao_enviar_pressionado)

    def ao_enviar_pressionado(self, event=None):
        prompt = self.campo_entrada.get()
        if prompt:
            self.campo_entrada.delete(0, "end")
            self.adicionar_mensagem("Você", prompt)
            self.funcao_enviar_prompt(prompt)

    def adicionar_mensagem(self, remetente: str, mensagem: str):
        self.caixa_texto.configure(state="normal")
        self.caixa_texto.insert("end", f"{remetente}: {mensagem}\n\n")
        self.caixa_texto.configure(state="disabled")
        self.caixa_texto.see("end")