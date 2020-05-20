from components.component_report import ComponentReport, PowerReport, AvionicsReport, CommsReport, ThermalReport
from flight_control.conop_modes import ConOp

class Component:

    def __init__(self, name, subsystem):
        self.component_name = name
        self.component_subsystem = subsystem

    def report_status(self):
        report = ComponentReport()
        return report

    def set_conop_mode(self):
        print("Not Implemented")

    def start_behaviour(self, conop):
        # type: (ConOp) -> None
        print("Not Implemented")

class PowerComponent(Component):

    battery_charge = 1.0

    def __init__(self, name):
        super().__init__(name, "Power")

    def report_status(self):
        report = PowerReport()
        report.battery_charge = self.battery_charge
        return report

class AvionicsComponent(Component):

    storage_free_percentage = 1.0
    performance_percentage = 1.0

    def __init__(self, name):
        super().__init__(name, "Avionics")

    def report_status(self):
        report = AvionicsReport()
        report.storage_free_percentage = self.storage_free_percentage
        report.performance_percentage = self.performance_percentage
        return report

class CommsComponent(Component):

    comms_check = True

    def __init__(self, name):
        super().__init__(name, "Comms")

    def report_status(self):
        report = CommsReport()
        report.comms_check = self.comms_check
        return report

class ThermalComponent(Component):

    temp = 60

    def __init__(self, name):
        super().__init__(name, "Thermal")

    def report_status(self):
        report = ThermalReport()
        report.temp = self.temp
        return report
