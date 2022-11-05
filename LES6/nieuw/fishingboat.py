from Boat import Boat
class FishingBoat(Boat):
    def __init__(self, name: str, acceleration: int, img_path: str = "../IMG/no_image.jpg"):
        super().__init__(name, acceleration, img_path)

