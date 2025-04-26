# Interactivity and running process.
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.image import Image

# Layouts
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

# Configuration
Config.set('graphics', 'width', '1080')
Config.set('graphics', 'height', '720')
Config.set('graphics', 'resizable', '1')


# Creating the objects
class MainApp(App):

    def build(self):
        box1 = BoxLayout(orientation='vertical')
        label1 = Label(text="Hello Kivy World!", font_size=50)
        label2 = Label(text="Created a box layout.", font_size=30, color=(1, 0, 0, 1))
        button1 = Button(text='A kivy Button', font_size=40, color=[1, 1, 0, 1])
        box1.add_widget(label1)
        box1.add_widget(label2)
        box1.add_widget(button1)
        return box1
