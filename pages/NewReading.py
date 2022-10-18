from tkinter import Tk
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

    def copy_text(self):
        new_window.clipboard_clear()
        new_window.clipboard_append(self.ids.result.text)
        new_window.update()
        new_window.destroy()

