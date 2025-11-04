from tkinter import ttk
from ttkthemes import ThemedTk

from src.telas.tela_input import TelaInput
from src.telas.tela_respostas import TelaRespostas
from src.telas.tela_resultados import TelaResultados


class App(ThemedTk):
    def __init__(self):
        super().__init__()
        self.title('Chat eco-nomico')
        self.geometry("800x600")
        self.set_theme('ubuntu')
        conteiner = ttk.Frame(self)
        conteiner.pack(fill='both', expand=True)

        self.quadros = {}

        for Q in (TelaInput, TelaRespostas, TelaResultados):
            nome_quadro = Q.__name__
            quadro = Q(pai=conteiner, controlador=self)
            self.quadros[nome_quadro] = quadro
            quadro.grid(row=1, column=1, sticky="nsew")
        
        self.mostrar_quadros("TelaInput")

    def mostrar_quadros(self, pagina):
        quadro = self.quadros[pagina]
        quadro.tkraise()
        


if __name__ == '__main__':
    app = App()
    app.mainloop()