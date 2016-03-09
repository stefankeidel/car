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
        if potential_spd == None:
            self.spd = 0
        else:
            self.spd = round(potential_spd * 0.621371, 2)

        potential_rpm = self.myobd.query(obd.commands.RPM).value
        if potential_rpm == None:
            self.rpm = 0
        else:
            self.rpm = int(potential_rpm)

        potential_maf = self.myobd.query(obd.commands.MAF).value
        if potential_maf == None:
            potential_maf = 1

        # instant fuel rate
        self.fuel_rate = round(self.spd * (7.718 / potential_maf), 2)

        potential_coolant_tmp = self.myobd.query(obd.commands.COOLANT_TEMP).value
        if potential_coolant_tmp == None:
            self.coolant_tmp = 0
        else:
            self.coolant_tmp = int(potential_coolant_tmp)

        potential_intake_tmp = self.myobd.query(obd.commands.INTAKE_TEMP).value
        if potential_intake_tmp == None:
            self.intake_tmp = 0
        else:
            self.intake_tmp = int(potential_intake_tmp)

        potential_fuel_level = self.myobd.query(obd.commands.FUEL_LEVEL).value
        if potential_fuel_level == None:
            self.fuel_level = 0
        else:
            self.fuel_level = int(potential_fuel_level)

class DashboardApp(App):
    def build(self):
        board = Dashboard()
        Clock.schedule_interval(board.update, 1.0 / 10.0)
        return board


if __name__ == '__main__':
    DashboardApp().run()
