from kapiteinPiraat import *
from vesselBoatShip import Vessel, Boat, Ship
from civilian import Civilian

if __name__ == '__main__':
    k = Kapitein(naam="Jack Sparrow",
                 quote="This is the day you will always remember as the day you almost caught Captain Jack Sparrow.")
    p1 = Piraat(naam="Black")
    p2 = Piraat(naam="Hack")
    p3 = Piraat(naam="Reck")

    k.get_crew()

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
    # print(len(c.getpassengers()))
    # c.disembark(civ2)
    # print(len(c.getpassengers()))
    # c.disembark(civ1)
    # print(len(c.getpassengers()))
    # c.disembark(civ1)
    print(c)

    d = Ship(name="a", masts=2, acceleration=2, img_path="/IMG/silentmary.jpg")
    print(d)
    d.embark(k)
    print(d)
    d.sail((True, True))
    d.disembark(p1)
    print(d)
    d.disembark(p1)
    print(d)