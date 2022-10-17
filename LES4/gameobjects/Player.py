from LES4.gameobjects import Ocean
class Player:
    def __init__(self,ocean:Ocean, naam:str,  aantalBommen:int):
        self.naam = naam
        self.aantalBeschikbareBommen = aantalBommen
        self.gegooideBommen = 0
        self.ocean = ocean
    def bomGegooid(self):
        self.gegooideBommen += 1
        self.aantalBeschikbareBommen -= 1