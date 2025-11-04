from tkinter import ttk, Text


class TelaInput(ttk.Frame):
    def __init__(self, pai, controlador):
        super().__init__(pai)
        
        self.controlador = controlador

        titulo = ttk.Label(self, text="Tela de input", font=("Arial", 16))
        titulo.grid(row=0, column=1)

        etiqueta_input = ttk.Label(self, text="Adicione o seu input aqui:")
        etiqueta_input.grid(row=1, column=1)


        quadro_input_text = ttk.Frame(self)
        quadro_input_text.grid(row=2, column=1)
        self.texto_input = Text(quadro_input_text, height=15, width=60, takefocus=True)
        self.texto_input.grid(row=1, column=0)
        rolagem_texto = ttk.Scrollbar(quadro_input_text, command=self.texto_input.yview)
        rolagem_texto.grid(row=1, column=1)
        self.texto_input.configure(yscrollcommand=rolagem_texto.set)
        

        botao_processar = ttk.Button(self, text='Processar input', command=self.processar_input)
        botao_processar.grid(row=3, column=1)

    def processar_input(self):
        texto = self.texto_input.get('1.0', 'end-1c')
        print('Input Text: ' + texto)