import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class MyGLCanvas(object):
    def __init__(self, width = 500, height = 500):
        self.width, self.height = width, height
        self.fieldOfView, self.near, self.far = (25, 1, 20)
        self.depth, self.rotX, self.rotY, self.rotZ = (-10, 20, -30, 0)
        
        self.objectID = 0
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        glutInitWindowPosition(0, 0)
        glutCreateWindow(b'OpenGL')

    def init(self, dispObj):
        glClearColor(0, 0, 0, 1)
        # glEnable(GL_DEPTH_TEST)
        # glEnable(GL_CULL_FACE)
        self.objectID = glGenLists(1)
        glNewList(self.objectID, GL_COMPILE)
        dispObj.display()
        glEndList()

    def argsInit(self, args):
        if len(args) == 1 and args[0] != '':
            self.fieldOfView = float(args[0])
        if len(args) == 2:
            self.near, self.far = (float(args[0]), float(args[1]))
        if len(args) == 3:
            self.rotX, self.rotY, self.rotZ = (float(args[0]), float(args[1]), float(args[2]))

    def reshape(self, width, height):        
        self.cameraInit(width, height)
        self.positionInit()

    def cameraInit(self, width, height):
        self.width, self.height = width, height
        aspect = width / height
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.fieldOfView, aspect, self.near, self.far)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def positionInit(self):
        glTranslated(0, 0, self.depth)

    def display(self):
        glPushMatrix()
        glRotated(self.rotX, 1, 0, 0)
        glRotated(self.rotY, 0, 1, 0)
        glRotated(self.rotZ, 0, 0, 1)
        self.coreDisplay()
        glPopMatrix()

    def coreDisplay(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glCallList(self.objectID)
        glutSwapBuffers()

    def loop(self):
        glutReshapeFunc(self.reshape)
        glutDisplayFunc(self.display)
        glutMainLoop()


def getArgs():
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = input('FOV / near far / rotX rotY rotZ / [] -> ').split(' ')
    return args
