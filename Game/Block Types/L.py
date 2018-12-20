class LBlock(block):
	

	def __init__(self,grid):
		self.__coord = np.array([[4,0],[5,1],[5,2],[6,2]])
		self.__color = 4
		self.__orient = 0
		self.__rotTF = np.array([[2,0],[1,1],[0,0],[-1,1]])
		self.__grid = grid
		self.__center = np.array([5, 1])


