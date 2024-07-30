from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

class MyCanvas(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 0, 0)  # Cor vermelha
            Line(points=(touch.x, touch.y))

class CanvasApp(App):
    def build(self):
        return MyCanvas()

if __name__ == '__main__':
    CanvasApp().run()
