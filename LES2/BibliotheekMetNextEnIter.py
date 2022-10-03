class Bibliotheek:
    def __init__(self, boekenlijst):
        self.boekenlijst:list = boekenlijst
        self.i = -1

    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        return self.boekenlijst[self.i]

if __name__ == '__main__':
    bib = Bibliotheek(["Boek1", "Tarzan", "boekk", "buka"])
    print(next(bib))
    print(next(bib))
    print(next(bib))
