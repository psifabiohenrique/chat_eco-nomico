import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Define a classe GraficosEconomia 
class GraficosEconomia(ctk.CTkFrame):
    """Classe responsável pelos gráficos que serão exibidos no componente que exibe os gráficos de estatística"""
    def __init__(self, master, **kwargs):
        """Construtor da classe
        
        Params:
            master: App
        """
        super().__init__(master, **kwargs)
        #Define-se que há apenas 2 linhas dentro desse Frame e weight=1 permite expansão proporcional da Tela
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Cor de fundo do gráfico
        plt.style.use('dark_background')
        #Cria a figura do gráfico de energia
        self.figura_energia = Figure(figsize=(5, 2.5), dpi=100)
        self.ax_energia = self.figura_energia.add_subplot(111)
        #Cria um frame somente para a energia calculada
        self.canvas_energia_frame = ctk.CTkFrame(self, fg_color="transparent")
        #Posição linha e coluna 0,0 o grade 
        self.canvas_energia_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))
        self.canvas_energia = FigureCanvasTkAgg(self.figura_energia, master=self.canvas_energia_frame)
        self.canvas_energia.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)
       
        #Cria a figura do gráfico de água
        self.figura_agua = Figure(figsize=(5, 2.5), dpi=100)
        self.ax_agua = self.figura_agua.add_subplot(111)
        #Cria um frame somente para a água calculada
        self.canvas_agua_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.canvas_agua_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))
        self.canvas_agua = FigureCanvasTkAgg(self.figura_agua, master=self.canvas_agua_frame)
        self.canvas_agua.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)
        #Ao iniciar o sistema, o gráfico é desenhado com valoress [0,0]
        self.atualizar_dados(valores_energia=[0, 0], valores_agua=[0, 0])

    def configurar_estilo_eixo(self, ax, titulo: str, unidade_y: str):
        """Função que configura o estilo do eixo dos gráficos
        
        Params:
            ax: matplotlib.figure.Figure
            titulo: string
            unidade_y: string
        Return:
            None
        """
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='x', colors='white', labelsize=9)
        ax.tick_params(axis='y', colors='white', labelsize=9)
        ax.set_title(titulo, color='white', fontsize=12)
        ax.set_ylabel(unidade_y, color='white', fontsize=10)

    def desenhar_grafico(self, ax, canvas, titulo: str, unidade_y: str, valores: list, cor_otimizado: str):
        """Função que desenha os gráficos na tela.
        
        Params:
            ax: matplotlib.figure.Figure
            canvas: FigureCanvasTkAgg
            titulo: string
            unidade_y: string
            valores: list[float]
            cor_otimizado: str
        Return:
            None"""
        ax.clear() 
        categorias = ['Padrão', 'Otimizado']
        cores = ['#FF6347', cor_otimizado]
        barras = ax.bar(categorias, valores, color=cores)
        self.configurar_estilo_eixo(ax, titulo, unidade_y)
        
        for barra in barras:
            altura = barra.get_height()
            ax.text(barra.get_x() + barra.get_width()/2., altura,
                     f'{altura:.4f}', ha='center', va='bottom', color='white', fontsize=9)

        limite_max = max(valores) * 1.15 if max(valores) > 0 else 0.1
        ax.set_ylim(bottom=0, top=limite_max)
        
        self.figura_energia.tight_layout()
        self.figura_agua.tight_layout()
        canvas.draw()
    
    def atualizar_dados(self, valores_energia: list, valores_agua: list):
        """Redezenha os gráficos na tela.
        
        Params:
            valores_energia: list[float]
            valores_agua: list[float]
        Return:
            None"""
        self.desenhar_grafico(self.ax_energia, self.canvas_energia, 
                              "Consumo Total de Energia (kWh)", "kWh", 
                              valores_energia, '#FFC107')
        
        self.desenhar_grafico(self.ax_agua, self.canvas_agua, 
                              "Consumo Total de Água (mL)", "mL", 
                              valores_agua, '#00A8A8')