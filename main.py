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
        self.hidden_grid = [[' '] for _ in range(10)]  # Create a nested list of 10*10
        self.rect_height = 6
        self.rect_width = 6
        self.space_between = 10
        self.default_grid_x = (SCREEN_WIDTH - (9 * self.space_between + self.rect_width)) / 2
        self.default_grid_y = 0
        self.grid_i = 0
        self.mouse_pos = (pyxel.mouse_x, pyxel.mouse_y)
        self.mouse_click = "NO"
        print(SCREEN_WIDTH / (9 * self.space_between + self.rect_width))
        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            self.mouse_click = "YES"
            print("clicked")
        self.mouse_click = "NO"
        
    def update_submarines(self):
        pass

    def draw(self):
        pyxel.cls(0)
        # Create the grid
        self.draw_grid(col=4)

        pyxel.text(5, 4, f"x = {pyxel.mouse_x} {pyxel.mouse_y}", col=3)

    def draw_grid(self, col):
        x = self.default_grid_x
        y = self.default_grid_y
        self.grid_i = 0
        while self.grid_i < 10:
            for _ in self.hidden_grid:
                for _ in self.hidden_grid:
                    pyxel.rect(x, y, self.rect_width, self.rect_height, col)
                    x += self.space_between
                y += self.space_between
                x = self.default_grid_x
                self.grid_i += 1

SubWar()
