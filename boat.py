from random import randint


class Boat:
    def __init__(self, ships: int):
        self.bot_grid = [['' for _ in range(10)] for _ in range(10)]
        self.ships = ships

    def place_ships(self) -> list: # Now it just place ships of 1 case
        for ship in range(self.ships):
            ship_row, ship_line = randint(0, 9), randint(0, 9)
            while self.bot_grid[ship_row][ship_line] == 'X':
                ship_row, ship_line = randint(0, 9), randint(0, 9)
            self.bot_grid[ship_row][ship_line] = 'X'
        print(self.bot_grid)

    def is_there_a_boat(self, coordinates: tuple) -> bool:
        # Coordinates accept value between 0 and 9 for the row and line
        if self.bot_grid[coordinates[0]][coordinates[1]]:
            return True
        return False
