class Civilian:
    def __init__(self, name: str):
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return f"This is a civilian named {self.name}"
