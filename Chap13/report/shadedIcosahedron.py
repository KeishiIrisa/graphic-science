from myShadeCanvas import MyShadeCanvas  # myShadeCanvasモジュールのimport
from shadedPolyhedron import ShadedPolyhedron # shadedPolyhedronモジュールのimport

class ShadedIcosahedron(ShadedPolyhedron): # ShadedIcosahedronクラスの定義
  def __init__(self):                    # 初期化メソッド
    '''
    陰影描画正20面体を初期化する
    '''
    PHI = (1 + 5**0.5) / 2               # 黄金比
    INP = 1 / PHI                        # 黄金比の逆数
    self.RCS = (PHI * 5**0.5)**0.5       # 外接球の半径 (細分割に利用)
    super().__init__(                    # Polyhedronクラスの初期化メソッド
      ((   0,    1,  PHI), (   0,   -1,  PHI), (   0,   -1, -PHI),
       (   0,    1, -PHI), ( PHI,    0,    1), ( PHI,    0,   -1),
       (-PHI,    0,   -1), (-PHI,    0,    1), (   1,  PHI,    0),
       (  -1,  PHI,    0), (  -1, -PHI,    0), (   1, -PHI,    0)), # 頂点座標値
      ((0,  1,  4), (0,  4,  8), (0,  8,  9), (0,  9,  7), (0,  7,  1),
       (1, 10, 11), (1, 11,  4), (4, 11,  5), (4,  5,  8), (8,  5,  3),
       (8,  3,  9), (9,  3,  6), (9,  6,  7), (7,  6, 10), (7, 10,  1),
       (2, 10,  6), (2,  6,  3), (2,  3,  5), (2,  5, 11), (2, 11, 10)),
                                         # 各面の頂点番号列
      (0.8, 0.3, 0.8, 1.0),              # 拡散成分
      (0.9, 0.9, 0.9, 1.0),              # 鏡面成分
      100)                               # 鏡面反射の減衰係数

def main():                              # main関数
  canvas = MyShadeCanvas()               # MyShadeCanvasの作成
  dispObj = ShadedIcosahedron()          # ShadedIcosahedronオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
