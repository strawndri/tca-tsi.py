from fpdf import FPDF
from pathlib import Path

from tkinter import Tk
from tkinter.filedialog import askopenfilename

import os

from kivy.uix.screenmanager import Screen 

import pytesseract as pt
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
import cv2

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

    def read_image(self, image_file):
        image = cv2.imread(image_file)
        text = pt.image_to_string(image)
        
        if text not in self.ids.result.text:
            self.ids.result.text += text

    def check_radio_button(self):
        if self.ids.image.active:
            return 'image'
        elif self.ids.video.active:
            return 'video'
        else:
            return 'nothing here...'  

    def uploadFile(self):

        type_of_file = self.check_radio_button()

        if type_of_file == 'video':

            filename = askopenfilename()
            video = cv2.VideoCapture(filename)
            success, image = video.read()
            i = 0
            success = True
            images = []

            while success:
                cv2.imwrite("data\\image_%d.jpg" % i, image)
                if (i > 0):
                    self.compareHistograms(i)
                i += 1
                success, image = video.read()
            
            for i in images:
                self.read_image(f"data\\image_{i}.jpg")
            filename = f"data\\image_{0}.jpg"

        elif type_of_file == 'image':
            filename = askopenfilename()
            self.read_image(filename)
        else:
            pass
        
        self.ids.imageToAnalyse.source = filename

    def createHistogram(self, image):
        img = cv2.imread(image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        hist = cv2.calcHist([img], [0, 1], None, [8, 8], [0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()

        return hist

    def compareHistograms(self, position):
        hist2 = self.createHistogram(f"data\\image_{position}.jpg")

        for i in range(0, position):
            
            try:
                hist1 = self.createHistogram(f"data\\image_{i}.jpg")
                result = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)

                if (result <= 3.0e-03):
                    os.remove(f"data\\image_{position}.jpg")
                    break
            except:
                i += 1
            
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

