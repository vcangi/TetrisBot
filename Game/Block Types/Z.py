class ZBlock(block):
	
<<<<<<< HEAD
	def __init__(self):
		self.__coord = np.array([[4,0],[5,0],[5,1],[6,1]])
=======
	def __init__(self,grid):
		self.__coord = np.array([[4,0],[0,5],[5,1],[6,1]])
>>>>>>> Added checks for valid block rotations/shifts
		self.__color = 1
		self.__orient = 0
		self.__rotTF = np.array([[2,0],[1,1],[0,0],[-1,1]])
<<<<<<< HEAD
		self.__center = np.array([5, 1])
=======
		self.__grid = grid
>>>>>>> Added checks for valid block rotations/shifts
