import numpy as np
import math

class RotMatrix(object):
    def __init__(self, mat):
        self.mat = np.array(mat)

    def multiply(self, o):
        return RotMatrix(self.mat@o.mat)

    def setMatrix(self, offset):
        return (self.mat[0, 0], self.mat[1, 0], self.mat[2, 0], 0,
                self.mat[0, 1], self.mat[1, 1], self.mat[2, 1], 0,
                self.mat[0, 2], self.mat[1, 2], self.mat[2, 2], 0,
                offset[0], offset[1], offset[2], 1)

    def rotAroundAxis(self, angle, x, y, z):
        d = (x*x + y*y + z*z)**0.5
        if d == 0:
            return self.multiply(RotMatrix.identity())
        else:
            x, y, z = (x/d, y/d, z/d)
            angle = angle * math.pi / 180
            s = math.sin(angle)
            c = math.cos(angle)
            return self.multiply(RotMatrix(
                ((c + (1 - c) * x * x, (1 - c) * x * y - s * z, (1 - c) * x * z + s * y),
                ((1 - c) * y * x + s * z, c + (1 - c) * y * y, (1 - c) * y * z - s * x),
                ((1 - c) * z * x - s * y, (1 - c) * z * y + s * x, c + (1 - c) * z * z))
            ))

    @classmethod
    def identity(cls):
        return RotMatrix(((1, 0, 0), (0, 1, 0), (0, 0, 1)))
