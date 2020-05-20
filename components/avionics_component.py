from components.component import AvionicsComponent

class CPU(AvionicsComponent):

    def __init__(self):
        super().__init__("CPU")


class SD(AvionicsComponent):

    def __init__(self):
        super().__init__("SD")
