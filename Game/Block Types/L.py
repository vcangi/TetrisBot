from block import Block
import numpy as np

class LBlock(Block):
	

	def __init__(self,grid):
		self._Block__coord = np.array([[5,0],[5,1],[5,2],[6,2]])
		self._Block__color = 4
		self._Block__orient = 0
		self._Block__rotTF = np.array([[2,0],[1,1],[0,0],[-1,1]])
		self._Block__grid = grid
		self._Block__center = np.array([5, 1])


