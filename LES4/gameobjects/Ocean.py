class Ocean:
    def __init__(self, grooteSpeelveld:int, aantalschepen:int):
        self.speelveld = [[0]*grooteSpeelveld] * grooteSpeelveld
        self.range = grooteSpeelveld
        self.aantalSchepen = aantalschepen

    def opvullenSpeelveld(self):
        print("---0, 1, 2, 3, 4----")
        x = 0
        for i in self.speelveld:
            print (x, i)
            while x > self.range:
                x = +1


if __name__ == '__main__':
    ocean1 = Ocean(grooteSpeelveld=5, aantalschepen=1)
    ocean1.opvullenSpeelveld()
