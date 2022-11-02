from kapiteinPiraat import Kapitein
from kapiteinPiraat import Piraat
if __name__ == '__main__':
    k = Kapitein(naam="Jack Sparrow",
                 quote="This is the day you will always remember as the day you almost caught Captain Jack Sparrow.")
    p1 = Piraat(naam="Black")
    p2 = Piraat(naam="Hack")
    p3 = Piraat(naam="Reck")

    k.add_crewmember(p1)
    k.add_crewmember(p2)
    k.add_crewmember(p3)
    k.add_crewmember("p3")

    print(k)
    print(p1)