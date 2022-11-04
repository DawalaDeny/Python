class InvalidValueAccelerationBoat(ValueError):
    def __init__(self, waarde):
        self.waarde = waarde

    def __str__(self):
            return f"Acceleration must be between 1 and 25, yours was: {self.waarde}"

class InvalidValueAccelerationShip(ValueError):
     def __init__(self, waarde):
        self.waarde = waarde

     def __str__(self):
        return f"Acceleration must be higher than 0, yours was: {self.waarde}"

class InvalidValueMasts(ValueError):
    def __init__(self, waarde):
        self.waarde = waarde

    def __str__(self):
        return f"A ship has atleast 2 masts, yours was: {self.waarde}"