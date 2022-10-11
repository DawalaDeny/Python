from Ship import Ship
class Ocean:
    def __init__(self,boot:Ship, grooteSpeelveld:int):
        self.speelveld = [["."]*grooteSpeelveld] * grooteSpeelveld
        self.range = grooteSpeelveld
        self.boot = boot

    def opvullenSpeelveld(self):
        rijI = 0
        str:str = f"  0 1 2 3 4\n"
        str += f"{rijI} "
        for i in range(self.range):
            for j in range(self.range):
                str += f"{self.speelveld[i][j]} "
            rijI += 1
            if (rijI < self.range):
                str += f"\n{rijI} "
        print(str)

if __name__ == '__main__':
    boot:Ship = Ship(lengte=5)
    o = Ocean(boot, grooteSpeelveld=5)
    o.opvullenSpeelveld()
