import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cubePosition as cp

fieldOfView, near, far = (25, 1, 20)
depth, rotX, rotY, rotZ = (-10, 20, -30, 0)


def getArgs():
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = input('FOV / near far / rotX rotY rotZ / [] -> ').split(' ')
    return args


def argsInit(args):
    global fieldOfView, near, far
    global rotX, rotY, rotZ
    if len(args) == 1 and args[0] != '':
        fieldOfView = float(args[0])
    if len(args) == 2:
        near, far = (float(args[0]), float(args[1]))
    if len(args) == 3:
        rotX, rotY, rotZ = (float(args[0]), float(args[1]), float(args[2]))


def reshape(width, height):
    aspect = width / height
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fieldOfView, aspect, near, far)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslated(0, 0, depth)


def display():
    glPushMatrix()
    glRotated(rotX, 1, 0, 0)
    glRotated(rotY, 0, 1, 0)
    glRotated(rotZ, 0, 0, 1)
    cp.display()
    glPopMatrix()


def loop():
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMainLoop()


def main():
    cp.window()
    cp.init()
    argsInit(getArgs())
    loop()


if __name__ == '__main__':
    main()
