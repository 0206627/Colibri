from components.component_report import ComponentReport
from flight_control.conop_modes import ConOp

class Component:

    def __init__(self, name, subsystem):
        self.component_name = name
        self.component_subsystem = subsystem

    def report_status(self):
        # regresa un objeto de component_report
        report = ComponentReport()              # usar un patrón Factory / Builder
        return report

    def set_conop_mode(self):
        print("Not Implemented")

    def start_behaviour(self, conop):
        # type: (ConOp) -> None
        print("Not Implemented")
