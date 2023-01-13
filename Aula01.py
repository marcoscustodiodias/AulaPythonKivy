from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        box = BoxLayout()
        label = Label(text= 'Ola Mundo')
        label.font_size = 50
        btn = Button(text='Button')
        btn.font_size = 50
        
        box.add_widget(label)
        box.add_widget(btn)
        return box


MyApp().run()