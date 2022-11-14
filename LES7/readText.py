class IOtekstbestand:
    def __init__(self):
        pass
    def printTekst(self):
        str = open("C:\\Users\\shabo\\Desktop\\School\\2022-2023\\Python\\tekst.txt", "r")
        str = str.read()
        print(str)

    def printXdeLijntje(self, lijn: int):
        tekst = open("C:\\Users\\shabo\\Desktop\\School\\2022-2023\\Python\\tekst.txt", "r")
        str2 = None
        i = 0
        while i < lijn:
            str2 = tekst.readline()
            i += 1
        print(str2)

    def writeNewTextFile(self, content: str):
        tekst = open("tekstje.txt", "w")
        tekst.write(content)

    def addText(self, content: str):
        tekst = open("tekstje.txt", "a")
        tekst.write(content)

if __name__ == '__main__':
    object = IOtekstbestand()
    #object.printTekst()
    object.printXdeLijntje(2)
    object.writeNewTextFile("s,dsn,d nqsbdhbqhd qsdbqhsjbd qhbdqsbhd qsdqsd qsdqsdqsdsqdqsdqsd")
    object.addText("\ns,dsn,d nqsbdhbqhd qsdbqhsjbd qhbdqsbhd qsdqsd qsdqsdqsdsqdqsdqsd")
    object.addText("\ns,dsn,d nqsbdhbqhd qsdbqhsjbd qhbdqsbhd qsdqsd qsdqsdqsdsqdqsdqsd")
    object.addText("\ns,dsn,d nqsbdhbqhd qsdbqhsjbd qhbdqsbhd qsdqsd qsdqsdqsdsqdqsdqsd")



