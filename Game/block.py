import numpy as np
import math


class Block:

    def __init__(self, grid):

        self.__coord = np.array([[0, 0], [0, 0], [0, 0], [0, 0]])
        self.__color = 0
        self.__orient = 0  # 0, 1, 2, 3
        self.__center = np.array([0, 0])
        self.__grid = grid
        self.__active = True

    def attempt_rotation(self, rotation_direction):
        # rotation_direction = 1: CW 90 degree rotation
        # rotation_direction = -1: CCW 90 degree rotation
        old_coordinates = self.__coord
        new_coordinates = self.rotate(rotation_direction)  # Gets potential new rotation coordinates
        new_coordinates, moved, tf = self.wall_kick(new_coordinates, rotation_direction)
        if moved:
            self.__center += tf
            self.__orient = (self.__orient + rotation_direction) % 4
            self.__coord = new_coordinates
        return old_coordinates

    def attempt_translation(self, x_transform, y_transform):
        new_coordinates = np.add(self.__coord, [x_transform, y_transform]).astype(int)
        translated = False
        if self.is_unoccupied(new_coordinates):
            self.__coord = new_coordinates
            self.__center += [x_transform, y_transform]
            translated = True
        return translated

    def wall_kick(self, coordinates, rotation_direction):
        transforms = KickLogic[self.__orient][rotation_direction]
        # flag to check if returned position is legal (did we return a new position instead of the old one)
        is_legal = False
        total_tf = [0, 0]
        for tf in transforms:
            coordinates += tf
            total_tf += tf
            if self.is_unoccupied(coordinates):
                is_legal = True
                return coordinates, is_legal, total_tf
        return self.__coord, is_legal, total_tf

    def rotate(self, rotation_direction=1):
        output = np.zeros(np.shape(self.__coord))

        # calculates the theta needed to get to the specified position
        theta = rotation_direction * math.pi / 2

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

    def is_unoccupied(self, coordinates):
        for pixel in coordinates:
            x = int(pixel[0])
            y = int(pixel[1])
            if x < 0 or x > 9:
                return False
            if y > 19:
                self.__active = False
                return False
            elif self.__grid[x, y] != 0:
                return False
        return True

    def get_position(self):
        return self.__coord

    def get_color(self):
        return self.__color

    def get_rotation(self):
        return self.__orient

    def get_grid(self):
        return self.__grid 

    def set_position(self, coord):
        self.__coord = coord

    def set_grid(self, grid):
        self.__grid = grid

    def set_activity(self, active):
        self.__active = active

    def is_active(self):
        return self.__active

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
