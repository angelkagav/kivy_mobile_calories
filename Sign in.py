from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRound
from kivymd.uix.button import MDRoundFlatButton

from kivy.lang import Builder

class Myapp(MDApp):
    def build(self):
        return Screen()

if __name__ == "__main__":
    Myapp().run()
# этот код нужно вставить в другой файл .kv
Builder.load_string("""
<MyScreen>:
    md_bg_color: [35/255,59/255,54/255,1]
    MDCard:
        orientation: 'vertical'
        size_hint: None, None
        size: 400, 500
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 15
        md_bg_color: [35/255, 49/255, 48/255, 1]
        padding: 20
        spacing: 30

        MDLabel:
            text: "SIGN-UP"
            font_style: "Button"
            font_size: 40
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 30

        MDTextFieldRound:
            hint_text: "username"
            size_hint_x: None
            icon_right: "account"
            width: 270
            font_size: 20
            pos_hint: {"center_x": .5}
            normal_color: [35/255, 49/255, 48/255, 1]
            color_active: [1, 1, 1, 1]

        MDTextFieldRound:
            hint_text: "user-id"
            size_hint_x: None
            icon_right: "account"
            width: 270
            font_size: 20
            pos_hint: {"center_x": .5}
            normal_color: [35/255, 49/255, 48/255, 1]
            color_active: [1, 1, 1, 1]

        MDTextFieldRound:
            hint_text: "password"
            password: True
            size_hint_x: None
            icon_right: "eye-off"
            width: 270
            font_size: 20
            pos_hint: {"center_x": .5}
            normal_color: [35/255, 49/255, 48/255, 1]
            color_active: [1, 1, 1, 1]

        MDTextFieldRound:
            hint_text: "confirm-password"
            size_hint_x: None
            password: True
            icon_right: "eye-off"
            width: 270
            font_size: 20
            pos_hint: {"center_x": .5}
            normal_color: [35/255, 49/255, 48/255, 1]
            color_active: [1, 1, 1, 1]

        MDTextFieldRound:
            hint_text: "mobile number"
            size_hint_x: None
            icon_right: "phone"
            width: 270
            font_size: 20
            pos_hint: {"center_x": .5}
            normal_color: [35/255, 49/255, 48/255, 1]
            color_active: [1, 1, 1, 1]

        MDRoundFlatButton:
            text: "SIGN-UP"
            font_size: 15
            pos_hint: {"center_x": .5}
            theme_text_color: "Custom"
            text_color: [0, 0, 0, 1]
""")

class MyScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        return MyScreen()

if __name__ == "__main__":
    MainApp().run()
