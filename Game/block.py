import numpy as np

class Block:

	def __init__(self):
		print('henlo world')
		self.coord = np.array

	def rotate(self):
		print('henlo')

	def getPosition(self):
		return self.coord

	def getColor(self):
		return self.Color

	def setPosition(self,coord):
		self.coord = coord

Z_PIECE_INITIAL	= np.array([[4,0],[0,5],[1,5],[1,6]])
S_PIECE_INITIAL	= np.array([[5,0],[6,0],[4,1],[5,1]])
I_PIECE_INITIAL	= np.array([[5,0],[5,1],[5,2],[5,3]])
L_PIECE_INITIAL	= np.array([[5,0],[5,1],[5,2],[6,2]])
J_PIECE_INITIAL	= np.array([[5,0],[5,1],[4,2],[5,2]])
O_PIECE_INITIAL	= np.array([[5,0],[6,0],[5,1],[6,1]])
T_PIECE_INITIAL	= np.array([[4,0],[5,0],[6,0],[5,1]])

COLOR = {'z':1
		 's':2
		 'i':3
		 'l':4
		 'j':5
		 'o':6
		 't':7}
		 
START = {'z':Z_PIECE_INITIAL
		 's':S_PIECE_INITIAL
		 'i':I_PIECE_INITIAL
		 'l':L_PIECE_INITIAL
		 'j':J_PIECE_INITIAL
		 'o':O_PIECE_INITIAL
		 't':T_PIECE_INITIAL}
