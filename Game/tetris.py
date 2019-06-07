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
        self.grid = np.zeros((BLOCKX, BLOCKY)) #Array storing 
        self.level = 1    # player leverl   
        self.score = 0    # player score
        self.lastTime = 0 # used for natural(automatic) drop 
        self.up_pressed = False #used to prevent holding key for rotations

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
        self.curr_block = block_arr[block_counter]
        block_counter += 1
        self.curr_block.setGrid(self.grid)
        run = True
        

        while run:
            pygame.time.delay(5)
            self.clock.tick(15)
            

            self.grid = np.zeros((BLOCKX, BLOCKY))
            self.controlBlock()
            gameTime = pygame.time.get_ticks()

            #Cause Automatic Drop due to lack of movement
            if gameTime - self.lastTime  >= 1000/self.level:
                self.naturalDrop()
                self.lastTime = gameTime

            self.updateGrid()
          
            
            self.redrawWindow()
            if self.checkClose():
                break
            #end

    def controlBlock(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.up_pressed == False:
                self.curr_block.getValidRotation(1)
                self.up_pressed = True
                self.lastTime = pygame.time.get_ticks()

            elif not keys[pygame.K_UP]:
                self.up_pressed = False

            if keys[pygame.K_LEFT]:
                self.curr_block.getValidShift(-1, 0)
                self.lastTime = pygame.time.get_ticks()

            if keys[pygame.K_RIGHT]:
                self.curr_block.getValidShift(1, 0)
                self.lastTime = pygame.time.get_ticks()


            if keys[pygame.K_DOWN]:
                self.curr_block.getValidShift(0, 1)
                self.lastTime = pygame.time.get_ticks()


    def naturalDrop(self):
        self.curr_block.getValidShift(0, 1)

    def updateGrid(self):

        coord = self.curr_block.getPosition().astype(int)
        color = self.curr_block.getColor()
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


#           R    G    B
WHITE   = (255, 255, 255)
GRAY    = (185, 185, 185)
BLACK   = (000, 000, 000)
RED     = (155, 000, 000)
LRED    = (175,  20,  20)
GREEN   = (000, 155, 000)
LGREEN  = ( 20, 175,  20)
BLUE    = (000, 000, 155)
LBLUE   = ( 20,  20, 175)
YELLOW  = (155, 155, 000)
LYELLOW = (175, 175,  20)
CYAN    = (000, 255, 255)
LCYAN   = (224, 255, 255)
PURPLE  = (128, 000, 128)
LPURPLE = (238, 130, 238)
ORANGE  = (255, 140, 000)
LORANGE = (255, 165, 000)

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
