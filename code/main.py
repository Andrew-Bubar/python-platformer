from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join


class Game:
    def __init__(self):
        pg.init()

        self.window = pg.display.set_mode((w_width, w_height))
        self.curr_lvl = Level()

        self.tmx_map = {0: load_pygame(join('testLevel.tmx'))}
        # join('..', 'TileSets', 'testLevel.tmx')
        print(self.tmx_map)

    def run(self):

        while True:  # game loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.curr_lvl.run()

            pg.display.update()


g = Game()
g.run()
