class InvalidValue(ValueError):
    def __init__(self, waarde):
        self.waarde = waarde

    def __str__(self):
        return f"Acceleration must be between 1 and 25, yours was: {self.waarde}"