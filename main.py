from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import obd
import random


class Dashboard(Widget):
    myobd = obd.OBD()

    spd = NumericProperty(0)
    rpm = NumericProperty(0)
    fuel_rate = NumericProperty(0)
    fuel_level = NumericProperty(0)
    coolant_tmp = NumericProperty(0)
    intake_tmp = NumericProperty(0)

    def update(self, dt):
    	potential_spd = self.myobd.query(obd.commands.SPEED).value
        potential_spd = 0 if potential_spd == None
        self.spd = round(potential_spd * 0.621371, 2)

    	potential_rpm = self.myobd.query(obd.commands.RPM).value
        potential_rpm = 0 if potential_rpm == None
        self.rpm = potential_rpm

        potential_maf = self.myobd.query(obd.commands.MAF).value
    	potential_maf = 1 if potential_maf == None # no division by 0
        # instant fuel rate
        self.fuel_rate = round(self.spd * (7.718 / potential_maf), 2)

        potential_coolant_tmp = self.myobd.query(obd.commands.COOLANT_TEMP).value
        potential_coolant_tmp = 0 if potential_coolant_tmp == None
        self.coolant_tmp = potential_coolant_tmp

        potential_intake_tmp = self.myobd.query(obd.commands.INTAKE_TEMP).value
        potential_intake_tmp = 0 if potential_intake_tmp == None
        self.intake_tmp = potential_intake_tmp

        potential_fuel_level = self.myobd.query(obd.commands.FUEL_LEVEL).value
        potential_fuel_level = 0 if potential_fuel_level == None
        self.fuel_level = potential_fuel_level

class DashboardApp(App):
    def build(self):
        board = Dashboard()
        Clock.schedule_interval(board.update, 1.0 / 10.0)
        return board


if __name__ == '__main__':
    DashboardApp().run()
