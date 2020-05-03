from components.component import Component
from flight_control.conop_modes import ConOp
from flight_control.conop_switcher_input import ConOpSwitcherInput


class FlightSystem:
    def __init__(self):
        self.component_list = list()
        pass

    def add_component(self, component):
        # type: (Component) -> None
        self.component_list.append(component)

    def list_all_components(self):
        for i in self.component_list:
            print(i.component_name)

    def retrieve_flight_conditions(self):
        cop_switcher_input = ConOpSwitcherInput()
        for component in self.component_list:
            report = component.report_status()
            component_id = component.component_name
            self.report_handler(cop_switcher_input, report, component_id)

    def decide_con_op_mode(self, cop_switcher_input, current_conop):
        # type: (ConOpSwitcherInput, ConOp) -> None
        if cop_switcher_input.power_ok and current_conop == ConOp.NOMINAL:
            pass

    @staticmethod
    def report_handler(cop_switcher_input, report, component_id):

        # esto ocurre por cada componente

        if component_id == "Batteries":
            print("Battery charge: ",report.battery_charge)
            cop_switcher_input.power_ok = True if report.battery_charge > .5 else False
            print("Conop switcher power: ",cop_switcher_input.power_ok)

