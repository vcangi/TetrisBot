import numpy as np
import math


class Block:

    def __init__(self, grid):

        self.__coord = np.array([[0, 0], [0, 0], [0, 0], [0, 0]])
        self.__color = 0
        self.__orient = 0  # 0, 1, 2, 3
        self.__center = np.array([0, 0])
        self.__grid = grid

    def getValidRotation(self, rot_dir):
        # rot_dir = 1: CW 90 degree rotation
        # rot_dir = -1: CCW 90 degree rotation
        old_loc = self.__coord
        new_loc = self.rotate(rot_dir)  # Gets potential new rotation location
        new_loc, moved, tf = self.WallKick(new_loc, rot_dir)
        if moved:
            self.__center += tf
            self.__orient = self.setRotation(rot_dir)
            self.__coord = new_loc
        return old_loc

    def getValidShift(self, shift_x, shift_y):
        # shift_dir assumed to be either be +1 or -1
        new_loc = np.add(self.__coord, [shift_x, shift_y]).astype(int)
        if self.isUnoccupied(new_loc):
            self.__coord = new_loc
            self.__center += [shift_x, shift_y]
        return self.__coord

    def WallKick(self, loc, rot_dir):
        transforms = KickLogic[self.__orient][rot_dir]
        # flag to check if returned position is legal (did we return a new position instead of the old one)
        is_legal = False
        total_tf = [0, 0]
        for tf in transforms:
            loc += tf
            total_tf += tf
            if self.isUnoccupied(loc):
                is_legal = True
                return loc, is_legal, total_tf
        return self.__coord, is_legal, total_tf

    def rotate(self, rot_dir=1):
        output = np.zeros(np.shape(self.__coord))

        # calculates the theta needed to get to the specified position
        theta = (rot_dir) * math.pi / 2

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
        return output

    def isUnoccupied(self, loc):
        for pixel in loc:
            x = int(pixel[0])
            y = int(pixel[1])
            if x < 0 or x > 9:
                return False
            elif self.__grid[x, y] != 0:
                return False
        return True

    def getPosition(self):
        return self.__coord

    def getColor(self):
        return self.__color

    def getRotation(self):
        return self.__orient

    def getGrid(self):
       return self.__grid 

    def setPosition(self, coord):
        self.__coord = coord

    def setGrid(self, grid):
        self.__grid = grid

    def setRotation(self, rot_dir):
        rot = 0
        if rot_dir == 1:
            if rot == 3:
                rot = 0
            else:
                rot += 1

        elif rot_dir == -1:
            if rot == 0:
                rot = 3
            else:
                rot -= 1
        else:
            print('Invalid Rotation Direction')
        return rot


# Rotation attempts for Wall Kicks (All blocks except I)

KickLogic = {0: {1: np.array([[0, 0], [-1, 0], [-1, 1], [0, -2], [-1, -2]]),
                 -1: np.array([[0, 0], [1, 0], [1, 1], [0, -2], [1, -2]])},

             1: {1: np.array([[0, 0], [1, 0], [1, -1], [0, 2], [1, 2]]),
                 -1: np.array([[0, 0], [1, 0], [1, -1], [0, 2], [1, 2]])},

             2: {1: np.array([[0, 0], [-1, 0], [-1, 1], [0, -2], [1, -2]]),
                 -1: np.array([[0, 0], [1, 0], [1, 1], [0, -2], [1, -2]])},

             3: {1: np.array([[0, 0], [-1, 0], [-1, -1], [0, 2], [1, 2]]),
                 -1: np.array([[0, 0], [1, 0], [1, -1], [0, 2], [-1, 2]])}
             }
