class Ship:
    def __init__(self, lengte:int):
        self.lengte:int = lengte
        self.gezonken:bool = "false"
        self.positie = [] * lengte

    def vulPosities(self, begin:int, richting:str):
        pass #Posities zijn getallen, eerst rij dan kolom. Boven: -10 Onder: +10 Links: -1 Rechts: +1


