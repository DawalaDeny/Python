from Ship import Ship
class Ocean:
    def __init__(self,boot:Ship, grooteSpeelveld:int):
        self.speelveld = [["."]*grooteSpeelveld] * grooteSpeelveld
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


