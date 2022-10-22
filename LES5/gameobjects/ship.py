from typing import List, Tuple
from enum import Enum

class Status(Enum):
    Hit = 0
    Miss = 1
    Hole = 2

class Ship:
    def __init__(self, positions: List[Tuple]):
        # positions is list of tuples
        self.__positions:  List[Tuple] = positions
        self.__sunk: bool = False
        self.__size: int = len(positions)
        self.__hits: List[Tuple] = []

    def get_positions(self) -> List[Tuple]:
        return self.__positions

    def throw_bomb(self, position: Tuple) -> Status:
        if position in self.__positions and position in self.__hits:
            return Status.Hole
        elif position not in self.__positions:
            if position not in self.__hits:
                self.__hits.append(position)
            return Status.Miss
        elif position in self.__positions:
            self.__hits.append(position)
            if len(self.__hits) == self.get_size():
                self.__sunk = True
            return Status.Hit


    def is_sunk(self) -> bool:
        return self.__sunk

    def get_size(self) -> int:
        return self.__size