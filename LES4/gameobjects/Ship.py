class Ship:
    def __init__(self, lengte:int):
        self.lengte:int = lengte
        self.geraaktedelen = 0
        self.positie = [] * lengte

    def vulPosities(self, begin:int, richting:str):
        pass

    def setPositie(self, coordinaten:list):
        self.positie = coordinaten

    def getPositie(self) -> list:
        return self.positie

    def isBootGeraakt(self, rij, kol) ->bool:
        geraakt = False
        for i in range(self.lengte ):
            if self.positie[i] ==[rij,kol]:
                geraakt = True
                self.geraaktedelen += 1
        return geraakt

