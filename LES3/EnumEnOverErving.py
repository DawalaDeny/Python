from enum import Enum
class AirType(Enum):
    jet = 0,
    propeller = 1
class GroundType(Enum):
    wheel = 0,
    tracks = 1
class Vehicle(object):
    def __init__(self, name:str):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return f"{self.name}"
class GroundVehicle(Vehicle):
    def __init__(self, gtype: GroundType, **kwargs) -> None:
        self.__type = gtype
        super(GroundVehicle, self).__init__(**kwargs)
    def drive(self):
        print(f"{self.getName()} is driving...")
    def getGtype(self):
        return self.__type.name
class AirVehicle(Vehicle):
    def __init__(self, atype: AirType, **kwargs) -> None:
        self.__type = atype
        super(AirVehicle, self).__init__(**kwargs)
    def fly(self):
        print(f"{self.getName()} is flying...")

    def getAtype(self):
        return self.__type.name
class Car(GroundVehicle):
    def __init__(self, **kwargs):
        super(Car, self).__init__(gtype=GroundType.wheel, **kwargs)
class FlyingCar(GroundVehicle, AirVehicle):
    def __init__(self, **kwargs):
        super(FlyingCar, self).__init__(gtype=GroundType.wheel, atype=AirType.jet, **kwargs)
    def __str__(self):
        return f"{self.getName()} {self.getGtype()} + {self.getAtype()}"
if __name__ == '__main__':
    a = AirType.jet
    print(a)

    tesla:Car = Car(name="Tesla")
    print(tesla)
    tesla.drive()

    flyingcar: FlyingCar = FlyingCar(name="FlyCar")
    print(flyingcar)
    flyingcar.drive()
    flyingcar.fly()