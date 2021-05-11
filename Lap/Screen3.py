import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, ReferenceListProperty , ObjectProperty
from kivy.uix.image import Image

import os

Window.size = (400 , 684)

dir_path = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(dir_path + '/Screen3.kv')

class Screen3(Widget):
    but = ObjectProperty(None)

class Button_AtomicStructure(Button):
    on = False
    def on_press(self):
        self.on = True
        self.sound = SoundLoader.load('Sound_Button.mp3')
        self.sound.play()
        print('AtomicStructure')

class Button_ElementPropoties(Button):
    on = False
    def on_press(self):
        self.on = True
        self.sound = SoundLoader.load('Sound_Button.mp3')
        self.sound.play()
        print('ElementPropoties')

class Button_RadioActive(Button):
    on = False
    def on_press(self):
        self.on = True
        self.sound = SoundLoader.load('Sound_Button.mp3')
        self.sound.play()
        print('RadioActive')

class Button_Back3_2(Button):
    on = False
    def on_press(self):
        self.on = True
        self.sound = SoundLoader.load('Sound_Button.mp3')
        self.sound.play()
        print('Back')


class MyApp(App):
    def build(self):
        return Screen3()

if __name__ == "__main__":
    MyApp().run()
        

