from tkinter import Tk
from tkinter.filedialog import askopenfilename
from kivy.uix.screenmanager import Screen 

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
        new_window = Tk()
        Tk.withdraw(new_window)
        filename = askopenfilename()

        self.ids.imageToAnalyse.source = filename