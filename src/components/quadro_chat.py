import threading
import tkinter

import customtkinter as ctk
import ollama

from src.services.GerenciadorEstados import GerenciadorEstados

INSTRUCAO_SISTEMA = """PROMPT NOVO: [INSTRUÇÕES DO SISTEMA E FUNÇÃO]
VOCÊ É UM OTIMIZADOR DE PROMPT. SUA TAREFA É RECEBER UM PROMPT E REESCREVÊ-LO PARA SUA FORMA MAIS CONCISA, SIMPLES E DIRETA.
O PROMPT OTIMIZADO DEVE MANTER EXATAMENTE O MESMO SENTIDO E RESULTADO ESPERADO DO PROMPT ORIGINAL.
REMOVA TODOS OS VERBOS E FRASES DE PREENCHIMENTO DESNECESSÁRIOS.
SEJA EXTREMAMENTE CONCISO. NÃO USE INTRODUÇÕES OU CONCLUSÕES.

[REGRAS E FORMATO]
1. O PROMPT OTIMIZADO DEVE SER MENOR (OU IGUAL) AO COMPRIMENTO DO PROMPT ORIGINAL.
2. A SAÍDA FINAL DEVE SER LIVRE DE QUALQUER ESTEREÓTIPO OU VIÉS PESSOAL.

[EXEMPLOS]
-- EXEMPLO 1 --
ENTRADA: "Boa tarde, tudo bem, chat? Eu gostaria de saber o que eu deveria fazer para conseguir aprender Cálculo I? Estou com vontade de aprender porque é algo muito bonito, mas parece ser tão difícil."
SAÍDA: O que eu deveria fazer para aprender Cálculo I?
-- EXEMPLO 2 --
ENTRADA: "Olha, eu estava pensando se você conseguiria fazer uma lista para mim, com no máximo cinco itens, das principais vantagens do uso da energia solar em ambientes residenciais. Seria muito útil."
SAÍDA: Liste 5 vantagens da energia solar em residências.
-- EXEMPLO 3 --
ENTRADA: "Com o devido respeito, venho por meio desta solicitar que, por obséquio, seja realizada uma breve síntese do documento anexo. Não é necessário incluir dados estatísticos complexos, apenas as conclusões gerais."
SAÍDA: Resuma o documento, incluindo apenas as conclusões gerais. Exclua dados estatísticos.
"""

# MODELO = "llama3.1:8b"
MODELO = 'gpt-oss:20b'
# MODELO = 'phi3:instruct'


class QuadroChat(ctk.CTkFrame):
    def __init__(self, master, estado: GerenciadorEstados, enviar_gemini, **kwargs):
        super().__init__(master, **kwargs)

        self.meu_estado = estado
        self.enviar_gemini = enviar_gemini

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=3)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=3)
        self.grid_columnconfigure(0, weight=1)

        # Caixa de texto mostrando o último input.
        ctk.CTkLabel(self, text="Prompt Resumido:").grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))
        self.caixa_texto = ctk.CTkTextbox(self, state="normal", font=("Arial", 14), )
        self.caixa_texto.insert('1.0', self.meu_estado.prompt_processado)
        self.caixa_texto.configure(state="disabled")
        self.caixa_texto.grid(row=1, column=0, sticky="nsew", padx=10, pady=(10, 5))

        ctk.CTkLabel(self, text="Prompt Original").grid(row=2, column=0, sticky="nsew", padx=10, pady=(10, 5))
        self.campo_entrada = ctk.CTkTextbox(self, font=("Arial", 14))
        self.campo_entrada.insert('1.0', self.meu_estado.prompt_original)
        self.campo_entrada.grid(row=3, column=0, sticky="ew", padx=10, pady=(5, 10))
        self.botao_enviar = ctk.CTkButton(self, width=50, text="Enviar prompt", command=self.ao_enviar_pressionado)
        self.botao_enviar.grid(row=4, column=0,sticky="nsew",padx=10,pady=(5, 10))
        self.campo_entrada.focus_set()


    def ao_enviar_pressionado(self):
        self.botao_enviar.configure(state="disabled")
        prompt = self.campo_entrada.get('0.0', 'end')
        threading.Thread(
            target=self.processar_localmente,
            args=(prompt,)
        ).start()

    def processar_localmente(self, prompt: str, ):

        self.meu_estado.prompt_original = prompt

        # Apresentando a informação para o usuário aguardar a IA responder
        self.caixa_texto.configure(state="normal")
        self.caixa_texto.insert(tkinter.END, "Processando o input, aguarde...")
        self.caixa_texto.see(tkinter.END)
        self.caixa_texto.configure(state="disabled")

        mensagens = [{"role": "system", "content": INSTRUCAO_SISTEMA}, {"role": "user", "content": prompt}]
        resposta = ollama.chat(model=MODELO, messages=mensagens, stream=True)

        for chunk in resposta:
            if "content" in chunk['message']:
                if 'Processando o input, aguarde...' in self.caixa_texto.get('0.0', 'end'):
                    # Apresentando a informação para o usuário aguardar a IA responder
                    self.caixa_texto.configure(state="normal")
                    self.caixa_texto.delete("1.0", "end")
                    self.caixa_texto.configure(state="disabled")
                texto_chunk = chunk["message"]["content"]
                self.master.after(0, self.atualiza_texto_resposta, texto_chunk)

        self.meu_estado.prompt_processado = self.caixa_texto.get('1.0', 'end')
        self.enviar_gemini()

    def atualiza_texto_resposta(self, novo_texto):
        self.caixa_texto.configure(state="normal")
        self.caixa_texto.insert(tkinter.END, novo_texto)
        self.caixa_texto.see(tkinter.END)
        self.caixa_texto.configure(state="disabled")

