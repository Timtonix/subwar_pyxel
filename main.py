import pyxel

"""
List of submarines :

- Ukrainian Tiger : 3 points
- French Nuclear : 4 points
- US Spider*2 : 2 points
- Taiwanese Dragon : 3 points
"""


class SubWar:
    def __init__(self):
        pyxel.init(160, 120, title="BattleShip")
        self.hidden_grid = [[' '] for _ in range(10)]  # Create a nested list of 10*10
        self.grid_x = 0
        self.grid_y = 0

        #

        pyxel.run(self.update, self.draw)

    def update(self):
        pass


    def update_submarines(self):
        pass


    def draw(self):
        pyxel.cls(0)

        # Create the grid
        for _ in self.hidden_grid:
            for _ in self.hidden_grid:
                pyxel.rect(self.grid_x, self.grid_y, 6, 6, 1)
                self.grid_x += 10
            self.grid_y += 10
            self.grid_x = 0

        pyxel.show()


SubWar()
