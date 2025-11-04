from tkinter import ttk

from src.telas.tela_menu import TelaMenu


class TelaRespostas(ttk.Frame):
    def __init__(self, pai, controlador):
        super().__init__(pai)
    
        self.controlador = controlador
        self.menu = TelaMenu(self, controlador)
        self.menu.grid(row=0, column=1)

        ttk.Label(self, text="Tela de respostas",).grid(row=1)
