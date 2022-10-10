class Ocean:
    def __init__(self, grooteSpeelveld:int, aantalschepen:int):
        self.speelveld = list([grooteSpeelveld,grooteSpeelveld])
        self.range = grooteSpeelveld
        self.aantalSchepen = aantalschepen

    def opvullenSpeelveld(self):
        for j in range(self.range):
            print(self.speelveld)
            rij = [0 for i in range(self.range)]
            self.speelveld.append(rij)
        print(self.speelveld)

if __name__ == '__main__':
    ocean1 = Ocean(grooteSpeelveld=5, aantalschepen=1)
    ocean1.opvullenSpeelveld()
