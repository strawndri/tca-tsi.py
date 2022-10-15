from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.core.window import Window

import pages.Home as Home
import pages.Guide as Guide
import pages.NewReading as NewReading

class WindowManager(ScreenManager):
    pass

Window.size = (1200, 600)
kv = Builder.load_file('main.kv')

class MainApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MainApp().run()