import numpy as np


class Block:

	def __init__(self):
		
		self.__coord  = np.array([[0,0],[0,0],[0,0],[0,0]])
		self.__color  = 0
		self.__orient = 0  # 0, 1, 2, 3
		self.__rotTF  = np.array([[0,0],[0,0],[0,0],[0,0]])
		self.__center = np.array([0, 0])

	def rotate(self, final_orient=self.__orient + 1):
		# calculates the theta needed to get to the specified position
		theta = (final_orient - self.__orient) * 90

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
			self.__coord[i, :] = np.round(float_coord[i, :] + self.__center, 0).astype(int)

	def getPosition(self):
		return self.__coord

	def getColor(self):
		return self.__color
	
	def getRotation(self):
		return self.__rotation

	def setPosition(self,coord):
		self.__coord = coord

	def setRotation(self,rotation):
		self.__rotation = rotation

	def wallKick(self,LR,grid):
		current = self.getRotation()
		transforms = KickLogic[current][LR]

		return coord

#Rotation attempts for Wall Kicks (All blocks except I)

KickLogic={ 0:{'Left':np.array([[-1,0],[-1,1],[0,-2],[-1,-2]]),
 			  'Right':np.array([[1,0], [1,1], [0,-2], [1,-2]])},

 			1:{'Left':np.array([[-1,0],[-1,1],[0,-2],[-1,-2]]),
 			  'Right':np.array([[1,0], [1,1], [0,-2], [1,-2]])},

 			2:{'Left':np.array([[-1,0],[-1,1],[0,-2],[-1,-2]]),
 			  'Right':np.array([[1,0], [1,1], [0,-2], [1,-2]])},

 			3:{'Left':np.array([[-1,0],[-1,1],[0,-2],[-1,-2]]),
 			  'Right':np.array([[1,0], [1,1], [0,-2], [1,-2]])}
 			} 