from fpdf import FPDF
from pathlib import Path

from tkinter import Tk
from tkinter.filedialog import askopenfilename

from kivy.uix.screenmanager import Screen 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import text_recognize as tr

new_window = Tk()
Tk.withdraw(new_window)

class NewReading(Screen):

    checks = []
    path = 'docs/img/img-icon.png'
    video_format = ['.mp4', '.gif', '.mkv', '.webm', '.avi', '.mov']
    image_format = ['.jpg', '.jpeg', '.png']
    type_of_file = ''
    is_link = False
    is_the_correct_format = False

    # verifica se o arquivo selecionado foi corretamente escolhido (formato)
    def check_file(self, filename, format):

        if (format == 'video'):
            list_format = self.video_format
        elif (format == 'image'):
            list_format = self.image_format

        if (format == 'video' and self.is_link):
            self.show_popup('invalid')
        elif (format == None):
            self.show_popup('empty')
        else:
            for i in list_format:
                if filename.endswith(i):
                    self.is_the_correct_format = True
                    self.show_popup('success')
                    break
            if (self.is_the_correct_format == False):
                self.show_popup('error')
    
    # verifica o valor selecionado pelo usuário
    def check_radio_button(self):
        if self.ids.image.active:
            return 'image'
        elif self.ids.video.active:
            return 'video'
        else:
            return None

    # realiza uma cópia do do texto p/ a área de transfência
    def copy_text(self):
        new_window.clipboard_clear()
        new_window.clipboard_append(self.ids.result.text)
        new_window.update()
        new_window.destroy()
        self.show_popup('copy')

    # recebe o caminho adicionado pelo usuário no input
    def getLink(self):
        self.path = self.ids.link.text
        self.type_of_file = self.check_radio_button()
        self.is_link = True
        self.ids.link.text = ''
        self.check_file(self.path, self.type_of_file)

    # recebe o valor conforme o click do usuário nos radiobuttons
    def radio_button_click(self, instance, value, topping):
        if value == True:
            NewReading.checks.append(topping)
            tops = ''
            for i in NewReading.checks:
                tops = f'{tops} {i}'
        else:
            NewReading.checks.remove(topping)
            tops = ''
            for i in NewReading.checks:
                tops = f'{tops} {i}'

    # coleta o texto que foi processado e o transforma em um arquivo de formato .pdf
    def string_to_pdf(self):
        pdf = FPDF()
        download_path = str(Path.home()/"Downloads")
        path = download_path + '/novo_arquivo.pdf'
        pdf.add_page()
        pdf.set_font('Arial', '', 12)
        text = self.ids.result.text
        text = text.encode('latin-1', 'ignore').decode('latin-1')
        pdf.multi_cell(0, 5, txt = text)
        pdf.output(path, 'F')
        self.show_popup('download') # mostra o popup de que o download foi concluído

    # apresenta o resultado em tela
    def show_result(self):
        if (self.is_the_correct_format):
            if (self.type_of_file == 'video'):
                print(self.path)
                text = tr.read_video(self.path)
                self.ids.imageToAnalyse.source = 'docs/img/img-icon.png'
            else:
                text = tr.read_image(self.path, self.is_link)
                self.ids.imageToAnalyse.source = self.path
                self.is_link = False

            if text not in self.ids.result.text:
                self.ids.result.text = text
        else:
            self.show_popup('error')

    # apresenta avisos conforme a ação do usuário
    def show_popup(self, type):
        box = BoxLayout(orientation = 'vertical', padding = (48))
        match type:
            case 'error':
                title = 'Erro inesperado'
                txt = 'Não foi possível dar continuidade à leitura, tente novamente!' 
            case 'success':
                title = 'Arquivo recebido'
                txt = 'O arquivo foi recebido com sucesso. Clique em "Realizar Leitura" e aguarde um instante até que o processamento seja finalizado.'
            case 'invalid':
                title = 'Formato inválido'
                txt = 'Tsi.py ainda não realiza leitura de vídeos coletados por url. Você será avisado quando a funcionalidade for inserida.'
            case 'empty':
                title = 'Erro no formato do arquivo'
                txt = 'Selecione "Imagem" ou "Vídeo" para continuar a leitura.'
            case 'download':
                title = 'Download concluído'
                txt = 'O download do texto foi finalizado. Verifique a pasta "Downloads" do seu dispositivo.'
            case 'copy':
                title = 'Texto copiado'
                txt = 'O texto lido foi copiado, com sucesso, para a área de transferência. Pressione o botão direito do mouse e clique em colar ou pressione CTRL+V para apresentar o seu texto.'

        box.add_widget(Label(
            text = txt, 
            font_family = 'Arial', 
            font_size = 18, 
            text_size = (400, 200),
            halign = 'center',
            valign = 'center',
            color = (249/255, 249/255, 249/255, 1)))

        popup = Popup(
            title = title, 
            content = box, 
            auto_dismiss = True,
            title_size = 18,
            title_align = 'center',
            size_hint = (None, None),
            size = (600, 400),
            background = 'docs/img/background.png')

        box.add_widget(Button(
            text = 'Fechar', 
            on_press = popup.dismiss,
            font_size = 24,
            color = (.2, .2, .2, 1),
            background_color = (178/255, 192/255, 205/255, 1),
            background_normal = '',
            size = (500, 72),
            size_hint = (None, None)
            ))

        popup.open()

    # faz upload do arquivo
    def upload_file(self):
        self.type_of_file = self.check_radio_button()
        self.path = askopenfilename()
        self.check_file(self.path, self.type_of_file)