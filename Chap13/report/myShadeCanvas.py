from OpenGL.GL import *
from OpenGL.GLUT import *
from myTranslateCanvas import MyTranslateCanvas

class MyShadeCanvas(MyTranslateCanvas):
    def __init__(self):
        super().__init__()
        self.lid, self.pid = (0, 0)
        self.light = (GL_LIGHT0, GL_LIGHT1)
        self.ambient = ((0.1, 0.1, 0.1, 1.0), (0.3, 0.1, 0.1, 1.0))
        self.diffuse = ((1.0, 1.0, 1.0, 1.0), (1.0, 0.1, 0.1, 1.0))
        self.specular = ((0.9, 0.9, 0.9, 1.0), (0.9, 0.2, 0.2, 1.0))
        self.lightPosition = ((5.0, 5.0, 0.0, 1.0), (5.0, 5.0, 0.0, 0.0))

    def init(self, dispObj):
        super().init(dispObj)
        glEnable(GL_LIGHTING)
        glEnable(GL_NORMALIZE)
        for i in range(len(self.light)):
            glLightfv(self.light[i], GL_AMBIENT, self.ambient[i])
            glLightfv(self.light[i], GL_DIFFUSE, self.diffuse[i])
            glLightfv(self.light[i], GL_SPECULAR, self.specular[i])
        glEnable(self.light[self.lid])

    def keyboard(self, key, x, y):
        if key == b'1':
            glDisable(self.light[self.lid])
            self.lid = (self.light[self.lid])
            glEnable(self.light[self.lid])
        elif key == b'p':
            self.lid = (self.pid + 1) % len(self.lightPosition)

        self.display()

    def display(self):
        glLoadIdentity()
        glLightfv(self.light[self.lid], GL_POSITION, self.lightPosition[self.pid])
        glMultMatrixd(self.state.setMatrix(self.offset))
        self.coreDisplay()

    def loop(self):
        glutKeyboardFunc(self.keyboard)
        super().loop()
