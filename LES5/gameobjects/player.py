import LES5.gameobjects.ocean as ocean
from typing import List
class Player:

    def __init__(self, name: str):
        self.name: str = name
        self.__ocean: ocean.Ocean = ocean.Ocean()
        self.__numbers_of_bombs: int = 10
        self.__numbers_of_bombs_left: int = 10

    def has_lost(self) -> bool:
        if not self.__ocean.get_ship().is_sunk() and self.__numbers_of_bombs_left == 0:
            return True
        else:
            return False

    def has_won(self) -> bool:
        return self.__ocean.get_ship().is_sunk()

    def drop_bomb(self, position):
        if self.get_numbers_of_bombs_left() > 0:
            self.__numbers_of_bombs_left -= 1
            return self.__ocean.drop_bomb(position)
        else:
            print("No more bombs!")
            return None

    def get_ocean_grid(self) -> List[List]:
        return self.__ocean.get_grid()

    def get_ocean(self):
        return self.__ocean

    def get_numbers_of_bombs_left(self) -> int:
        return self.__numbers_of_bombs_left
