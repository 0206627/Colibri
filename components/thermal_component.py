from components.component import ThermalComponent

class TempSensor(ThermalComponent):

    def __init__(self):
        super().__init__("Temperature Sensor")