import PySimpleGUI as sg

layout = [  [sg.Text('Tsi.py')],
            [sg.Button('Acessar guia do tsi.py')], 
            [sg.Button('Realizar nova leitura')]]
            
window = sg.Window('Tsi.py', layout, size=(1200, 550))

while True:
    event, values = window.read()

    if (event == sg.WIN_CLOSED or event == 'Cancel'):
        break

    print(values)

window.close()
