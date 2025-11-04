from tkinter import ttk

from src.telas.tela_menu import TelaMenu

class TelaResultados(ttk.Frame):
    def __init__(self, pai, controlador):
        super().__init__(pai)

        self.controlador = controlador

        self.menu = TelaMenu(self, self.controlador)
        self.menu.grid(row=0, column=1)