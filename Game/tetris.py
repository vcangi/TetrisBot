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


class Tetris:

    def __init__(self):
        self.win = pygame.display.set_mode((WIN_X_DIM, WIN_Y_DIM))
        self.clock = pygame.time.Clock()
        self.grid = np.zeros((GRID_X_DIM, GRID_Y_DIM)) #Array storing 
        self.level = 1    # player leverl   
        self.score = 0    # player score
        self.lastTime = 0 # used for natural(automatic) drop 
        self.up_held = False  # used to prevent holding key for rotations

    
        self.block_counter = 0
        self.block_bag = np.array([ZBlock(self.grid),
                              IBlock(self.grid),
                              JBlock(self.grid),
                              OBlock(self.grid),
                              LBlock(self.grid),
                              TBlock(self.grid),
                              SBlock(self.grid)])
        np.random.shuffle(self.block_bag)
        self.curr_block = self.block_bag[self.block_counter]

        self.block_counter += 1
        self.curr_block.set_grid(self.grid)
    
    def run_game(self):
        run = True
        

        while run:
            pygame.time.delay(5)
            self.clock.tick(15)
            

            gameTime = pygame.time.get_ticks()
            if self.block_counter == 0:
                np.random.shuffle(self.block_bag)

            if self.curr_block.is_active() is False:
                self.curr_block = self.block_bag[self.block_counter]
                self.block_counter = (self.block_counter + 1) % len(self.block_bag)
                self.curr_block.set_grid(self.grid)
            
            self.clear_current_block()
            self.control_block()
            #Cause Automatic Drop due to lack of movement
            if gameTime - self.lastTime  >= 1000/self.level:
                self.natural_drop()
                self.lastTime = gameTime

            self.update_grid()
            self.redraw_window()
              
              
            if self.check_close():
                  break
            #end

    def control_block(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.up_held is False:
            self.curr_block.attempt_rotation(1)
            self.up_held = True
            self.lastTime = pygame.time.get_ticks()

        elif not keys[pygame.K_UP]:
            self.up_held = False

        if keys[pygame.K_LEFT]:
            self.curr_block.attempt_translation(-1, 0)
            self.lastTime = pygame.time.get_ticks()

        if keys[pygame.K_RIGHT]:
            self.curr_block.attempt_translation(1, 0)
            self.lastTime = pygame.time.get_ticks()


        if keys[pygame.K_DOWN]:
            self.curr_block.attempt_translation(0, 1)
            self.lastTime = pygame.time.get_ticks()


    def natural_drop(self):
        self.curr_block.attempt_translation(0, 1)

    def update_grid(self):

        coord = self.curr_block.get_position().astype(int)
        color = self.curr_block.get_color()
        for c in coord:
            self.grid[c[0], c[1]] = color

    def clear_current_block(self):
        coord = self.curr_block.get_position().astype(int)
        for c in coord:
            self.grid[c[0], c[1]] = 0

    def redraw_window(self):
        self.win.fill((50, 50, 50))
        self.draw_blocks()
        self.draw_grid_lines()
        pygame.display.update()

    def draw_grid_lines(self):
        x = 0
        y = 0
        for l in range(0, GRID_X_DIM):
            x += UNIT_SIZE
            pygame.draw.line(self.win, GRAY, (x, 0), (x, GRID_Y_PIXELS))
        for l in range(0, GRID_Y_DIM):
            y += UNIT_SIZE
            pygame.draw.line(self.win, GRAY, (0, y), (GRID_X_PIXELS, y))

    def draw_blocks(self):
        for x in range(0, GRID_X_DIM):
            for y in range(0, GRID_Y_DIM):
                color = self.grid[x, y]
                #  block_x and block_y refer to the top left pixel coordinates of the block
                block_x = int(x * UNIT_SIZE)
                block_y = int(y * UNIT_SIZE)
                pygame.draw.rect(self.win, color_map[color], (block_x, block_y, UNIT_SIZE, UNIT_SIZE))

    def check_close(self):
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
WIN_X_DIM = 500
WIN_Y_DIM = 500

# Grid dimensions
GRID_X_DIM = 10
GRID_Y_DIM = 20
UNIT_SIZE = int(WIN_Y_DIM / GRID_Y_DIM)  # Number of pixels per grid unit

# Number of Pixels Grid Takes up
GRID_X_PIXELS = UNIT_SIZE * GRID_X_DIM
GRID_Y_PIXELS = UNIT_SIZE * GRID_Y_DIM