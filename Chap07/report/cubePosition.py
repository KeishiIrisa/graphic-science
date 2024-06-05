import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


eyex, eyey, eyez = (4, 3, 7)
vertices = ((-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1))
faces = ((1, 2, 6, 5), (2, 3, 7, 6), (4, 5, 6, 7), (0, 4, 7, 3), (0, 1, 5, 4), (0, 3, 2, 1))
colors = ((0, 1, 1), (1, 0, 1), (1, 1, 0), (0, 0.5, 0.5), (0.5, 0, 0.5), (0.5, 0.5, 0))


def window(width = 500, height = 500):
    width
    height
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'OpenGL')


def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)


def argsInit():
    global eyex, eyey, eyez
    if len(sys.argv) > 3:
        args = sys.argv[1:]
    else:
        args = input("eyex eyey eyez or [] -> ").split()
    if len(args) >= 3:
        eyex, eyey, eyez = (float(args[0]), float(args[1]), float(args[2]))


def reshape(width, height):
    width
    height
    global eyex, eyey, eyez
    fieldOfView, near, far = (25, 1, 20)
    aspect = width / height
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fieldOfView, aspect, near, far)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eyex, eyey, eyez, 0, 0, 0, 0, 1, 0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_QUADS)
    for i in range(len(faces)):
        glColor3fv(colors[i])
        for j in range(len(faces[i])):
            glVertex3dv(vertices[faces[i][j]])
    glEnd()
    glFlush()


def loop():
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMainLoop()


def main():
    window()
    init()
    argsInit()
    loop()


if __name__ == "__main__":
    main()
