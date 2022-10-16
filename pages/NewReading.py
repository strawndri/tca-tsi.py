from tkinter import Tk
from tkinter.filedialog import askopenfilename
from kivy.uix.screenmanager import Screen 

class NewReading(Screen):

    filename = ''
    
    def uploadFile(self):
        new_window = Tk()
        Tk.withdraw(new_window)
        self.filename = askopenfilename()