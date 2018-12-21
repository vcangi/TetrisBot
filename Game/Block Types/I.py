from block import Block
import numpy as np

class IBlock(Block):
	
	
	def __init__(self,grid):
		self._Block__coord= np.array([[5,0],[5,1],[5,2],[5,3]])
		self._Block__color = 3
		self._Block__orient = 0
		self._Block__rotTF = np.array([[0,0],[0,0],[0,0],[0,0]])
		self._Block__grid = grid
		self._Block__center = np.array([4.5, 1.5])

	def WallKick(self,loc,RotDir):
		transforms = KickLogic[self._Block__orient][RotDir]
		isLegal = False #flag to check if returned position is legal (did we return a new positon instead of the old one)
		total_tf = [0,0]
		for tf in transforms:
			loc += tf 
			total_tf += tf
			if self.isUnoccupied(loc):
				isLegal = True
				return loc,isLegal,total_tf
		return self._Block__coord,isLegal,total_tf

		return coord

KickLogic={ 0:{1:np.array([[0,0],[-2,0], [1,0], [-2,-1],  [1,2]]),
 			  -1:np.array([[0,0],[-1,0], [2,0],  [-1,2], [2,-1]])},

 			1:{1:np.array([[0,0],[-1,0], [2,0],  [1,-2],  [2,-1]]),
 			  -1:np.array([[0,0],[2,0], [-1,0],  [2,1],  [-1,-2]])},

 			2:{1:np.array([[0,0],[1,0], [-2,0],  [-1,2],  [-2,1]]),
 			  -1:np.array([[0,0],[2,0], [-1,0],  [2,1], [-1,-2]])},

 			3:{1:np.array([[0,0],[1,0], [-2,0],  [1,-2], [-2,1]]),
 			  -1:np.array([[0,0],[-2,0], [1,0],  [-2,-1], [1,2]])}
 			} 

