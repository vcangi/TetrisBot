class OBlock(block):
	
	def __init__(self,grid):
		self.__coord = np.array([[5,0],[6,0],[5,1],[6,1]])
		self.__color = 6
		self.__orient = 0
		self.__rotTF = np.array([[0,0],[0,0],[0,0],[0,0]])
		self.__center = np.array([5.5, 0.5])
		self.__grid = grid

	def rotate(self):
		return self.__coord

	def WallKick(self):
		return self.__coord
