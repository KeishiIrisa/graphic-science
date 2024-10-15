from myGLCanvas import MyGLCanvas, getArgs # myGLCanvasモジュールのimport
from polyhedron import Polyhedron        # polyhedronモジュールのimport

class Dodecahedron(Polyhedron):                  # Cubeクラスの定義
  def __init__(self):                    # 初期化メソッド
    '''
    正十二面体を初期化する
    '''
    phi = (1 + 5**0.5) / 2


    vertices = [
        [1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
        [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1],
        [1/phi, phi, 0], [1/phi, -phi, 0], [-1/phi, phi, 0], [-1/phi, -phi, 0],
        [0, 1/phi, phi], [0, -1/phi, phi], [0, 1/phi, -phi], [0, -1/phi, -phi],
        [phi, 0, 1/phi], [phi, 0, -1/phi], [-phi, 0, 1/phi], [-phi, 0, -1/phi]
    ]

    faces = [
        (0, 8, 10, 4, 12), (0, 12, 13, 2, 16), (0, 16, 17, 1, 8),
        (1, 14, 5, 10, 8), (1, 17, 3, 15, 14), (15, 3, 9, 11, 7),
        (9, 2, 13, 6, 11), (6, 13, 12, 4, 18), (18, 19, 7, 11, 6),
        (18, 4, 10, 5, 19), (5, 14, 15, 7, 19), (17, 16, 2, 9, 3)
    ]

    edges = [
      (0, 8), (8, 10), (10, 4), (4, 12), (12, 0),
      (0, 16), (16, 17), (17, 1), (1, 8), (12, 13),
      (13, 2), (2, 16), (17, 3), (3, 9), (9, 2),
      (13, 6), (6, 18), (18, 4), (6, 11), (11, 9),
      (11, 7), (7, 15), (15, 3), (18, 19), (19, 5),
      (5, 14), (14, 15), (1, 14), (10, 5), (19, 7)
    ]

    colors = [
        (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0),
        (1, 0, 1), (0, 1, 1), (0.5, 0.5, 0), (0.5, 0, 0.5),
        (0, 0.5, 0.5), (0.5, 0.5, 0.5), (0.75, 0.25, 0.25), (0.25, 0.75, 0.75)
    ]

    super().__init__(vertices, faces, edges, colors)

def main():                              # main関数
  canvas = MyGLCanvas()                  # MyGLCanvasの作成
  dispObj = Dodecahedron()                       # Cubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.argsInit(getArgs())             # シェル引数/キーボード入力による文字列の取得
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
