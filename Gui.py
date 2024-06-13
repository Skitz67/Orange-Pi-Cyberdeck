from kivy.app import App
# Widgets
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button

# Layouts
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.gridlayout import GridLayout



functions = ["WiFi Functions", "NFC Functions", "IR Function"]

ROWS = len(functions) + 1

COLS = 1

class GridApp(App):
    def build(self):
        root = GridLayout(rows=ROWS, cols=COLS)
        root.add_widget(Label(text = "Functions"))
        for i in range(len(functions)):
            root.add_widget(Button(text = functions[i]))
        return root

GridApp().run()

