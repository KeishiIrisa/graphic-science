import sys
import numpy as np
from OpenGL.GL import *
from myShadeCanvas import MyShadeCanvas
from shadedIcosahedron import ShadedIcosahedron


class ShadedSubdivision(ShadedIcosahedron):
    def __init__(self, times):
        super().__init__()
        self.times = times

    def display(self):
        self.material()
        for i in range(len(self.faces)):
            self.subdivide(np.array(self.vertices[self.faces[i][0]]),
                           np.array(self.vertices[self.faces[i][1]]),
                           np.array(self.vertices[self.faces[i][2]]),
                           self.times)

    def subdivide(self, p0, p1, p2, l):
        if l > 0:
            p01 = self.split(p0, p1)
            p12 = self.split(p1, p2)
            p20 = self.split(p2, p0)
            self.subdivide(p0, p01, p20, l-1)
            self.subdivide(p1, p12, p01, l-1)
            self.subdivide(p2, p20, p12, l-1)
            self.subdivide(p01, p12, p20, l-1)
        else:
            self.triangle(p0, p1, p2)

    def split(self, p0, p1):
        mid = p0 + p1
        return mid*self.RCS / (mid@mid)**0.5

    def triangle(self, p0, p1, p2):
        glShadeModel(GL_FLAT)
        glBegin(GL_POLYGON)
        glNormal3dv(tuple(p0+p1+p2))
        glVertex3dv(tuple(p0))
        glVertex3dv(tuple(p1))
        glVertex3dv(tuple(p2))
        glEnd()


def getArgs():
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = input('times -> ').split(" ")
    return int(args[0])


def main():
    canvas = MyShadeCanvas()
    dispobj = ShadedSubdivision(getArgs())
    canvas.init(dispobj)
    canvas.loop()


if __name__ == "__main__":
    main()
