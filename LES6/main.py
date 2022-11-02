from kapiteinPiraat import *
from vesselBoatShip import Vessel, Boat
from civilian import Civilian

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


    # b = Vessel(name="Vesselke", img_path="IMG/no_image.jpg", acceleration=5, masts=3)
    # b.sail((True, False))
    # print(b.getspeed())
    # b.ShowImage()

    c = Boat(name="aaaa", img_path="/IMG/fishingboat.jpg", acceleration=25, masts=2)
    civ1 = Civilian(name="mens1")
    civ2 = Civilian(name="mens2")
    c.embark(civ1)
    c.embark(civ2)
    c.sail((True,True))
    print(c)


