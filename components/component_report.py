import time
from flight_control.conop_modes import ComponentStatus, ComponentHealth

class ComponentReport:

    status = ComponentStatus.OPERATIONAL
    component_health = ComponentHealth.HEALTHY

    # AGREGAR ATRIBUTOS IGUALES EN TODOS LOS COMPONENTES

    def __init__(self):
        self.time = time.time()

class PowerReport(ComponentReport):

    def __init__(self):
        super().__init__()
        self.battery_charge = 1.0

class AvionicsReport(ComponentReport):
    def __init__(self):
        super().__init__()
        self.storage_free_percentage = 1.0
        self.performance_percentage = 1.0

class CommsReport(ComponentReport):
    def __init__(self):
        super().__init__()
        self.comms_check = True

class ThermalReport(ComponentReport):
    def __init__(self):
        super().__init__()
        self.temp = 60


