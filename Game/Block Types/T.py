from block import Block
import numpy as np


class TBlock(Block):

    def __init__(self, grid):
        self._Block__coord = np.array([[4, 0], [5, 0], [6, 0], [5, 1]])
        self._Block__color = 7
        self._Block__orient = 0
        self._Block__grid = grid
        self._Block__center = np.array([5, 0])
        self._Block__active = True
