import sys

from OpenGL.GL import *


class Fractal(object):
    def __init__(self, dispObj, scale, vecs, times):
        self.primitive, self.scale, self.vecs, self.times = \
            (dispObj, scale, vecs, times)

    def display(self):
        self.drawFractal(self.times)

    def drawFractal(self, t):
        if t > 0:
            for i in range(len(self.vecs)):
                glPushMatrix()
                glTranslated(self.vecs[i][0], self.vecs[i][1], self.vecs[i][2])
                glScaled(self.scale, self.scale, self.scale)
                self.drawFractal(t-1)
                glPopMatrix()
        else:
            self.primitive.display()


def getArgs():
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = input('times [FOV / near far / rotX rotY rotZ] -> ').split(' ')
    return (int(args[0]), args[1:])
