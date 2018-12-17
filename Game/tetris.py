from block import Block
import pygame
import numpy as np
class tetris:

    def __init__(self):
        self.win = pygame.display.set_mode((WINX,WINY))
        self.clock = pygame.time.Clock()
        self.grid =np.zeros((BLOCKY,BLOCKX))

    def runGame(self):
        while True:
            pygame.time.delay(50)
            self.clock.tick(10)
            self.redrawWindow()

    def redrawWindow(self):
        self.win.fill((0,0,0))
        self.drawGrid()
        pygame.display.update()
    
    def drawGrid(self):
        x = 0
        y = 0
        for l in range(0,BLOCKX):
            x += BLOCKSIZE
            pygame.draw.line(self.win, GRAY, (x,0),(x,GRIDPIXELY))
        for l in range(0,BLOCKY):
            y += BLOCKSIZE
            pygame.draw.line(self.win, GRAY, (0,y),(GRIDPIXELX,y))



WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)

# WIndow Size
WINX = 500
WINY = 500
#Number of blocks in grid
BLOCKX = 10
BLOCKY = 20
BLOCKSIZE = WINY/BLOCKY
#Number of Pixels Grid Takes up
GRIDPIXELX = WINX/2
GRIDPIXELY = WINY


