from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        box = BoxLayout()
        label = Label(text= 'Ola Mundo')
        label.fonte_size = 50
        
        box.add_widget(label)
        
        return box
        




MyApp().run()