from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from myGLCanvas import MyGLCanvas

class MySpinCanvas(MyGLCanvas):
    def __init__(self):
        super().__init__()
        self.x, self.y = self.startX, self.startY = (-1, -1)
        self.buttondown = -1
        self.angle = 0
        self.axisX, self.axisY, self.axisZ = (0, 0, 1)

    def mouse(self, button, state, x, y):
        if state == GLUT_DOWN:
            self.buttondown = button
            self.x, self.y = self.startX, self.startY = (x, y)
        if state == GLUT_UP:
            self.buttondown = -1
            if button == GLUT_LEFT_BUTTON:
                if self.startX == x and self.startY == y:
                    self.angle = 0
                    glutIdleFunc(None)
                else:
                    glutIdleFunc(self.idle)

    def motion(self, x, y):
        deltaX, deltaY = (x-self.x, y-self.y)
        if self.buttondown == GLUT_LEFT_BUTTON:
            SPINRATIO = 50
            self.angle = (deltaX**2 + deltaY**2)**0.5 * SPINRATIO / min(self.width, self.height)
            modelMatrix = glGetDoublev(GL_MODELVIEW_MATRIX)
            projMatrix = glGetDoublev(GL_PROJECTION_MATRIX)
            viewport = glGetIntegerv(GL_VIEWPORT)
            originX, originY, originZ = gluProject(0, 0, 0, modelMatrix, projMatrix, viewport)
            self.axisX, self.axisY, self.axisZ = gluUnProject(originX+deltaY, originY+deltaX, originZ, modelMatrix, projMatrix, viewport)
            self.x, self.y = (x, y)
            self.idle()

    def positionInit(self):
        glTranslated(0, 0, self.depth)
        glRotated(self.rotX, 1, 0, 0)
        glRotated(self.rotY, 0, 1, 0)
        glRotated(self.rotZ, 0, 0, 1)

    def idle(self):
        glRotated(self.angle, self.axisX, self.axisY, self.axisZ)
        self.display()

    def display(self):
        self.coreDisplay()


    def loop(self):
        glutReshapeFunc(self.reshape)
        glutDisplayFunc(self.display)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutIdleFunc(None)
        glutMainLoop()
