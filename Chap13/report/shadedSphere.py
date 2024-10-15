from OpenGL.GL import *
from myShadeCanvas import MyShadeCanvas
from shadedSubdivision import ShadedSubdivision, getArgs

class ShadedSphere(ShadedSubdivision):
    def __init__(self, times):
        super().__init__(times)

    def triangle(self, p0, p1, p2):
        glShadeModel(GL_SMOOTH)
        glBegin(GL_POLYGON)
        glNormal3dv(tuple(p0))
        glVertex3dv(tuple(p0))
        glNormal3dv(tuple(p1))
        glVertex3dv(tuple(p1))
        glNormal3dv(tuple(p2))
        glVertex3dv(tuple(p2))
        glEnd()


def main():
    canvas = MyShadeCanvas()
    dispobj = ShadedSphere(getArgs())
    canvas.init(dispobj)
    canvas.loop()


if __name__ == "__main__":
    main()
