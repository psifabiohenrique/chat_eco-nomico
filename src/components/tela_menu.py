from tkinter import ttk


class TelaMenu(ttk.Frame):
    def __init__(self, pai, controlador):
        super().__init__(pai)
        self.controlador = controlador

        botao_inicial = ttk.Button(
            self,
            text="Tela inicial",
            command=lambda: self.controlador.mostrar_quadros("TelaInput"),
        )
        botao_inicial.grid(row=0, column=0)

        botao_respostas = ttk.Button(
            self,
            text="Tela Respostas",
            command=lambda: self.controlador.mostrar_quadros("TelaRespostas"),
        )
        botao_respostas.grid(row=0, column=1)

        botao_resultados = ttk.Button(
            self,
            text="Tela Resultados",
            command=lambda: self.controlador.mostrar_quadros('TelaResultados'),
        )
        botao_resultados.grid(row=0, column=2)
