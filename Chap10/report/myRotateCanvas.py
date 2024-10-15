from OpenGL.GLUT import *
from myGLCanvas import MyGLCanvas

class MyRotateCanvas(MyGLCanvas):
    def __init__(self):
        super().__init__()
        self.x, self.y = (-1, -1)
        self.buttondown = -1

    def mouse(self, button, state, x, y):
        if state == GLUT_DOWN:
            self.buttondown = button
            self.x, self.y = (x, y)
        if state == GLUT_UP:
            self.buttondown = -1

    def motion(self, x, y):
        if self.buttondown == GLUT_LEFT_BUTTON:
            thetaX, thetaY = (360*(y-self.y)/self.height, 360*(x-self.x)/self.width)
            self.rotX, self.rotY = (self.rotX+thetaX, self.rotY+thetaY)
            self.x, self.y = (x, y)
            self.display()

    def loop(self):
        glutReshapeFunc(self.reshape)
        glutDisplayFunc(self.display)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutMainLoop()
