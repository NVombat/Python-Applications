from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.app import App

from datetime import datetime as dt
from pathlib import Path
import json, glob
import random

#APP CODE
Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, uname, pwd):
        with open("/home/nvombat/Desktop/Python-Projects/FeelGood App/users.json") as jfile:
            users = json.load(jfile)
        if uname in users and users[uname]['password'] == pwd:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = 'Wrong Username or Password'

    def reset_pwd(self):
        self.manager.current = 'reset_screen'

class ResetScreen(Screen):
    def reset(self, uname, pwd):
        with open("/home/nvombat/Desktop/Python-Projects/FeelGood App/users.json") as jfile:
            users = json.load(jfile)
        users['uname'] = {'username': uname, 'password': pwd, 'created': dt.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("/home/nvombat/Desktop/Python-Projects/FeelGood App/users.json", 'w') as jfile:
            json.dump(users, jfile)

        self.manager.current = "login_screen"

class SignUpScreen(Screen):
    def add_user(self, uname, pwd):
        with open("/home/nvombat/Desktop/Python-Projects/FeelGood App/users.json") as jfile:
            users = json.load(jfile)
        users['uname'] = {'username': uname, 'password': pwd, 'created': dt.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("/home/nvombat/Desktop/Python-Projects/FeelGood App/users.json", 'w') as jfile:
            json.dump(users, jfile)

        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("/home/nvombat/Desktop/Python-Projects/FeelGood App/quotes/*.txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]

        if feel in available_feelings:
            with open(f"/home/nvombat/Desktop/Python-Projects/FeelGood App/quotes/{feel}.txt") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try Another Feeling!"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()