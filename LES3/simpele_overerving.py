class Person:
    def __init__(self, voornaam:str, achternaam:str) -> None:
        self.voornaam:str = voornaam
        self.achternaam:str = achternaam

    def __str__(self):
        return f"{self.voornaam} {self.achternaam}"
    def shout(self) -> str:
        return "shout"

class Student(Person):
    def __init__(self, firstname:str, achternaam:str, building:str="HBW"):
        self.building = building
        super().__init__(firstname, achternaam)
    def shout(self) -> str:
        return "huiswerk"

class ErasmusStudent(Person):
    def __init__(self, country:str, **kwargs) -> None:
        self.country = country
        super().__init__(**kwargs)

    def shout(self) -> str:
        return super().shout() + " "+ self.country
if __name__ == '__main__':
    s1:Student = Student("john", "connor")
    print("-Student 1-")
    print(s1)
    print(s1.shout())
    s2:ErasmusStudent = ErasmusStudent("USA", voornaam="John", achternaam="Cena")
    print("\n-Student 2-")
    print(s2)
    print(s2.shout())