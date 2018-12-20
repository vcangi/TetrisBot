class IBlock(block):
	
	
	def __init__(self,grid):
		self.__coord = np.array([[5,0],[5,1],[5,2],[5,3]])
		self.__color = 3
		self.__orient = 0
		self.__rotTF = np.array([[0,0],[0,0],[0,0],[0,0]])
		self.__grid = grid
		self.__center = np.array([4.5, 1.5])

	def WallKick(self,LR,grid):
		current = self.getRotation()
		transforms = KickLogic[current][LR]

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

