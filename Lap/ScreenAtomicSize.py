import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import NumericProperty, ReferenceListProperty , ObjectProperty
from kivy.uix.image import Image

import os

Window.size = (400 , 684)

dir_path = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(dir_path + '/ScreenAtomicSize.kv')

class ScreenAtomicSize(Widget):
    but = ObjectProperty(None)    

class Button_RunAtom(Button):
    on = False
    def on_press(self):
        self.on = True
        self.sound = SoundLoader.load('Sound_Button.mp3')
        self.sound.play()
        print('Button_Run')

class Button_BackAS_4(Button):
    on = False
    def on_press(self):
        self.on =True
        print('Back')
        self.sound = SoundLoader.load('Sound_Button.mp3')
        self.sound.play()

class Mascot2(Widget):
    pass
    

class MyApp(App):
    def build(self):
        return ScreenAtomicSize()

if __name__ == "__main__":
    MyApp().run()