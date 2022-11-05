from Vessel import Vessel
from Civilian import Civilian
from Exception import *

class Boat(Vessel):
    def __init__(self, name: str, acceleration: int, img_path: str, masts: int = 1):
        if acceleration < 1 or acceleration > 25:
            raise InvalidValueAccelerationBoat(acceleration)
        else:
            super().__init__(name, masts, acceleration, img_path)
            self.passengers = []
            self.speed = 0

    def __str__(self):
        return f"naam boot: {self.name} met {len(self.passengers)} passegiers met een snelheid" \
               f" van {self.speed} km/h"

    def sail(self, windstream: tuple[bool,bool]):
        if len(self.passengers) > 0:
            super(Boat, self).sail(windstream)

    def embark(self, passegier):
        if isinstance(passegier, Civilian):
            if len(self.passengers) < 1:
                    self.passengers.append(passegier)
            else:
                i = 0
                gevonden = False
                while not gevonden and i < len(self.passengers):
                    x = self.passengers[i]
                    if x == passegier:
                        gevonden = True
                    i += 1
                if not gevonden:
                    self.passengers.append(passegier)
        else:
            print("Dit is geen passegier")

    def disembark(self, passegier=None):
        self.passengers = None

    def getpassengers(self):
        return self.passengers