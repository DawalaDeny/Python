from Vessel import Vessel
from Exception import *
from Kapitein import Kapitein
from Piraat import Piraat
import random

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
                    rand = random
                    i = rand.randint(0, 1)
                    if i == 1:
                        self.captain = passenger
        elif isinstance(passenger, Piraat):
            if self.captain is None:
                print("A crew without a captain is no crew!")
            else:
                    self.captain.add_crewmember(passenger)
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
        print(self.captain.get_crew)
        print(self.captain)

    def __str__(self):
        return f"Name of the ship is: {self.name} \n" \
               f"The captain is: {self.captain} \n" \
               f"Speed is: {self.speed}"