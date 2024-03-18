#Это код начальной страницы, где пользователь должен ввести свои параметры (рост, вес, пол и тд)


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput


class MainPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")
        next_button = Button(text="Дальше", on_press=self.go_to_next_page)
        layout.add_widget(Label(text="Привет!"))
        layout.add_widget(next_button)
        self.add_widget(layout)

    def go_to_next_page(self, instance):
        app = App.get_running_app()
        app.root.current = "HeightPage"


class HeightPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")
        height_label = Label(text="Введите свой рост:")
        self.height_input = TextInput(font_size=40, multiline=False, input_type="number")
        self.next_button = Button(text="Далее", on_press=self.go_to_age_page)

        layout.add_widget(height_label)
        layout.add_widget(self.height_input)
        layout.add_widget(self.next_button)

        self.add_widget(layout)

    def go_to_age_page(self, instance):
        app = App.get_running_app()
        app.root.current = "AgePage"
        app.root.get_screen("AgePage").set_height(self.height_input.text)


class AgePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")
        age_label = Label(text="Введите ваш возраст:")
        self.age_input = TextInput(font_size=40, multiline=False, input_type="number")
        next_button = Button(text="Далее", on_press=self.go_to_gender_page)

        layout.add_widget(age_label)
        layout.add_widget(self.age_input)
        layout.add_widget(next_button)

        self.add_widget(layout)

    def set_height(self, height):
        self.height = height

    def go_to_gender_page(self, instance):
        app = App.get_running_app()
        app.root.current = "GenderPage"
        app.root.get_screen("GenderPage").set_height(self.height)
        app.root.get_screen("GenderPage").set_age(self.age_input.text)


class GenderPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")
        gender_label = Label(text="Выберите пол:")
        male_button = Button(text="Мужской", on_press=self.select_male)
        female_button = Button(text="Женский", on_press=self.select_female)

        layout.add_widget(gender_label)
        layout.add_widget(male_button)
        layout.add_widget(female_button)

        self.add_widget(layout)

    def set_height(self, height):
        self.height = height

    def set_age(self, age):
        self.age = age

    def select_male(self, instance):
        app = App.get_running_app()
        app.root.current = "WeightPage"
        app.root.get_screen("WeightPage").set_height(self.height)
        app.root.get_screen("WeightPage").set_age(self.age)
        app.root.get_screen("WeightPage").set_gender("Мужской")

    def select_female(self, instance):
        app = App.get_running_app()
        app.root.current = "WeightPage"
        app.root.get_screen("WeightPage").set_height(self.height)
        app.root.get_screen("WeightPage").set_age(self.age)
        app.root.get_screen("WeightPage").set_gender("Женский")

class WeightPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")
        weight_label = Label(text="Введите ваш вес:")
        self.weight_input = TextInput(font_size=40, multiline=False, input_type="number")
        calculate_button = Button(text="Рассчитать", on_press=self.calculate_calories)

        layout.add_widget(weight_label)
        layout.add_widget(self.weight_input)
        layout.add_widget(calculate_button)

        self.add_widget(layout)

    def set_height(self, height):
        self.height = height

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def calculate_calories(self, instance):
        height = int(self.height)
        age = int(self.age)
        weight = int(self.weight_input.text)

        if self.gender == "Мужской":
            bmr = 66.5 + 13.75 * weight + 5.003 * height - 6.775 * age
        else:
            bmr = 655.1 + 9.563 * weight + 1.85 * height - 4.676 * age

        daily_calories = bmr * 1.2

        print("Рост:", height)
        print("Возраст:", age)
        print("Пол:", self.gender)
        print("Вес:", weight)
        print("BMR (базовый обмен веществ):", bmr)
        print("Суточная норма калорий:", daily_calories)
        # Вы можете добавить свои дополнительные действия с BMR и daily_calories


class LoginPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")
        login_button = Button(text="Login", on_press=self.go_to_main_page)

        layout.add_widget(Label(text="Please login"))
        layout.add_widget(login_button)

        self.add_widget(layout)

    def go_to_main_page(self, instance):
        app = App.get_running_app()
        app.root.current = "MainPage"


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        login_page = LoginPage(name="LoginPage")
        main_page = MainPage(name="MainPage")
        height_page = HeightPage(name="HeightPage")
        age_page = AgePage(name="AgePage")
        gender_page = GenderPage(name="GenderPage")
        weight_page = WeightPage(name="WeightPage")
        sm.add_widget(login_page)
        sm.add_widget(main_page)
        sm.add_widget(height_page)
        sm.add_widget(age_page)
        sm.add_widget(gender_page)
        sm.add_widget(weight_page)

        return sm


if __name__ == "__main__":
    MyApp().run()
