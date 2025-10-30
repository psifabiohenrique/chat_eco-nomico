from tkinter import ttk
from ttkthemes import ThemedTk

from src.telas.tela_input import TelaInput


class App(ThemedTk):
    def __init__(self):
        super().__init__()
        self.title('Chat eco-nomico')
        self.geometry("800x600")
        self.set_theme('ubuntu')
        conteiner = ttk.Frame(self)
        conteiner.pack(fill='both', expand=True)

        self.quadros = {}

        for Q in (TelaInput,):
            quadro = Q(pai=conteiner, controlador=self)
            self.quadros[Q] = quadro
            quadro.grid(row=0, column=0, sticky="nsew")
        
        self.mostrar_quadros(TelaInput)

    def mostrar_quadros(self, pagina):
        quadro = self.quadros[pagina]
        quadro.tkraise()
        


if __name__ == '__main__':
    app = App()
    app.mainloop()