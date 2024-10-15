from myGLCanvas import MyGLCanvas, getArgs # myGLCanvasモジュールのimport
from polyhedron import Polyhedron        # polyhedronモジュールのimport

class Tetrahedron(Polyhedron):                  # Cubeクラスの定義
  def __init__(self):                    # 初期化メソッド
    '''
    正四面体を初期化する
    '''
    super().__init__(                    # Polyhedronクラスの初期化メソッド
            ((-1, -1, -1),( 1,  1, -1),(1, -1, 1),(-1, 1, 1)), # 頂点座標値
            ((0, 1, 2), (0, 3, 1), (0, 2, 3), (1, 3, 2)),        # 各面の頂点番号列
            ((0, 1), (0, 3), (0, 2), (1, 2), (2, 3), (3, 1)),  # 各稜線の頂点番号列
            ((  0,   1,   1), (  1,   0,   1), (  1,   1,   0), (0, 0, 1)) ) # 各面の描画色

def main():                              # main関数
  canvas = MyGLCanvas()                  # MyGLCanvasの作成
  dispObj = Tetrahedron()                       # Cubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.argsInit(getArgs())             # シェル引数/キーボード入力による文字列の取得
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
