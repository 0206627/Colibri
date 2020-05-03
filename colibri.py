# Get current CON_OP STATUS
from components.power_component import Batteries, EPS
from flight_control.con_op_manager import ConOpManager
from flight_control.flight_system import FlightSystem

flight_system = FlightSystem()

flight_system.add_component(Batteries())
flight_system.add_component(EPS())
conOp = ConOpManager()

while True:
    current_status = conOp.get_current_conop()
    flight_system.retrieve_flight_conditions()
    print(current_status)
