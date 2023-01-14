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
        self.grid_i =  0

        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.text(0, 100, "Mouse CLICK", col=3)
            print("clicked")

    def update_submarines(self):
        pass

    def draw(self):
        pyxel.cls(0)
        # Create the grid
        while self.grid_i < 10:
            for _ in self.hidden_grid:
                for _ in self.hidden_grid:
                    pyxel.rect(self.grid_x, self.grid_y, 6, 6, 1)
                    self.grid_x += 10
                self.grid_y += 10
                self.grid_x = 0
                self.grid_i += 1
                print(f"On a fini la {self.grid_i} grille")
        self.grid_x = 0
        self.grid_y = 0
        self.grid_i = 0



SubWar()
