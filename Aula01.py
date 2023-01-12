from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        #return Button(text='Clique para Confirmar')
        label = Label(text= 'Ola Mundo')
        label.fonte_size = 50
        return label
        




MyApp().run()