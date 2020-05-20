from components.component import Component
from flight_control.conop_modes import ConOp
from flight_control.conop_switcher_input import ConOpSwitcherInput

class FlightSystem:
    def __init__(self):
        self.component_list = list()
        self.cop_switcher_input = ConOpSwitcherInput()

    def add_component(self, component):
        # type: (Component) -> None
        self.component_list.append(component)

    def list_all_components(self):
        for i in self.component_list:
            print(i.component_name)

    def retrieve_flight_conditions(self):

        # type: () -> ConOpSwitcherInput
        for component in self.component_list:
            report = component.report_status()
            component_id = component.component_name
            self.cop_switcher_input = self.report_handler(self.cop_switcher_input, report, component_id)

        return self.cop_switcher_input

    def print_flight_conditions(self):

        attributes = vars(self.cop_switcher_input)
        print(', '.join("%s: %s" % item for item in attributes.items()))

    def decide_con_op_mode(self, cop_switcher_input, current_conop):

        # type: (ConOpSwitcherInput, ConOp) -> ConOp

        if not cop_switcher_input.antena_comms_ok or not cop_switcher_input.temp_ok:
            return ConOp.CONTINGENCY

        if not cop_switcher_input.power_ok or not cop_switcher_input.cpu_performance_ok or not cop_switcher_input.sd_storage_ok:
            return ConOp.NOMINAL

        if cop_switcher_input.power_ok and current_conop == ConOp.NOMINAL:
            return ConOp.PAYLOAD_OPERATIONS

        return current_conop

    @staticmethod
    def report_handler(cop_switcher_input, report, component_id):

        if component_id == "Batteries":
            cop_switcher_input.power_ok = True if report.battery_charge > 0.5 else False

        elif component_id == "CPU":
            cop_switcher_input.cpu_performance_ok = True if report.performance_percentage > 0.7 else False

        elif component_id == "SD":
            cop_switcher_input.sd_storage_ok = True if report.storage_free_percentage > 0.1 else False

        elif component_id == "Antenna":
            cop_switcher_input.antena_comms_ok = True if report.comms_check else False

        elif component_id == "Temperature Sensor":
            cop_switcher_input.temp_ok = True if 0 < report.temp < 100 else False

        return cop_switcher_input