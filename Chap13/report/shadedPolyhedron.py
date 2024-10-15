import numpy as np
from OpenGL.GL import *

class ShadedPolyhedron(object):
    def __init__(self, vertices=(), faces=(), edges=(), diffuse=(), specular=(), shininess=0):
        self.vertices, self.faces, self.edges, self.diffuse, self.specular, self.shininess = \
            (vertices, faces, edges, diffuse, specular, shininess)

    def display(self):
        self.material()
        glShadeModel(GL_FLAT)
        for i in range(len(self.faces)):
            glBegin(GL_POLYGON)
            glNormal3dv(normal(self.vertices[self.faces[i][0]],
                               self.vertices[self.faces[i][1]],
                               self.vertices[self.faces[i][2]]))
            for j in range(len(self.faces[i])):
                glVertex3dv(self.vertices[self.faces[i][j]])
            glEnd()

    def material(self):
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, self.diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, self.shininess)

def normal(p0, p1, p2):
    p0, p1, p2 = (np.array(p0), np.array(p1), np.array(p2))
    return tuple(np.cross(p1 - p0, p2 - p0))
