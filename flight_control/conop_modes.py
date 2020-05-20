from enum import Enum

class ConOp(Enum):
    NOMINAL = 0
    COMMS = 1
    LOW_ENERGY = 2
    PAYLOAD_OPERATIONS = 3
    CONTINGENCY = 4

class ComponentStatus(Enum):
    OPERATIONAL = 0
    NEEDS_MAINTENANCE = 1
    ERROR = 2

class ComponentHealth(Enum):
    HEALTHY = 0
    DAMAGED = 1
    FATAL = 2
