from LES4.gameobjects.Ocean import Ocean
from LES4.gameobjects.Ship import Ship
from LES4.gameobjects.Player import Player
import time
#Waarom werkt dit niet als je dit buiten gameobjects plaatst?


class Battleship:
    pass
if __name__ == '__main__':
    print("Wat is uw naam?")
    naam = input()
    time.sleep(1)
    print(f"Hallo! {naam}\n\nDit is ZEESLAG")
    time.sleep(0.5)
    print(f"\n\nHoe groot moet het speelveld zijn?")
    groote = int(input())
    niet5:bool=True
    while niet5:
        if (groote > 4) and (groote<11):
            niet5 = False
        else:
            print(f"Geef een getal groter dan 4 en kleiner dan 11 in te geven!")
            groote = int(input())
    print(f"Hoeveel bommen wilt u?")

    bommen = int(input())
    ongeldig: bool = True
    while ongeldig:
        if bommen > 2:
            ongeldig=False
        else:
            print(f"Gelieve een getal in te geven groter dan 2")
            bommen = int(input())
    boot:Ship = Ship(lengte=3)
    oceaan:Ocean = Ocean(boot,grooteSpeelveld=groote)
    speler: Player = Player(oceaan, naam=naam, aantalBommen=bommen)
    oceaan.locatieBootBepalen()
    oceaan.opvullenSpeelveld()
    print(boot.getPositie())








