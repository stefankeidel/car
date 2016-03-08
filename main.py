from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import obd
import random


class Dashboard(Widget):
    myobd = obd.OBD()

    # row 1: speed, rpm, fuel rate
    spd = NumericProperty(0)
    rpm = NumericProperty(0)
    fuel_rate = NumericProperty(0)

    cmd_spd = obd.commands.SPEED
    cmd_rpm = obd.commands.RPM
    cmd_fuel_rate = obd.commands.FUEL_RATE

    # row 2: oil, cooland, air tmps
    oil_tmp = NumericProperty(0)
    coolant_tmp = NumericProperty(0)
    air_tmp = NumericProperty(0)

    cmd_oil_tmp = obd.commands[1][92]
    cmd_coolant_tmp = obd.commands.COOLANT_TEMP
    cmd_air_tmp = obd.commands[1][70]

    def update(self, dt):
    	potential_spd = self.myobd.query(self.cmd_spd).value
    	if potential_spd == None:
    		potential_spd = 0   
        self.spd = round(potential_spd * 0.621371,2)

    	potential_rpm = self.myobd.query(self.cmd_rpm).value
    	if potential_rpm == None:
    		potential_rpm = 0   
        self.rpm = potential_rpm

        potential_maf = self.myobd.query(obd.commands.MAF).value
    	if potential_maf == None:
    		potential_maf = 1
        self.fuel_rate = round(self.spd * (7.718 / potential_maf),2)

        potential_oil_tmp = self.myobd.query(self.cmd_oil_tmp).value
    	if potential_oil_tmp == None:
    		potential_oil_tmp = 0   
        self.oil_tmp = potential_oil_tmp

        potential_coolant_tmp = self.myobd.query(self.cmd_coolant_tmp).value
    	if potential_coolant_tmp == None:
    		potential_coolant_tmp = 0   
        self.coolant_tmp = potential_coolant_tmp

        potential_air_tmp = self.myobd.query(self.cmd_air_tmp).value
    	if potential_air_tmp == None:
    		potential_air_tmp = 0   
        self.air_tmp = potential_air_tmp

class DashboardApp(App):
    def build(self):
        board = Dashboard()
        Clock.schedule_interval(board.update, 1.0 / 10.0)
        return board


if __name__ == '__main__':
    DashboardApp().run()

