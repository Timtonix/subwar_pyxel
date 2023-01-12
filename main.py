import pyxel


class SubWar:
    def __init__(self):
        pyxel.init(160, 120, title="BattleShip")
        self.hidden_grid = [[' '] for _ in range(10)]  # Create a nested list of 10*10
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        for _ in self.hidden_grid:
            for _ in self.hidden_grid:
                pyxel.rect(self.x, self.y, 2, 2, 1)
                self.x += 4
            self.y += 4
            self.x = 0

        pyxel.show()


SubWar()
