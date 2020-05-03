from components.component import Component

class Batteries(Component):
    def __init__(self):
        super().__init__("Batteries", "Power")

class EPS(Component):
    def __init__(self):
        super().__init__("EPS", "Power")
