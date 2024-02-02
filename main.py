from kivy.app import App
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass


class TestApp(App):
    def build(self):
        return MainWidget()
    pass

TestApp().run()