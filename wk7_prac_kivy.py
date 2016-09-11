
from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertMilesToKilometresApp(App):
    def build(self):
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('wk7_prac_kivy.kv')
        return self.root

    def handle_calculator(self):
        value = self.validate_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.validate_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculator()

    def validate_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

ConvertMilesToKilometresApp().run()
