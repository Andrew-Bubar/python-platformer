from settings import *


class Level:

    def __init__(self):
        self.win = pg.display.get_surface()

    def run(self):
        self.win.fill('red')
