from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.core.window import Window

import screens.Home as Home
import screens.Guide as Guide
import screens.NewReading as NewReading

class WindowManager(ScreenManager):
    pass

Window.size = (1200, 600)

# centralização da janela na tela
Window.top = Window.size[1]/8
Window.left -= Window.size[0]/6

kv = Builder.load_file('main.kv')
class MainApp(App):
    def build(self):
        return kv

if __name__ == '__main__': 
    MainApp().run()