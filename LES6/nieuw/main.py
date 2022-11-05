from Kapitein import Kapitein
from Piraat import Piraat
from Ship import Ship
from Boat import Boat
from Civilian import Civilian
if __name__ == '__main__':
   k = Kapitein(naam="spaarow", quote="a")
   a = Piraat(naam="a", quote="a")
   b = Piraat(naam="b", quote="b")
   c = Civilian(name="a")
   k.add_crewmember(a)
   k.add_crewmember(b)
# Piraat en Kapitein
    # k = Kapitein(naam="Jack", quote="asasaas")
    # p1 = Piraat(naam="sdsds")
    # p2 = Piraat(naam="sdsdqsdqsdqsdqsds")
    #
    # k.add_crewmember(a)
    # k.add_crewmember(a)
    # print(len(k.get_crew()))
    # print(k.get_crew())
    # k.add_crewmember(b)
    # k.add_crewmember(b)
    # print(len(k.get_crew()))
    # print(k.get_crew())

# Boot
   # s = Boat(name='a', img_path="../IMG/no_image.jpg", acceleration=25,masts=10)
   # s.embark(b)
   # s.embark(c)
   # s.embark(c)
   # s.embark(c)
   #
   # s.sail((True, False))
   # print(s)

# Ship Kapitein Piraat

   # ship = Ship(name="a", acceleration=5, img_path="../IMG/no_image.jpg", masts=3)
   # ship.embark(a)
   # ship.embark(k)
   # print(ship)
   #
   # k2 = Kapitein(naam="barossa", quote="sdsd")
   # p1 = Piraat(naam="a", quote="a")
   # p2 = Piraat(naam="a", quote="a")
   # p3 = Piraat(naam="a", quote="a")
   # p4 = Piraat(naam="a", quote="a")
   # k2.add_crewmember(p1)
   # k2.add_crewmember(p2)
   # ship.embark(k2)
   # ship.embark(p4)
   # print(ship)
