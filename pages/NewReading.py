from tkinter import Tk
from tkinter.filedialog import askopenfilename
from kivy.uix.screenmanager import Screen 

class NewReading(Screen):

    filename = './img/background.jpg'
    
    def uploadFile(self):
        new_window = Tk()
        Tk.withdraw(new_window)
        filename = askopenfilename()

        self.ids.imageToAnalyse.source = filename