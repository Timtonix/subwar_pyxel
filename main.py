import pyxel

"""
List of submarines :

- Ukrainian Tiger : 3 points
- French Nuclear : 4 points
- US Spider*2 : 2 points
- Taiwanese Dragon : 3 points
"""
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

class SubWar:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="BattleShip")
        self.color_grid = [[7 for _ in range(10)] for _ in range(10)]  # Create a nested list of 10*10
        self.gps_grid = [[[''] for _ in range(10)] for _ in range(10)]
        self.rect_height = 6
        self.rect_width = 6
        self.space_between = 10
        self.default_grid_x = (SCREEN_WIDTH - (9 * self.space_between + self.rect_width)) / 2
        self.default_grid_y = (SCREEN_HEIGHT - (9 * self.space_between + self.rect_height)) / 2
        self.grid_i = 0
        self.mouse_pos = (pyxel.mouse_x, pyxel.mouse_y)
        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            grid_length = len(self.color_grid)
            # On compte le nombre de tableaux dans la grid
            for row in range(grid_length):
                for line in range(grid_length):
                    mouse_x = pyxel.mouse_x
                    mouse_y = pyxel.mouse_y
                    dx = self.gps_grid[row][line][0] - pyxel.mouse_x
                    dy = self.gps_grid[row][line][1] - pyxel.mouse_y

                    if dx * dx + dy * dy < self.rect_height * self.rect_width:
                        """
                        Explication du calcul mené ci-dessus :
                        
                        dx: c'est la position x d'un carré moins x de la souris
                        dy: pareil mais avec y
                        
                        PRINT :
                            rect_x 32.0
                            rect_y = 12.0
                            dx = -2.0
                            dy = -2.0
                            mouse_x = 34
                            mouse_y = 14
                            dx * dx + dy * dy = 8.0 -> cela nous donnes un aire dans le carré cliqué, si < 36 c'est que c'est bien dans notre carré !
                            area = 36
                            
                        """
                        print(f"Clicked on {self.gps_grid[row][line][0]} - {self.gps_grid[row][line][1]}")

    def draw_grid(self):
        x = self.default_grid_x
        y = self.default_grid_y
        self.grid_i = 0

        while self.grid_i < 10:
            grid_length = len(self.color_grid)
            for row in range(grid_length):
                for line in range(grid_length):
                    print(self.color_grid[row][line])
                    pyxel.rect(x, y, self.rect_width, self.rect_height, self.color_grid[row][line])
                    self.gps_grid[row][line] = (x, y)
                    x += self.space_between
                y += self.space_between
                x = self.default_grid_x
                self.grid_i += 1

    def draw(self):
        pyxel.cls(0)
        # Create the grid
        self.draw_grid()

        pyxel.text(5, 4, f"x = {pyxel.mouse_x} {pyxel.mouse_y}", col=3)



SubWar()
