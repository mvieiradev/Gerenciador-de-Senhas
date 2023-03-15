import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):

        # Layout

        sg.theme('Black')
        layout = [
            [sg.text('Site/Software', size=(10,1)),
            sg.input(key='site', size=(20,1))],
            [sg.Text('E-mail/Usuario', size=(10,1)), 
            sg,input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres',sg.Combo(valuse=list(
                range(30)),ke='total_chars', default_values=1, size=(3, 1)))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
        # Declarar janela
        self.janela = sg.Window('password Generator', layout)
      
    def Inicias(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.gerar_senha
    def salver_senhas(self):
        pass 
gen = PassGen()
gen.iniciar()