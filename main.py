from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import obd
import random

class Dashboard(Widget):
    rpm = NumericProperty(0)
    mpg = NumericProperty(0)
    myobd = obd.OBD()
    cmd_rpm = obd.commands.RPM

    def update(self, dt):
    	potential_rpm = self.myobd.query(self.cmd_rpm).value
    	if potential_rpm == None:
    		potential_rpm = 1500.0   
        self.rpm = potential_rpm

class DashboardApp(App):
    def build(self):
        board = Dashboard()
        Clock.schedule_interval(board.update, 10.0 / 10.0)
        return board


if __name__ == '__main__':
    DashboardApp().run()