from PIL import Image
import time

class Vessel:
    def __init__(self, name: str, masts: int, acceleration: int, img_path: str):
        self.name = name
        self.masts = masts
        self.acceleration = acceleration
        self.img_path = img_path
        self.speed = 0
    def getname(self):
        return self.name

    def getmasts(self):
        return self.masts

    def getacceleration(self):
        return self.acceleration

    def getimg(self):
        return self.img_path

    def getspeed(self):
        return self.speed

    def ShowImage(self):
        image = Image.open(self.img_path)
        image = image.resize((100, 100))
        image.show()
        time.sleep(1)
        image.close()

    def embark(self, passenger):
        pass

    def disembark(self, passenger):
        pass

    # is eerste bool bv. er is wind aanwezig (true) en tweede bool in ons voordeel (true)?
    def sail(self, windstream: tuple[bool, bool]):
            multiplier = 0
            if windstream[0]:
                multiplier += 2
            if not windstream[1]:
                multiplier -= 0.5
            if multiplier < 0:
                multiplier = 0
            self.speed = self.masts * self.acceleration * multiplier
