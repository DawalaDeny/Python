from typing import List
from random import randint, choice
import LES5.gameobjects.ship as ship
from LES5.gameobjects.ship import Status


class Ocean:
    def __init__(self, dimension = 5):
        self.__dimension = dimension
        # ["." for collumn in range(dimension)] ==> kolommen
        # [kolommen for row in range(dimension)] ==> rijen
        self.__grid: List[List[str]] = [["." for column in range(dimension)] for row in range(dimension)]
        self.__ship: ship = choice([self.__position_ship_vertical(size=3), self.__position_ship_horizontal(size=3)])

    # creatie verticale ship
    def __position_ship_vertical(self, size) -> ship:
        row = randint(0, self.__dimension - size)
        column = randint(0, self.__dimension - 1)

        #een ship maken die een lijst van tuples verwacht.
        positions = []
        for p in range(0, size):
            positions.append((row + p, column))

        return ship.Ship(positions=positions)

    # creatie horizontale ship
    def __position_ship_horizontal(self, size) -> ship:
        row = randint(0, self.__dimension - 1)
        column = randint(0, self.__dimension - size)
        positions = []
        for p in range(0, size):
            positions.append((row, column + p))

        return ship.Ship(positions=positions)

    def get_ship(self) -> ship:
        return self.__ship

    def get_dimension(self):
        return self.__dimension

    def get_grid(self):
        return self.__grid.copy()

    def drop_bomb(self, position):
        #inputcontrole
        if position[0] < self.__dimension and position[1] < self.__dimension:
            if self.__ship.throw_bomb(position=position) == Status.Hit:
                self.__grid[position[0]][position[1]] = "X"
                return Status.Hit
            elif self.__ship.throw_bomb(position=position) == Status.Miss:
                self.__grid[position[0]][position[1]] = "O"
                return Status.Miss
            else:
                return Status.Hole
        else:
            print("Over the edge")
            return None

if __name__ == '__main__':
    ocean = Ocean(dimension=5)
    ocean.drop_bomb((1,3))

    for g in ocean.get_grid():
        print(g)