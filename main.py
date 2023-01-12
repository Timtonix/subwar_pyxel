import pyxel
import random


class SubWar():
    def __init__(self):
        pyxel.init(128, 128, title="BattleShip")
        self.grid = [[' ']*10 for x in range(10)]

    def update(self):
        pass

    def draw(self):
        pass