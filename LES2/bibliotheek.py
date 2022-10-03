class Bibliotheek:

    def __init__(self):
        self.lijst = [12, 12, 13, 14, 12]

    def printLijst(self):
        for i in self.lijst:
            print(i)

if __name__ == '__main__':
    b1 = Bibliotheek()
    b1.printLijst()
