# Interactivity and running process.
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image

# Layouts
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

# Configuration
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')
Config.set('graphics', 'resizable', '1')


# Creating the objects
class FirstScreen(Screen):
    def search_image(self):
        pass
class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()
