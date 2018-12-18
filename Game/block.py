import numpy as np

class Block:

	def __init__(self):
		
		self.__coord  = np.array([[0,0],[0,0],[0,0],[0,0]])
		self.__color  = 0
		self.__orient = 0
		self.__rotTF  = np.array([[0,0],[0,0],[0,0],[0,0]])

	def rotate(self,LR):
		if LR =='CW':
			flip = np.fliplr(self.__rotTF)
			neg = np.multiply(flip,np.array([-1, 1]))
			return neg
		elif LR == 'CCW':
			neg = np.multiply(self.__rotTF,np.array([-1, 1]))
			flip = np.fliplr(neg)
			return flip
		else
			error('Invalid Rotation Direction')

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