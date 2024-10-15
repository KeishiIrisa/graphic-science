from OpenGL.GL import *
from myTranslateCanvas import MyTranslateCanvas

class ColorCube(object):
    def __init__(self):
        self.vertices = ((-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
                         (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1))
        self.colors = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
                       (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1))
        self.faces = ((1, 2, 6, 5), (2, 3, 7, 6), (4, 5, 6, 7),
                      (0, 4, 7, 3), (0, 1, 5, 4), (0, 3, 2, 1))

    def display(self):
        glBegin(GL_QUADS)
        for i in range(len(self.faces)):
            for j in range(len(self.faces[i])):
                glColor3dv(self.colors[self.faces[i][j]])
                glVertex3dv(self.vertices[self.faces[i][j]])
        glEnd()


def main():
    canvas = MyTranslateCanvas()
    dispObj = ColorCube()
    canvas.init(dispObj)
    canvas.loop()


if __name__ == '__main__':
    main()
