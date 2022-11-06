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
        self.ids.link.text =  ''

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

        match (type_of_file):
            case 'video':
                filename = askopenfilename()
                text =tr.read_video(filename)

                if text not in self.ids.result.text:
                    self.ids.result.text += text
                filename = f"data\\image_{0}.jpg"

            case 'image':
                filename = askopenfilename()
                text = tr.read_image(filename)
                if text not in self.ids.result.text:
                    self.ids.result.text += text
            case other:
                pass
        
        self.ids.imageToAnalyse.source = filename
