from OpenGL.GL import *                  # GLモジュールのimport

class Polyhedron(object):                # Polyhedronクラスの定義
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

  def display(self):                     # (多面体の) 描画メソッド
    '''
    多面体の描画を行う
    '''
    for i in range(len(self.faces)):     # 多角形描画の反復 (面番号 i)
      glBegin(GL_POLYGON)                # 多角形描画の開始
      glColor3dv(self.colors[i])         # 描画色の指定
      for j in range(len(self.faces[i])): # 面頂点の反復 (頂点番号 j)
        glVertex3dv(self.vertices[self.faces[i][j]]) # 頂点座標値の指定
      glEnd()                            # 多角形描画の終了
