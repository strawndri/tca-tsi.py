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
    filename = 'docs/img/img-icon.png'
    video_format = ['.mp4', '.gif', '.mkv', '.webm', '.avi', '.mov']
    image_format = ['.jpg', '.jpeg', '.png']

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
        path = self.ids.link.text
        self.ids.imageToAnalyse.source = path

        type_of_file = self.check_radio_button()

        match (type_of_file):
            case 'video':
                pass
            case 'image':
                text = tr.read_image(path, True)
                if text not in self.ids.result.text:
                    self.ids.result.text = text
            case other:
                pass

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
        try:
            filename = askopenfilename()
        except:
            self.show_popup_error()
        else:
            match (type_of_file):
                case 'video':
                    if (self.check_file(filename, self.video_format)):
                        text = tr.read_video(filename)
                        self.show_result(text)
                        self.ids.imageToAnalyse.source = f"data\image_{0}.jpg"
                    else:
                        self.show_popup_error()
                case 'image':
                    if (self.check_file(filename, self.image_format)):
                        text = tr.read_image(filename)
                        self.show_result(text)
                        self.ids.imageToAnalyse.source = filename
                    else:
                        self.show_popup_error()
            

    def check_file(self, filename, list_format):
        is_the_correct_format = False
        for i in list_format:
            if filename.endswith(i):
                is_the_correct_format = True
                break
        return is_the_correct_format

    def show_result(self, text):
        if text not in self.ids.result.text:
            self.ids.result.text = text

    def show_popup_error(self):
        print('Erro!!!!!!!!!!!!!!!!!!!!!!!!!!')
