import numpy as np


class Block:

	def __init__(self,grid):
		
		self.__coord  = np.array([[0,0],[0,0],[0,0],[0,0]])
		self.__color  = 0
		self.__orient = 0  # 0, 1, 2, 3
		self.__rotTF  = np.array([[0,0],[0,0],[0,0],[0,0]])
		self.__center = np.array([0, 0])
		self.__grid = grid

	def getValidRotation(self,RotDir):
		#RotDir assumed to be either be +1 or -1
		newLoc = self.rotate(RotDir) #Gets potential new rotaion location
		newLoc,moved = self.WallKick(newLoc,RotDir,grid)
		if moved:
			self.__orient = self.setRotation(RotDir)
			self.__coord  = newLoc
		return self.__coord

	def getValidShift(self,ShiftDir):
		#ShiftDir assumed to be either be +1 or -1
		newLoc = np.add(self.__coord,[ShiftDir,0])
		if self.isUnoccupied(newLoc) and newLoc[:,0] !< 0 and newLoc[:,0] !> 9:
			self.__coord  = newLoc
			self.__center = self.__center
		return self.__coord

	def WallKick(self,loc,RotDir):
		transforms = KickLogic[current][RotDir]
		isLegal = False #flag to check if returned position is legal (did we return a new positon instead of the old one)
		for tf in transforms:
			loc = loc + tf 
			if self.isUnoccupied(loc)
				isLegal = True
				return loc,isLegal
		return self.__coord,isLegal

	def rotate(self, RotDir= 1):
		output = np.zeros(np.shape(self.__coord))

		# calculates the theta needed to get to the specified position
		theta = (RotDir) * 90
		
		# Rotation Matrix
		rot_mat = np.array(((np.cos(theta), -np.sin(theta)), (np.sin(theta), np.cos(theta))))
		float_coord = self.__coord.astype(float)

		# subtracts the center of rotation from each coordinate pair
		for i in range(np.size(float_coord, 0)):
			float_coord[i, :] = float_coord[i, :] - self.__center

		# rotates about the origin
		float_coord = np.matmul(float_coord, rot_mat)

		# translates each point back to the center of rotation
		for i in range(np.size(float_coord, 0)):
			output[i, :] = np.round(float_coord[i, :] + self.__center, 0).astype(int)
		return  output

	def isUnoccupied(self,loc):
		for pixel in loc:
				if self.__grid[pixel] != 0:
					return False
		return True

	def getPosition(self):
		return self.__coord

	def getColor(self):
		return self.__color
	
	def getRotation(self):
		return self.__orient

	def setPosition(self,coord):
		self.__coord = coord

	def setRotation(self,RotDir):
		rot = 0
		if RotDir == 1:
			if rot == 3:
				rot = 0
			else:
				rot += 1
		
		else if RotDir == -1:
			if rot == 0:
				rot = 3
			else:
				rot -= 1
		
		else
			error('Invalid Rotation Direction')
		return rot




#Rotation attempts for Wall Kicks (All blocks except I)

KickLogic={ 0:{1:np.array([[0,0],[-1,0],[-1,1],[0,-2],[-1,-2]]),
 			  -1:np.array([[0,0],[1,0], [1,1], [0,-2], [1,-2]])},

 			1:{1:np.array([[0,0],[1,0], [1,-1],  [0,2],  [1,2]]),
 			  -1:np.array([[0,0],[1,0], [1,-1],  [0,2],  [1,2]])},

 			2:{1:np.array([[0,0],[-1,0],[-1,1],  [0,-2],[1,-2]]),
 			  -1:np.array([[0,0], [1,0], [1,1],  [0,-2], [1,-2]])},

 			3:{1:np.array([[0,0],[-1,0], [-1,-1], [0,2], [1,2]]),
 			  -1:np.array([[0,0], [1,0],  [1,-1], [0,2],[-1,2]])}
 			} 