from Kapitein import Kapitein
from Piraat import Piraat
from Ship import Ship
from Boat import Boat
from Civilian import Civilian
from fishingboat import FishingBoat
from rescueboat import RescueBoat
from silentmary import SilentMary
from blackpearl import BlackPearl

if __name__ == '__main__':

  jackSparrow = Kapitein(naam="Jack Sparrow",
                        quote="This is the day you will always remember as the day you almost caught Captain Jack Sparrow!")
  barbossa = Kapitein(naam="Barbossa", quote="You Best Start Believin' In Ghost Stories... You're in one!")
  salazar = Kapitein(naam="Salazar", quote="My very dead men, the sea is ours! It's time to hunt a pirate!")

  print(jackSparrow)
  print(barbossa)
  print(salazar)
  print()

  gibbs = Piraat("Joshamee Gibs")
  will = Piraat("Will Turner")
  elizabeth = Piraat("Elizabeth Swann")

  print(gibbs)
  print(will)
  print(elizabeth)
  print()

  bootstrap = Piraat("Bootstrap Bill Turner")
  pintel = Piraat("Pintel")
  ragetti = Piraat("Ragetti")

  print(bootstrap)
  print(pintel)
  print(ragetti)
  print()

  silentMary = SilentMary(img_path="../IMG/silentmary.jpg", acceleration=3, name="Silent Mary")
  blackPearl = BlackPearl(img_path="../IMG/blackpearl.jpg", acceleration=3, name="Black Pearl")
  fishingBoat = FishingBoat(img_path="../IMG/fishingboat.jpg", acceleration=3, name="Fishing Boat")
  rescueBoat = RescueBoat(name="rescueboat", acceleration=3)

  print(silentMary)
  print(blackPearl)
  print(fishingBoat)
  print(rescueBoat)
  print()

  silentMary.embark(salazar)
  print(silentMary)
  silentMary.sail((True, True))

  blackPearl.embark(jackSparrow)
  jackSparrow.add_crewmember(gibbs)
  barbossa.add_crewmember(bootstrap)
  barbossa.add_crewmember(pintel)
  blackPearl.embark(barbossa)

  print(blackPearl)
  print(rescueBoat)
  print(fishingBoat)
  print()

  blackPearl.sail((True, True))
  blackPearl.disembark()
  blackPearl.sail((True, True))
  print()

  rescueBoat.embark(will)
  rescueBoat.embark(elizabeth)
  print(rescueBoat)
  rescueBoat.sail((True, True))
  print(rescueBoat)
  rescueBoat.disembark(elizabeth)
  # print(rescueBoat)
  rescueBoat.disembark(ragetti)
  rescueBoat.disembark(will)
  # print(rescueBoat)
  print()

  amberHeard = Civilian("Amber Heard")
  print(amberHeard)
  blackPearl.embark(amberHeard)
  fishingBoat.embark(amberHeard)
  print(fishingBoat)

  silentMary.ShowImage()
  blackPearl.ShowImage()
  fishingBoat.ShowImage()
  rescueBoat.ShowImage()



 # k = Kapitein(naam="spaarow", quote="a")
   # a = Piraat(naam="a", quote="a")
   # b = Piraat(naam="b", quote="b")
   # c = Civilian(name="a")
   # k.add_crewmember(a)
   # k.add_crewmember(b)

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
   # s.disembark()
   # print(s.getpassengers())
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
   # k2.add_crewmember(p3)
   # ship.embark(k2)
   # ship.embark(p4)
   # print(ship)
   # ship.disembark(p1)
   # ship.disembark(p1)
   # ship.disembark(p2)
   # ship.disembark(p2)
   # print(ship)