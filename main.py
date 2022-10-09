from PySimpleGUI import (
    Window, Button, Text, Image, Input, WIN_CLOSED,
    Column, VSeparator,
    )

def set_button_style(text='', key='', color='#FC9DBD', size=(24, 1)):
    return Button(text, key=key, button_color=color, size=size)

def window_home():
    layout = [
        [Button('Acessar guia do tsi.py', key='-GUIDE-', button_color='#FC9DBD')],
        [Button('Realizar nova leitura', key='-READING-', button_color='#FC9DBD')]]
    return Window('Home', layout=layout, size=(1000, 500), font=('Arial 16 bold'), background_color='#758EAC')


def window_guide():
    layout = [
        [Button('Home', key='-HOME-', button_color='#FC9DBD')]]
    return Window('Guia do Tsi.py', layout=layout, size=(1000, 500), background_color='#F9F9F9')


def window_reading():
    layout_left = [
        [Button('Home', key='-HOME-', button_color='#FC9DBD'), Button('Acessar guia do tsi.py', key='-GUIDE-', button_color='#FC9DBD')],
        [Text('Nova Leitura')], 
        [Text('Selecione o formato do arquivo: ')],
        [set_button_style(text='Imagem', key='-IMAGE-'), set_button_style(text='Vídeo', key='-VIDEO-')],
        [Text('Escolha a ação:')], 
        [set_button_style(text='Upload', key='-UPLOAD-'), set_button_style(text='Link', key='-LINK-')],
        [set_button_style(text='Realizar leitura', key='-DO_READING-')],
        [set_button_style(text='Copiar texto', key='-COPY-'), set_button_style(text='Download', key='-DOWNLOAD-')],
    ]

    layout_right = [
        [Image()], [Text('bla bla bla')]
    ]

    layout = [[Column(layout_left), VSeparator(), Column(layout_right)]]
    return Window('Nova Leitura', layout=layout, size=(1000, 500), background_color='#F9F9F9', font=('Arial 12'))


window = window_home()

while True:
    event, values = window.read()

    if (event == WIN_CLOSED):
        break

    if (event == '-HOME-') or (event == '-GUIDE-') or (event == '-READING-'):
        window.close()
        if (event == '-HOME-'):
            window = window_home()
        elif (event == '-GUIDE-'):
            window = window_guide()
        elif (event == '-READING-'):
            window = window_reading()

window.close()
