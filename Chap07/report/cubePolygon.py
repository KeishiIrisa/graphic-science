import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
import cubePosition as cp


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for i in range(len(cp.faces)):
        glBegin(GL_POLYGON)
        glColor3dv(cp.colors[i])
        for j in range(len(cp.faces[i])):
            glVertex3dv(cp.vertices[cp.faces[i][j]])
        glEnd()
    glFlush()


def loop():
    glutReshapeFunc(cp.reshape)
    glutDisplayFunc(display)
    glutMainLoop()


def main():
    cp.window()
    cp.init()
    cp.argsInit()
    loop()


if __name__ == '__main__':
    main()
