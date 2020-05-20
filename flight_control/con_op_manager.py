from flight_control.conop_modes import ConOp

class ConOpManager:

    status = ConOp.NOMINAL

    def __init__(self):
        pass

    def get_current_conop(self):
       return self.status

    def set_current_conop(self, conop):
        self.status = conop