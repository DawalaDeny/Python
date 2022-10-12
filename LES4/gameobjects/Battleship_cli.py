from LES4.gameobjects.Ocean import Ocean
from LES4.gameobjects.Ship import Ship
#Waarom werkt dit niet als je dit buiten gameobjects plaatst?


class Battleship:
    pass
if __name__ == '__main__':
    boot:Ship = Ship(lengte=5)
    oceaan:Ocean = Ocean(boot,grooteSpeelveld=5)
    oceaan.opvullenSpeelveld()
    print("test")






