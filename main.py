import pygame
import Tetromino

Tetromino.init()
while True: # game loop
        Tetromino.runGame()
        Tetromino.showTextScreen('Game Over')