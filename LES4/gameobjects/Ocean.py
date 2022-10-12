from Ship import Ship
import random
class Ocean:
    def __init__(self,boot:Ship, grooteSpeelveld:int):
        self.speelveld = [["." for x in range(grooteSpeelveld)] for y in range(grooteSpeelveld)]
        self.range = grooteSpeelveld
        self.boot = boot

    def opvullenSpeelveld(self):
        rijI = 0
        output:str = f"  0 1 2 3 4\n"
        output += f"{rijI} "
        for i in range(self.range):
            for j in range(self.range):
                output += f"{self.speelveld[i][j]} "
            rijI += 1
            if (rijI < self.range):
                output += f"\n{rijI} "
        print(output)

    def locatieBootBepalen(self):
        randomKol = random.randint(0, self.range-1)
        randomRij = random.randint(0, self.range-1)
        randomRichting:str = random.choice(["Noord", "Oost", "Zuid", "West"])
        huidigelocatie = [randomRij,randomKol]
        zoeken:bool= True
        while zoeken:
            if randomRichting.startswith("N"):
                ifke = randomRij - self.boot.lengte
                if ifke >= -1:
                    list = [[huidigelocatie[0],huidigelocatie[1]], [huidigelocatie[0]-1, huidigelocatie[1]], [huidigelocatie[0]-2, huidigelocatie[1]]]
                    self.boot.setPositie(list)
                    # self.speelveld[huidigelocatie[0]][huidigelocatie[1]] = "O"
                    # self.speelveld[huidigelocatie[0]-1][huidigelocatie[1]] = "O"
                    # self.speelveld[huidigelocatie[0]-2][huidigelocatie[1]] = "O"
                    zoeken = False
                else:
                    randomRichting: str = random.choice(["Noord", "Oost", "Zuid", "West"])
            elif randomRichting.startswith("O"):
                ifke = randomKol -self.boot.lengte
                if ifke < 0:
                    list = [[huidigelocatie[0], huidigelocatie[1]], [huidigelocatie[0], huidigelocatie[1]+1], [huidigelocatie[0], huidigelocatie[1]+2]]
                    self.boot.setPositie(list)
                    # self.speelveld[huidigelocatie[0]][huidigelocatie[1]] = "O"
                    # self.speelveld[huidigelocatie[0]][huidigelocatie[1]+1] = "O"
                    # self.speelveld[huidigelocatie[0]][huidigelocatie[1]+2] = "O"
                    zoeken = False
                else:
                    randomRichting: str = random.choice(["Noord", "Oost", "Zuid", "West"])
            elif randomRichting.startswith("Z"):
                ifke = randomRij - self.boot.lengte
                if ifke < 0:
                    list = [[huidigelocatie[0], huidigelocatie[1]], [huidigelocatie[0] + 1, huidigelocatie[1]],[huidigelocatie[0] + 2, huidigelocatie[1]]]
                    self.boot.setPositie(list)
                    # self.speelveld[huidigelocatie[0]][huidigelocatie[1]] = "O"
                    # self.speelveld[huidigelocatie[0] + 1][huidigelocatie[1]] = "O"
                    # self.speelveld[huidigelocatie[0] + 2][huidigelocatie[1]] = "O"
                    zoeken = False
                else:
                    randomRichting: str = random.choice(["Noord", "Oost", "Zuid", "West"])
            elif randomRichting.startswith("W"):
                ifke = randomKol - self.boot.lengte
                if ifke >= -1:
                    list = [[huidigelocatie[0], huidigelocatie[1]], [huidigelocatie[0], huidigelocatie[1] - 1],[huidigelocatie[0], huidigelocatie[1] - 2]]
                    self.boot.setPositie(list)
                    # self.speelveld[huidigelocatie[0]][huidigelocatie[1]] = "O"
                    # self.speelveld[huidigelocatie[0]][huidigelocatie[1] - 1] = "O"
                    # self.speelveld[huidigelocatie[0]][huidigelocatie[1] - 2] = "O"
                    zoeken = False
                else:
                    randomRichting: str = random.choice(["Noord", "Oost", "Zuid", "West"])








