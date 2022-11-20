from fpdf import FPDF
from pathlib import Path

from tkinter import Tk
from tkinter.filedialog import askopenfilename

from kivy.uix.screenmanager import Screen 

import text_recognize as tr

new_window = Tk()
Tk.withdraw(new_window)

class NewReading(Screen):

    checks = []
    path = 'docs/img/img-icon.png'
    video_format = ['.mp4', '.gif', '.mkv', '.webm', '.avi', '.mov']
    image_format = ['.jpg', '.jpeg', '.png']
    is_link = False
    is_the_correct_format = False

    def checkbox_click(self, instance, value, topping):
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

    def check_radio_button(self):
        if self.ids.image.active:
            return 'image'
        elif self.ids.video.active:
            return 'video'
        else:
            return 'nothing here...'  

    def copy_text(self):
        new_window.clipboard_clear()
        new_window.clipboard_append(self.ids.result.text)
        new_window.update()
        new_window.destroy()

    def getLink(self):
        self.path = self.ids.link.text
        type_of_file = self.check_radio_button()
        self.check_file(self.path, type_of_file)
        self.is_link = True

    def string_to_pdf(self):
        pdf = FPDF()
        download_path = str(Path.home()/"Downloads")
        path = download_path + '/test.pdf'
        pdf.add_page()
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(40, 10, self.ids.result.text)
        pdf.output(path, 'F')

    def upload_file(self):
        type_of_file = self.check_radio_button()
        self.path = askopenfilename()
        self.check_file(self.path, type_of_file)

    def check_file(self, filename, format):
        if (format == 'video'):
            list_format = self.video_format
        else:
            list_format = self.image_format

        for i in list_format:
            if filename.endswith(i):
                self.is_the_correct_format = True
                self.show_popup('success')
                break
        if (self.is_the_correct_format == False):
            self.show_popup('error')

    def show_result(self):
        if (self.is_the_correct_format):
            if (format == 'video'):
                text = tr.read_video(self.path)
                self.ids.imageToAnalyse.source = f"data\image_{0}.jpg"
            else:
                text = tr.read_image(self.path, self.is_link)
                self.ids.imageToAnalyse.source = self.path

            if text not in self.ids.result.text:
                self.ids.result.text = text
        else:
            self.show_popup('error')

    def show_popup(self, type):
        match type:
            case 'error':
                print('Erro!!!!!!!!!!!!!!!!!!!!!!!!!!')
            case 'success':
                print('Arquivo recebido com sucesso!')
