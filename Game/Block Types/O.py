class OBlock(block):
	
	def __init__(self):
		self.__coord = np.array([[5,0],[6,0],[5,1],[6,1]])
		self.__color = 6
		self.__rotTF = np.array([[0,0],[0,0],[0,0],[0,0]])

	def rotate(self):
		return self.__coord
