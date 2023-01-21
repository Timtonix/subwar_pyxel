import pyxel
import boat
"""
List of submarines :

- Ukrainian Tiger : 3 points
- French Nuclear : 4 points
- US Spider*2 : 2 points
- Taiwanese Dragon : 3 points
"""
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 160


class SubWar:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="BattleShip")
        self.color_grid = [[7 for _ in range(10)] for _ in range(10)]  # Create a nested list of 10*10
        self.gps_grid = [[0 for _ in range(10)] for _ in range(10)]
        self.circ_radius = 4
        self.space_between = 11
        self.default_grid_x = (SCREEN_WIDTH - (9 * self.space_between + self.circ_radius)) / 2
        self.default_grid_y = (SCREEN_HEIGHT - (9 * self.space_between + self.circ_radius)) / 2
        self.mouse_pos = (pyxel.mouse_x, pyxel.mouse_y)
        pyxel.mouse(True)

        # Create boats
        self.ships = boat.Boat(5)
        self.ships.place_ships()

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

                    if dx * dx + dy * dy < self.circ_radius * self.circ_radius:
                        """
                        Explication du calcul mené ci-dessus :
                        
                        dx: c'est la position x d'un carré moins x de la souris -
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
                        if self.ships.is_there_a_boat((row, line)):
                            self.color_grid[row][line] = 8  # Rouge
                        else:
                            self.color_grid[row][line] = 12  # Bleu
                            print(f"Clicked on {self.gps_grid[row][line][0]} - {self.gps_grid[row][line][1]}")

    def draw_grid(self):
        x = self.default_grid_x
        y = self.default_grid_y
        grid_length = len(self.color_grid)
        for row in range(grid_length):
            for line in range(grid_length):
                pyxel.circ(x, y, self.circ_radius, self.color_grid[row][line])
                self.gps_grid[row][line] = (x, y)
                x += self.space_between
            y += self.space_between
            x = self.default_grid_x

    def draw(self):
        pyxel.cls(0)
        if self.ships.remaining_boat() == 0:
            pyxel.text(self.default_grid_x, self.default_grid_y, "YOU WIN", col=8)
        else:
            # Create the grid
            self.draw_grid()
            pyxel.text(5, 4, f"Remaining Boat : {int(self.ships.remaining_boat())}", 3)


SubWar()
