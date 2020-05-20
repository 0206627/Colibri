from components.avionics_component import CPU, SD
from components.comms_component import Antenna
from components.power_component import Batteries, EPS
from components.thermal_component import TempSensor
from flight_control.con_op_manager import ConOpManager
from flight_control.flight_system import FlightSystem

flight_system = FlightSystem()

antenna = Antenna()
battery = Batteries()
cpu = CPU()
sd = SD()
temp_sensor = TempSensor()

flight_system.add_component(antenna)
flight_system.add_component(battery)
flight_system.add_component(cpu)
flight_system.add_component(sd)
flight_system.add_component(temp_sensor)

conOp = ConOpManager()

while True:

    battery.battery_charge = (float)(input("Battery charge % [0.0, 1.0]: "))
    antenna.comms_check = eval(input("Antenna communication [True, False]: "))
    cpu.performance_percentage = (float)(input("CPU performance % [0.0, 1.0]: "))
    sd.storage_free_percentage = (float)(input("SD storage free % [0.0, 1.0]: "))
    temp_sensor.temp = (float)(input("Temperature sensor temp ºC [-10, 150]: "))

    current_conop = conOp.get_current_conop()
    flight_conditions = flight_system.retrieve_flight_conditions()
    new_conop = flight_system.decide_con_op_mode(flight_conditions, current_conop)
    print("")
    print("Before: ", current_conop)
    print("Flight Conditions:")
    flight_system.print_flight_conditions()
    print("After: ", new_conop)
    print("")
    print("------------------------------")
    print("")
