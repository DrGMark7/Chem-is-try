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
Builder.load_file(dir_path + '/Screen2.kv')

class Screen2(Widget):
    but = ObjectProperty(None)

class Button_Grade10(Button):
    on = False
    def on_press(self):
        self.on = True
        print('on 10')
        self.sound = SoundLoader.load('Sound_Button.mp3')
        self.sound.play()

class Button_Grade11(Button):
    on = False
    def on_press(self):
        self.on = True
        print('on 11')
        self.sound = SoundLoader.load('Sound_Button.mp3')
        self.sound.play()

class Button_Grade12(Button):
    on = False
    def on_press(self):
        self.on = True
        print('on 12')
        self.sound = SoundLoader.load('Sound_Button.mp3')
        self.sound.play()

class Button_Back2_1(Button):
    on = False
    def on_press(self):
        self.on =True
        print('Back')
        self.sound = SoundLoader.load('Sound_Button.mp3')
        self.sound.play()

class MyApp(App):
    def build(self):
        return Screen2()

if __name__ == "__main__":
    MyApp().run()
    
