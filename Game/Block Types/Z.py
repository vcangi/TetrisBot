class ZBlock(block):
	
	def __init__(self):
		self.__coord = np.array([[4,0],[5,0],[5,1],[6,1]])
		self.__color = 1
		self.__rotTF = np.array([[2,0],[1,1],[0,0],[-1,1]])
		self.__center = np.array([5, 1])