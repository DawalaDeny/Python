import Ocean
class Player:
    def __init__(self, naam:str, ocean:Ocean, aantalBommen:int):
        self.naam = naam
        self.aantalBeschikbareBommen = aantalBommen
        self.gegooideBommen = 0
        self.ocean = ocean