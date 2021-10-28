#Baixando vídeos do youtube com interface gráfica
from pytube import YouTube #Biblioteca que permite o download dos vídeos
from PySimpleGUI import PySimpleGUI as sg #Interface gráfica



#Layout
sg.theme('Reddit') 
layout = [ #o que terá na janela, local de texto para input, botão de download
    [sg.Text('Link'),sg.Input(key ='link')],        
    [sg.Button('Download')]
]
#Janela
janela = sg.Window('Baixar vídeo',layout) #Título da janela e o layout
#Ler Eventos
while True:
    eventos,valores = janela.read()
    if eventos == sg.WINDOW_CLOSED: #Se clicar no botão de fechar, sai da GUI
        break
    
    if eventos == 'Download':
        x = str(valores.values()) #como se trata de um dicionário, devo mostrar os valores do mesmo
        YouTube(x).streams.get_highest_resolution().download()
        
        

 


