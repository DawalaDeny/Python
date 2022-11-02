class Civilian:
    def __init__(self, name:str):
        self.name=name
    def get_name(self):
        return self.name
    def __str__(self):
        output = f"This is a civilian named {self.name}"
        return output