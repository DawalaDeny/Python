
from gameobjects.player import Player
from gameobjects.ocean import Ocean
from typing import List

def create_ocean(ocean: Ocean):
    header: List[str] = ["\t"]
    for h in range(ocean.get_dimension()):
        header.append(str(h) + "\t")
    print("".join(header))
    for x in range(len(header) -1):
        row = header[x+1]
        for y in range(len(header) -1):
            row += str(ocean.get_grid()[x][y]) + "\t"
        print("".join(row))

if __name__ == '__main__':
    print("Welcome to Battle")
    name: str = input("Whats your name: ")
    player: Player = Player(name=name)
    print("You have to bomb a ship of three positions long in a square sea of 5 to 5")

    while not player.has_won() and not player.has_lost():
        print(f"{player}, you have {player.get_numbers_of_bombs_left()} bombs left")
        print(f"Hint: {player.get_ocean().get_ship().get_positions()}")
        row: int = int(input("What's the row number of your next bomb:"))
        col: int = int(input("What's the col number of your next bomb:"))
        result = player.drop_bomb((row, col))
        print(str(result))

        create_ocean(player.get_ocean())

    if player.has_won():
        print("Hooray")
    elif player.has_lost():
        print("Try again...")


