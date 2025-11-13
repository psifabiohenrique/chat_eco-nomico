import customtkinter as ctk
from src.components.quadro_respostas import QuadroRespostas
from src.components.barra_lateral import BarraLateral
from src.components.quadro_chat import QuadroChat
from src.components.janela_graficos import JanelaGraficos
from src.services.ia_gemini import obter_resposta_gemini
from src.services.ia_local import obter_resposta_ollama
from src.services.limpeza_prompt import limpar_prompt


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
        
        self.CUSTO_ENERGIA_KWH_100_PALAVRAS = 0.14
        self.CUSTO_AGUA_ML_100_PALAVRAS = 0.500
        
        self.llm_ativo = "gemini"
        self.total_energia_gemini_kwh = 0.0
        self.total_agua_gemini_ml = 0.0
        self.total_energia_ollama_kwh = 0.0
        self.total_agua_ollama_ml = 0.0
        self.total_energia_padrao_kwh = 0.0
        self.total_agua_padrao_ml = 0.0
        
        self.janela_graficos_instancia = None

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
            valores_energia_consumo = [self.total_energia_gemini_kwh, self.total_energia_ollama_kwh]
            valores_agua_consumo = [self.total_agua_gemini_ml, self.total_agua_ollama_ml]
            valores_energia_economia = [self.total_energia_padrao_kwh, self.total_energia_gemini_kwh]
            valores_agua_economia = [self.total_agua_padrao_ml, self.total_agua_gemini_ml]
            
            self.janela_graficos_instancia.atualizar_dados_publico(
                valores_energia_consumo, valores_agua_consumo,
                valores_energia_economia, valores_agua_economia
            )

    def contar_palavras(self, texto: str) -> int:
        return len(texto.split())

    def ao_trocar_llm(self, nome_llm: str):
        if nome_llm == self.JANELAS.INICIO:
            self.quadro_resp =  QuadroChat(self, funcao_enviar_prompt=self.processar_prompt)
            self.quadro_resp.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10) 
        elif nome_llm == self.JANELAS.RESPOSTAS:
            self.quadro_resp = QuadroRespostas(self,)
            self.quadro_resp.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)
        elif nome_llm == self.JANELAS.GRAFICOS:
            self.quadro_resp = JanelaGraficos(self)
            self.quadro_resp.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)

    def processar_prompt(self, prompt_original: str):
        
        self.quadro_chat.campo_entrada.configure(state="disabled")
        self.update_idletasks() 

        prompt_limpo = limpar_prompt(prompt_original)
        if prompt_limpo != prompt_original.lower() and prompt_limpo:
             self.quadro_chat.adicionar_mensagem("Sistema (Otimizador)", f"Prompt enviado: {prompt_limpo}")
        
        palavras_originais_prompt = self.contar_palavras(prompt_original)
        palavras_limpas_prompt = self.contar_palavras(prompt_limpo)
        
        porcentagem_economia_prompt = 0.0
        if palavras_originais_prompt > 0 and palavras_originais_prompt > palavras_limpas_prompt:
            porcentagem_economia_prompt = (palavras_originais_prompt - palavras_limpas_prompt) / float(palavras_originais_prompt)
        
        resposta = ""
        nome_remetente = ""
        prompt_processado_com_sucesso = False 
        
        try:
            if self.llm_ativo == "gemini":
                nome_remetente = "Gemini"
                resposta = obter_resposta_gemini(prompt_limpo) 
                
                if not resposta.startswith("Erro:"):
                    palavras_resposta_real = self.contar_palavras(resposta)
                    custo_energia_otimizado = (palavras_resposta_real / 100.0) * self.CUSTO_ENERGIA_KWH_100_PALAVRAS
                    custo_agua_otimizado = (palavras_resposta_real / 100.0) * self.CUSTO_AGUA_ML_100_PALAVRAS
                    self.total_energia_gemini_kwh += custo_energia_otimizado
                    self.total_agua_gemini_ml += custo_agua_otimizado
                    
                    palavras_resposta_hipotetica = palavras_resposta_real
                    if porcentagem_economia_prompt > 0 and porcentagem_economia_prompt < 1.0:
                            palavras_resposta_hipotetica = palavras_resposta_real / (1.0 - porcentagem_economia_prompt)
                    
                    custo_energia_padrao = (palavras_resposta_hipotetica / 100.0) * self.CUSTO_ENERGIA_KWH_100_PALAVRAS
                    custo_agua_padrao = (palavras_resposta_hipotetica / 100.0) * self.CUSTO_AGUA_ML_100_PALAVRAS
                    self.total_energia_padrao_kwh += custo_energia_padrao
                    self.total_agua_padrao_ml += custo_agua_padrao
                    
                    prompt_processado_com_sucesso = True
            
            elif self.llm_ativo == "ollama":
                nome_remetente = "Ollama"
                resposta = obter_resposta_ollama(prompt_limpo) 
                if not resposta.startswith("Erro:"):
                    prompt_processado_com_sucesso = True
                
        except Exception as e:
            resposta = f"Erro ao contatar a API: {e}"
            nome_remetente = "Erro"
        
        self.quadro_chat.adicionar_mensagem(nome_remetente, resposta)
        
        if prompt_processado_com_sucesso:
            self.atualizar_todos_graficos()
        
        self.quadro_chat.campo_entrada.configure(state="normal")

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