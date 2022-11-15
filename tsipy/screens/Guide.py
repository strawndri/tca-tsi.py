from kivy.uix.screenmanager import Screen 
from kivy.uix.label import Label

class Guide(Screen):
    
    def on_pre_enter(self):

        colors= {
            'blue': (90/255, 113/255, 133/255, 1),
            'black': (.2, .2, .2, 1),
            'grey': (81/255, 81/255, 81/255, 1)
        } 

        grid_layout = self.ids.grid_layout
        config = []
        with open('docs/text/guide.txt', encoding='utf8') as file:
            for line in file:
                match (line[0]):
                    case '1':
                        config = [line[2:], 32, colors['blue'], True, 10]
                    case '2':
                        config = [line[2:], 24, colors['black'], True, 25]
                    case '3':
                        config = [line[2:], 18, colors['grey'], True, 20]
                    case '4':
                        config = [line[2:], 18, colors['black'], False, 100]
                      
                grid_layout.add_widget(Label(
                    text=config[0], 
                    font_size=config[1], 
                    color=config[2], 
                    bold=config[3], 
                    font_family='Arial',
                    halign='left',
                    size_hint_y= None,
                    height= config[4],
                    text_size= (900, 200)))



    


