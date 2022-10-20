from tkinter import Tk
from fpdf import FPDF
from pathlib import Path
from tkinter.filedialog import askopenfilename
from kivy.uix.screenmanager import Screen 

new_window = Tk()
Tk.withdraw(new_window)

class NewReading(Screen):

    checks = []
    filename = './img/img-icon.png'

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

    def uploadFile(self):
        filename = askopenfilename()

        self.ids.imageToAnalyse.source = filename

    def getLink(self):
        path = self.ids.link.text
        self.ids.imageToAnalyse.source = path
        self.ids.link.text =  ''
        
    def copy_text(self):
        new_window.clipboard_clear()
        new_window.clipboard_append(self.ids.result.text)
        new_window.update()
        new_window.destroy()

    def string_to_pdf(self):
        pdf = FPDF()
        download_path = str(Path.home()/"Downloads")
        path = download_path + '/test.pdf'
        pdf.add_page()
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(40, 10, self.ids.result.text)
        pdf.output(path, 'F')

