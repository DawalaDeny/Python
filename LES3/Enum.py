from enum import Enum
class AirType(Enum):
    jet=0,
    propeller=1
class GroundType(Enum):
    wheel = 0,
    tracks=1
if __name__ == '__main__':
    a = AirType.jet
    print(a)