#Baixando vídeos do youtube com interface gráfica
from pytube import YouTube #Biblioteca que permite o download dos vídeos
from PySimpleGUI import PySimpleGUI as sg #Interface gráfica



#Layout
sg.theme('Reddit') 
layout = [
    [sg.Text('Link'),sg.Input(key ='link')],
    [sg.Button('Download')]
]
#Janela
janela = sg.Window('Baixar vídeo',layout)
#Ler Eventos
while True:
    eventos,valores = janela.read()
    if eventos == sg.WINDOW_CLOSED: 
        break
    
    if eventos == 'Download':
        x = str(valores.values())
        YouTube(x).streams.get_highest_resolution().download()
        
        

 


