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
            if self.checkClose():
                break

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

    def checkClose(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False



WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)
CYAN        = (  0, 255, 255)
LIGHTCYAN   = (224, 255, 255)
PURPLE      = (128,   0, 128)
LIGHTPURPLE = (238, 130, 238)
ORANGE      = (255, 140,   0)
LIGHTORANGE = (255, 165, 0)



# WIndow Size
WINX = 500
WINY = 500
#Number of blocks in grid
BLOCKX = 10
BLOCKY = 20
BLOCKSIZE = WINY/BLOCKY

#Number of Pixels Grid Takes up
GRIDPIXELX = BLOCKSIZE*BLOCKX
GRIDPIXELY = BLOCKSIZE*BLOCKY


