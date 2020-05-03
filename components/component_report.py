import time

class ComponentReport:
    status = "OPERATIONAL" # ERROR, NEEDS_MAINTENANCE ... PODRÍA SER ENUM
    component_health = "HEALTHY"
    battery_charge = 0.6
    # AGREGAR ATRIBUTOS IGUALES EN TODOS LOS COMPONENTES

    def __init__(self):
        self.time = time.time()
        pass

