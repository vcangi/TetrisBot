class JBlock(block):
	
<<<<<<< HEAD
	def __init__(self):
		self.__coord  = np.array([[5,0],[5,1],[4,2],[5,2]])
		self.__color  = 5
		self.__rotTF  = np.array([[2,0],[1,1],[0,0],[-1,1]])
		self.__center = np.array([5, 1])
=======
	def __init__(self,grid):
		self.__coord = np.array([[5,0],[5,1],[4,2],[5,2]])
		self.__color = 5
		self.__orient = 0
		self.__rotTF = np.array([[2,0],[1,1],[0,0],[-1,1]])
		self.__grid = grid
>>>>>>> Added checks for valid block rotations/shifts
