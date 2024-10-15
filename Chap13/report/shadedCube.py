from myShadeCanvas import MyShadeCanvas  # myShadeCanvasモジュールのimport
from shadedPolyhedron import ShadedPolyhedron # shadedPolyhedronモジュールのimport

class ShadedCube(ShadedPolyhedron):      # ShadedCubeクラスの定義
  def __init__(self):                    # 初期化メソッド
    '''
    陰影描画立方体を初期化する
    '''
    super().__init__(                    # Polyhedronクラスの初期化メソッド
            ((-1, -1, -1), ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1),
             (-1, -1,  1), ( 1, -1,  1), ( 1,  1,  1), (-1,  1,  1)), # 頂点座標値
            ((1, 2, 6, 5), (2, 3, 7, 6), (4, 5, 6, 7),
             (0, 4, 7, 3), (0, 1, 5, 4), (0, 3, 2, 1)),
            ((0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 5),
             (2, 6), (3, 7), (4, 5), (5, 6), (6, 7), (7, 4)),
            (0.8, 0.8, 0.2, 1.0),        # 拡散成分
            (0.9, 0.9, 0.9, 1.0),        # 鏡面成分
            100)                         # 鏡面反射の減衰係数

def main():                              # main関数
  canvas = MyShadeCanvas()               # MyShadeCanvasの作成
  dispObj = ShadedCube()                 # ShadedCubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
