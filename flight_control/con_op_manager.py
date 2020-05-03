from flight_control.conop_modes import ConOp

class ConOpManager:
    status = "Default"

    def __init__(self):
        pass

    def get_current_conop(self):

        # ELEGIR QUÉ CONOP MODE CON EL CONOPHANDLERINPUT

        """
        Returns current flight con op mode.
        :return: ConOp mode.
        """
        # TODO Mode handling logic
        return ConOp.NOMINAL
