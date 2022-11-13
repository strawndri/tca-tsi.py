from kivy.uix.screenmanager import Screen 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Guide(Screen):
    def __init__(self, **kwargs):
        super(Guide, self).__init__(**kwargs)
        self.inside = BoxLayout()
        with open('docs/text/guide.txt', encoding='utf8') as file:
            for line in file:
                match (line[0]):
                    case '1':
                        self.inside.add_widget(Label(text=line))
                    case '2':
                        self.inside.add_widget(Label(text=line))
                    case '3':
                        self.inside.add_widget(Label(text=line))
                    case '4':
                        self.inside.add_widget(Label(text=line))
                    case '5':
                        self.inside.add_widget(Label(text=line))
                    case '6':
                        self.inside.add_widget(Label(text=line))
    


    


