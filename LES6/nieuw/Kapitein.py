from Piraat import Piraat
class Kapitein(Piraat):
    def __init__(self, naam: str, quote: str = "Ahoy"):
        self.crew = []
        super().__init__(naam, quote)
    def add_crewmember(self, crewmember):
        if isinstance(crewmember, Piraat):
            i=0
            gevonden=False
            if len(self.crew) > 0:
                while i < len(self.crew) and gevonden == False:
                    item = self.crew[i]
                    if crewmember == item:
                        gevonden = True
                    i +=1
                if not gevonden:
                    self.crew.append(crewmember)
                else:
                    print("Crewmember is already present")
            else:
                self.crew.append(crewmember)
        else:
            print("Can only add pirates")

    def remove_crewmember(self, crewmember):
        if isinstance(crewmember, Piraat):
            i = 0
            gevonden = False
            while gevonden == False & i < len(self.crew):
                item = self.crew[i]
                if crewmember == item:
                    gevonden = True
                i += 1
            if gevonden:
                self.crew.remove(crewmember)
            else:
                print("Crewmember is already present")
        else:
            print("Can only remove pirates")

    def __str__(self):
        output:str = f"Captain {self.naam} has {len(self.crew)} crewmembers says: {self.quote}"
        return output
    def get_crew(self) -> list:
        return self.crew
