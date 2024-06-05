import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


eyex, eyey, eyez = (4, 3, 7)
# 立方体の頂点座標
vertices = ((-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1))
# 正四面体の頂点と面と色
tetra_vertices = [vertices[i] for i in [0, 2, 5, 7]]
tetra_faces = ((0, 1, 2), (0, 3, 1), (0, 2, 3), (1, 3, 2))
colors = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0))


def window(width=500, height=500):
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
    glBegin(GL_TRIANGLES)
    for i in range(len(tetra_faces)):
        glColor3fv(colors[i])
        for j in range(3):
            glVertex3dv(tetra_vertices[tetra_faces[i][j]])
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
