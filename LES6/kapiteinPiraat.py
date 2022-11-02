class Piraat:
    def __init__(self, naam:str, quote:str = "Ahoy!"):
        self.naam = naam
        self.quote = quote
    def get_naam(self):
        return self.naam
    def get_quote(self):
        return self.quote
    def __str__(self):
        output:str = f"Pirate {self.naam} says {self.quote}"
        return output
class Kapitein(Piraat):
    def __init__(self, naam: str, **kwargs):
        super().__init__(naam)
        self.crew = []
    def add_crewmember(self, crewmember):
        if isinstance(crewmember, Piraat):
            i=0
            gevonden=False
            if len(self.crew) > 0:
                while not gevonden & i < len(self.crew):
                    item = self.crew[i]
                    if crewmember == item:
                        gevonden = True
                    i +=1
                    print("lala")
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
        output:str = f"Captain {self.naam} has {len(self.crew)} crewmembers."
        return output
    def get_crew(self):
        return self.crew