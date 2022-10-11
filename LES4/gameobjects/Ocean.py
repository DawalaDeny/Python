class Ocean:
    def __init__(self, grooteSpeelveld:int, aantalschepen:int):
        self.speelveld = [["."]*grooteSpeelveld] * grooteSpeelveld
        self.range = grooteSpeelveld
        self.aantalSchepen = aantalschepen

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
    ocean1 = Ocean(grooteSpeelveld=5, aantalschepen=1)
    ocean1.opvullenSpeelveld()
