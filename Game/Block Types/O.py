from block import Block
import numpy as np


class OBlock(Block):

    def __init__(self, grid):
        self._Block__coord = np.array([[4, 0], [5, 0], [4, 1], [5, 1]])
        self._Block__color = 6
        self._Block__orient = 0
        self._Block__grid = grid
        self._Block__center = np.array([4.5, 0.5])
        self._Block__active = True

    def WallKick(self, loc, RotDir):
        return self._Block__coord, True, [0, 0]