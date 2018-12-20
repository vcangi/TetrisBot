class SBlock(block):
	
	def __init__(self,grid):
		self.__coord = np.array([[5,0],[6,0],[4,1],[5,1]])
		self.__color = 2
		self.__orient = 0
		self.__rotTF = np.array([[0,0],[0,0],[0,0],[0,0]])
<<<<<<< HEAD
		self.__center = np.array([5, 1])
=======
		self.__grid = grid

>>>>>>> Added checks for valid block rotations/shifts
