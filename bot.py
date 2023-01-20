import random
from random import randint


class Bot:
    """
    Boat placement :
    - Create a nested List with B for boat
        [[[''], [''], [''], [''], [''], [''], [''], [''], [''], ['']],
        [[''], [''], [''], [''], [''], [''], [''], ['B'], ['B'], ['']],
        [[''], [''], [''], ['B'], [''], [''], [''], [''], [''], ['']],
        [[''], [''], [''], ['B'], [''], [''], [''], [''], [''], ['']],
        [[''], [''], [''], ['B'], [''], [''], [''], [''], [''], ['']],
        [[''], ['B'], [''], [''], [''], [''], [''], [''], [''], ['']],
        [[''], ['B'], [''], [''], [''], [''], [''], [''], [''], ['']],
        [[''], ['B'], [''], [''], [''], ['B'], ['B'], ['B'], [''], ['']],
        [[''], ['B'], [''], [''], [''], [''], [''], [''], [''], ['']],
        [[''], [''], [''], [''], [''], [''], [''], [''], [''], ['']]]
    - 1x 2 boat
    - 2x 3 boat
    - 1x 4 boat
    """
    def __init__(self, ships: tuple):
        self.bot_grid = [['' for _ in range(10)] for _ in range(10)]
        self.ships = ships

    def place_ships(self) -> list:
        test_ships = (2, 3, 3, 4)
        grid_length = len(self.bot_grid)
        tuple_length = len(test_ships)
        for ship_length in range(tuple_length): # Donne la longueur du bateau -> 2, 3, 4...
            print(test_ships[ship_length])
            direction_ud = random.choice(["up", "down", "left", "right"])
            match direction_ud:
                case "up":
                    ship_row, ship_line = randint(0, 9 - test_ships[ship_length]), randint(0, 9)
                case"down":
                    ship_row, ship_line = randint(0 + test_ships[ship_length], 9), randint(0, 9)
                case "left":
                    ship_row, ship_line = randint(0, 9), randint(0 + test_ships[ship_length], 9)
                case "right":
                    ship_row, ship_line = randint(0, 9), randint(0, 9 - test_ships[ship_length])

            self.bot_grid[ship_row][ship_line] = 'B'
            for i in range(test_ships[ship_length] - 1):
                print(f"boat number = {ship_length}, length = {test_ships[ship_length]}, i = {i}, direction = {direction_ud}")
                match direction_ud:
                    case "up":
                        ship_row += 1
                        self.bot_grid[ship_row][ship_line] = 'B'
                    case "down":
                        ship_row -= 1
                        self.bot_grid[ship_row][ship_line] = 'B'
                    case "left":
                        ship_line -= 1
                        self.bot_grid[ship_row][ship_line] = 'B'
                    case "right":
                        ship_line += 1
                        self.bot_grid[ship_row][ship_line] = 'B'

        print(self.bot_grid)
