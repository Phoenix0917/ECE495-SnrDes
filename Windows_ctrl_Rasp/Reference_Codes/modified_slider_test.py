from __future__ import print_function
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout

class ModifiedSlider(Slider):
    def __init__(self, **kwargs):
        self.register_event_type('on_release')
        super(ModifiedSlider, self).__init__(**kwargs) # runs parent class init

    def on_release(self):
        pass

    def on_touch_up(self, touch): # gets called twice - once by the slider and once by the screen?
        super(ModifiedSlider, self).on_touch_up(touch) # runs parent classes on touch up function and stores it the touch it recieved 
        if touch.grab_current == self: # checks if the current touch is the one that was dispatched for this widget
            self.dispatch('on_release')
            return True

def callback_release(instance):
    print('The Slider object {} is released'.format(instance))

def callback_value(instance, value):
    print('The slider {} value changed to: {}'.format(instance, value))

modified_slider_instance = ModifiedSlider()
modified_slider_instance.bind(on_release=callback_release)
modified_slider_instance.bind(value=callback_value)

slider_instance = Slider()
slider_instance.bind(value=callback_value)

class TestSlider(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        root.add_widget(modified_slider_instance)
        root.add_widget(slider_instance)
        return root

if __name__ == '__main__':
    TestSlider().run()