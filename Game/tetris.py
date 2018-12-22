from block import Block
import pygame
import numpy as np
from Z import ZBlock
from I import IBlock
from J import JBlock
from O import OBlock
from L import LBlock
from T import TBlock
from S import SBlock
import time


class tetris:

    def __init__(self):
        self.win = pygame.display.set_mode((WINX, WINY))
        self.clock = pygame.time.Clock()
        self.grid = np.zeros((BLOCKX, BLOCKY))

    def runGame(self):
        block_counter = 0
        block_arr = np.array([ZBlock(self.grid),
                              IBlock(self.grid),
                              JBlock(self.grid),
                              OBlock(self.grid),
                              LBlock(self.grid),
                              TBlock(self.grid),
                              SBlock(self.grid)])
        np.random.shuffle(block_arr)
        curr_block = block_arr[block_counter]
        block_counter += 1
        curr_block.setGrid(self.grid)
        run = True
        while run:
            pygame.time.delay(5)
            self.clock.tick(15)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()


            self.grid = np.zeros((BLOCKX, BLOCKY))
            self.updateGrid(curr_block)
            # curr_block.getValidShift(1)

            if keys[pygame.K_SPACE]:
                curr_block.getValidRotation(1)

            if keys[pygame.K_LEFT]:
                curr_block.getValidShift(-1, 0)

            if keys[pygame.K_UP]:
                curr_block.getValidShift(0, -1)

            if keys[pygame.K_RIGHT]:
                curr_block.getValidShift(1, 0)

            if keys[pygame.K_DOWN]:
                curr_block.getValidShift(0, 1)

            self.redrawWindow()

            if self.checkClose():
                break

    def updateGrid(self, curr_block):

        coord = curr_block.getPosition().astype(int)
        color = curr_block.getColor()
        for c in coord:
            self.grid[c[0], c[1]] = color


    def redrawWindow(self):
        self.win.fill((50, 50, 50))
        self.DrawBlocks()
        self.drawGridLines()
        pygame.display.update()

    def drawGridLines(self):
        x = 0
        y = 0
        for l in range(0, BLOCKX):
            x += BLOCKSIZE
            pygame.draw.line(self.win, GRAY, (x, 0), (x, GRIDPIXELY))
        for l in range(0, BLOCKY):
            y += BLOCKSIZE
            pygame.draw.line(self.win, GRAY, (0, y), (GRIDPIXELX, y))

    def DrawBlocks(self):
        for x in range(0, (BLOCKX)):
            for y in range(0, (BLOCKY)):
                color = self.grid[x, y]
                xFrom = int(x * BLOCKSIZE)
                yFrom = int(y * BLOCKSIZE)
                pygame.draw.rect(self.win, color_map[color], (xFrom, yFrom, BLOCKSIZE, BLOCKSIZE))

    def checkClose(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False


#               R    G    B
WHITE = (255, 255, 255)
GRAY = (185, 185, 185)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
LIGHTRED = (175, 20, 20)
GREEN = (0, 155, 0)
LIGHTGREEN = (20, 175, 20)
BLUE = (0, 0, 155)
LIGHTBLUE = (20, 20, 175)
YELLOW = (155, 155, 0)
LIGHTYELLOW = (175, 175, 20)
CYAN = (0, 255, 255)
LIGHTCYAN = (224, 255, 255)
PURPLE = (128, 0, 128)
LIGHTPURPLE = (238, 130, 238)
ORANGE = (255, 140, 0)
LIGHTORANGE = (255, 165, 0)

color_map = {0: BLACK,
             1: RED,
             2: GREEN,
             3: CYAN,
             4: ORANGE,
             5: BLUE,
             6: YELLOW,
             7: PURPLE}

# Window Size
WINX = 500
WINY = 500
# Number of blocks in grid
BLOCKX = 10
BLOCKY = 20
BLOCKSIZE = int(WINY / BLOCKY)

# Number of Pixels Grid Takes up
GRIDPIXELX = BLOCKSIZE * BLOCKX
GRIDPIXELY = BLOCKSIZE * BLOCKY
