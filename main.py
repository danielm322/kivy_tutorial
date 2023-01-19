from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    counter = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("Hello!")
    # Slider value can be taken care of by id of slide in kv file
    # slider_value_txt = StringProperty("50")
    text_input_str = StringProperty("foo")
    def on_button_click(self):
        print("Button clicked")
        if self.count_enabled:
            self.counter += 1
            self.my_text = f"You clicked {self.counter} times"

    def on_toggle_button_state(self, widget):
        print("Toggle state:" + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    # def on_slider_value(self, widget):
    #     print("Slider: " + str(widget.value))
    #     self.slider_value_txt = str(int(widget.value))
    def on_text_validate(self, widget):
        self.text_input_str = widget.text

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)
# class GridLayoutExample(GridLayout):
#    pass
class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

TheLabApp().run()
