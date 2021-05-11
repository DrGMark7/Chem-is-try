import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.base import runTouchApp

from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager , Screen , FadeTransition

from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.graphics import Rectangle
from kivy.properties import NumericProperty, ReferenceListProperty , ObjectProperty , ListProperty , StringProperty

import Screen2
import Screen3
import Screen4
import ScreenAtomicSize

from AtomicSize import AtomicRadius_Comparison
from IE_EN import IE_EN_Comparison

import os

Window.size = (400 , 684)

dir_path = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(dir_path + '/Screen1.kv')

class Screen1(Screen):
    but = ObjectProperty(None)

class Screen2(Screen):
    but = ObjectProperty(None)    

class Screen3(Screen):
    but = ObjectProperty(None)    

class Screen4(Screen):
    but = ObjectProperty(None)    

class ScreenAtomicSize(Screen):
    but = ObjectProperty(None)
    def photo(self,dt):       
       self.ids.ElementPic_I.source = 'Button_Back.png'
   
    def ele_import(self, Ele_I , Ele_II ,**kwargs):
        print(Ele_I)
        print(Ele_II) 

        List_Pic = AtomicRadius_Comparison(Ele_I , Ele_II)
        A = List_Pic[0]
        B = List_Pic[1]
        C = List_Pic[2]

        with self.canvas:
            self.ElementPic_I = Rectangle(source='{}'.format(A), pos=(0, 200), size=(150,150))
            self.ElementPic_II = Rectangle(source='{}'.format(B), pos=(200, 200), size=(150,150))
            self.Arrow_Pic = Rectangle(source='{}'.format(C), pos=(120, 220), size=(127.5,100))
        print(A,B,C)  
                  
    # def IE_EN(self, Ele_IE_I , Ele_IE_II ):
    #     print(Ele_IE_I)
    #     print(Ele_IE_II)s

class Button_Start(Button):
    on = False
    def on_press(self):
        self.on = True
        self.sound = SoundLoader.load('Sound_Button.mp3')
        self.sound.play()
        print('Start')        

class Mascot1(Widget):
    pass

class WindowManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1()), sm.add_widget(Screen2())
        sm.add_widget(Screen2()), sm.add_widget(Screen3())
        sm.add_widget(Screen3()), sm.add_widget(Screen4())
        sm.add_widget(Screen4()), sm.add_widget(ScreenAtomicSize())             
        return sm

if __name__ == '__main__':
    MyApp().run()