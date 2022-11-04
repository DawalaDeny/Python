from PIL import Image
import time
from civilian import Civilian
from Exception import *
from kapiteinPiraat import Kapitein, Piraat
import random

class Vessel:
    def __init__(self, name: str, masts: int, acceleration: int, img_path: str):
        self.name = name
        self.masts = masts
        self.acceleration = acceleration
        self.img_path = img_path
        self.speed = 0
    def getname(self):
        return self.name
    def getmasts(self):
        return self.masts
    def getacceleration(self):
        return self.acceleration
    def getimg(self):
        return self.img_path
    def getspeed(self):
        return self.speed

    def ShowImage(self):
        image = Image.open(self.img_path)
        image = image.resize((100,100))
        image.show()
        time.sleep(1)
        image.close()
    def embark(self, passenger):
        pass

    def disembark(self, passenger):
        pass

#is eerste bool bv. er is wind aanwezig (true) en tweede bool in ons voordeel (true)?
    def sail(self, windstream: tuple[bool, bool]):
        multiplier = 0
        if windstream[0]:
            multiplier += 2
        if not windstream[1]:
            multiplier -= 0.5
        if multiplier < 0:
            multiplier = 0
        self.speed = self.masts * self.acceleration * multiplier


class Boat(Vessel):
    def __init__(self, name: str, acceleration: int, img_path: str, masts: int = 1):
        if acceleration < 1 or acceleration >25:
            raise InvalidValueAccelerationBoat(acceleration)
        else:
            super().__init__(name, masts, acceleration, img_path)
            self.passengers = []
            self.speed = 0

    def __str__(self):
        output=f"naam boot: {self.name} met {len(self.passengers)} passegiers met een snelheid" \
               f" van {self.speed} km/h"
        return output
    def sail(self, windstream: tuple[bool,bool]):
        if len(self.passengers) > 0:
            super(Boat, self).sail(windstream)

    def embark(self, passegier):
        if len(self.passengers) < 1:
            if isinstance(passegier, Civilian):
                self.passengers.append(passegier)
            else:
                print("Dit is geen passegier")
        else:
            i = 0
            gevonden = False
            while not gevonden & i < len(self.passengers):
                x = self.passengers[i]
                if x == passegier:
                    gevonden = True
                i += 1
            if not gevonden:
                self.passengers.append(passegier)
    def disembark(self, passegier):
        if len(self.passengers) > 0:
            gevonden = False
            i=0
            while gevonden == False & i < len(self.passengers):
                x = self.passengers[i]
                if x == passegier:
                    gevonden = True
                i+=1
            if gevonden == True:
                self.passengers.remove(passegier)
            else:
                print(f"Passegier met de naam {passegier.get_name()} is niet aanwezig")
        else:
            print("Er zijn momenteel 0 passegiers aan boord.")
    def getpassengers(self):
        return self.passengers
class Ship(Vessel):
    def __init__(self, name: str, acceleration: int, img_path: str, masts: int = 2):
        self.captain = None
        if masts < 2:
            raise InvalidValueMasts(masts)
        elif acceleration < 0:
            raise InvalidValueAccelerationShip(acceleration)
        else:
         super().__init__(name, masts, acceleration, img_path)

    def embark(self, passenger):
        if isinstance(passenger, Kapitein):
            if self.captain is None:
                self.captain = passenger
            else:
                if len(self.captain.get_crew()) > len(passenger.get_crew()):
                    pass
                elif len(self.captain.get_crew()) < len(passenger.get_crew()):
                    self.captain = passenger
                else:
                    i = random
                    i.randint(0, 1)
                    if i == 1:
                        self.captain = passenger

        elif isinstance(passenger, Piraat):
            if self.captain is None:
                print("A crew without a captain is no crew!")
            else:
                self.captain.add_crewmember(Piraat)
        else:
            print("Error, only a pirate or a captain can enter the ship!")
    def disembark(self, passenger):
        if self.captain is None:
            print("There is no captain on board!")
        else:
            if isinstance(passenger, Kapitein):
                self.captain = None
            elif isinstance(passenger, Piraat):
                crew = self.captain.get_crew
                print(crew)
                print(crew)
                i = 0
                gevonden = False
                while i < len(crew):
                    if crew[i] == passenger:
                        self.captain.remove_crewmember(passenger)
                        gevonden = True
                    else:
                        i +=1
                if gevonden:
                    print(f"Piraat: {passenger.get_naam()} is succesvol verwijderd")
                else:
                    print(f"Piraat: {passenger.get_naam()} is NIET succesvol verwijderd")
    def sail(self, windstream: tuple[bool, bool]):
        if self.captain is not None:
            super(Ship, self).sail(windstream)
    def __str__(self):
        return f"Name of the ship is: {self.name} \n" \
               f"The captain is: {self.captain} \n" \
               f"Speed is: {self.speed}"