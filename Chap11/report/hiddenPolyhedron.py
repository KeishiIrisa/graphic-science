from OpenGL.GL import *

class HiddenPolyhedron(object):
    def __init__(self, vertices = (), faces = (), edges = (), colors = ()):
                                            # 初期化メソッド
        '''
        vertices - 頂点座標値, 省略時 空タプル
        faces    - 面の頂点番号列, 省略時 空タプル
        edges    - 稜線の頂点番号列, 省略時 空タプル
        colors   - 面の描画色, 省略時 空タプル
        多面体を初期化する
        '''
        self.vertices, self.faces, self.edges, self.colors = \
                    (vertices, faces, edges, colors)
                                # 頂点座標値, 面の頂点番号列, 稜線の頂点番号列, 面の描画色
        
    def displayFaces(self, face):
        glColor3dv((0, 0, 0))
        glBegin(GL_POLYGON)
        for i in range(len(face)):
            glVertex3dv(self.vertices[face[i]])
        glEnd()
    
    def displayEdges(self, face):
        glColor3dv((1, 1, 0))
        glLineWidth(2.0)
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glLineStipple(1, 0xFFFF)
        glEnable(GL_LINE_STIPPLE)
        glBegin(GL_LINES)
        for i in range(len(face)):
            if i == len(face) - 1:
                glVertex3dv(self.vertices[face[i]])
                glVertex3dv(self.vertices[face[0]])
            else:
                glVertex3dv(self.vertices[face[i]])
                glVertex3dv(self.vertices[face[i + 1]])
        glEnd()
        glDisable(GL_LINE_STIPPLE)

    def display(self):
        for i in range(len(self.faces)):  
            self.displayFaces(self.faces[i])
            self.displayEdges(self.faces[i])
