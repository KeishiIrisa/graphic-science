from myGLCanvas import MyGLCanvas, getArgs # myGLCanvasモジュールのimport
from polyhedron import Polyhedron        # polyhedronモジュールのimport

class Octahedron(Polyhedron):                  # Cubeクラスの定義
  def __init__(self):                    # 初期化メソッド
    '''
    正八面体を初期化する
    '''
    sqrt3 = 3**1/2
    super().__init__(                    # Polyhedronクラスの初期化メソッド
            ((0, sqrt3, 0), (-sqrt3, 0, 0), (0, 0, sqrt3), (sqrt3, 0, 0), (0, 0, -sqrt3), (0, -sqrt3, 0)), # 頂点座標値
            ((0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1), (5, 3, 2), (5, 4, 3), (5, 1, 4), (5, 2, 1)),        # 各面の頂点番号列
            ((0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4), (4, 1), (5, 2), (5, 3), (5, 4), (5, 1)),  # 各稜線の頂点番号列
            ((0, 1, 1), (1, 0, 1), (1, 1, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0.5, 0.5), (0.5, 0, 0.5)) ) # 各面の描画色

def main():                              # main関数
  canvas = MyGLCanvas()                  # MyGLCanvasの作成
  dispObj = Octahedron()                       # Cubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.argsInit(getArgs())             # シェル引数/キーボード入力による文字列の取得
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
