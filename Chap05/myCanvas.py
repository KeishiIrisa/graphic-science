from tkinter import *                    # tkinterモジュールのimport
import numpy as np                       # numpyモジュールのimport (npで)

class MyCanvas(object):                  # MyCanvasクラスの定義
  def __init__(self, width = 600, height = 600, xo = 300, yo = 300, r = 2.0):
                                         # 初期化メソッド
    '''
    width, height - canvasの幅と高さ ，省略時 600, 600
    xo, yo        - 描画原点のcanvas (スクリーン) 上の位置 ，省略時 300, 300
    r             - 描画領域 (世界座標系で) の範囲 ，省略時 2.0
    canvasの作成と初期化を行う
    '''
    self.w, self.h = (width, height)     # canvasの幅と高さ
    self.xo, self.yo = (xo, yo)          # 描画原点のcanvas (スクリーン) 上の位置
    self.r = r                           # 描画領域 (世界座標系で) の範囲
    self.s = min(self.w, self.h) / self.r # 描画領域の拡大縮小率
    self.mr = 2                          # marker (制御点用) の半径 
    self.root = Tk()                     # ルートフレームの作成
    self.canvas = Canvas(self.root, width = self.w, height = self.h)
    self.canvas.pack()                   # canvasの作成と配置確定
    
  def bind(self, event, func):           # コールバック関数の登録メソッド
    '''
    event - イベント
    func  - コールバック関数
    イベントに対するコールバック関数を登録する
    '''
    self.canvas.bind(event, func)        # event のコールバック関数

  def mainloop(self):                    # 実行ループの開始メソッド
    '''
    実行ループを開始する
    '''
    self.root.mainloop()                 # ルートフレームの実行ループ開始

  def setOrigin(self, x, y):             # 描画原点の指定メソッド
    '''
    x, y - 描画原点のcanvas (スクリーン) 上の位置
    描画原点の位置を記録する
    '''
    self.xo, self.yo = (x, y)            # 描画原点の位置の記録

  def setRange(self, r):                 # 描画領域の範囲指定メソッド
    '''
    r - 描画領域 (世界座標系で) の範囲
    描画領域の範囲 (長さ) を指定する
    '''
    self.r = r                           # 描画領域 (世界座標系で) の範囲
    self.s = min(self.w, self.h) / self.r # 描画領域の拡大縮小率

  def point(self, x, y):                 # 点データの作成メソッド
    '''
    x, y - スクリーン上の座標値
    対応する世界座標系での点データ (numpy.array) を作成して返す
    '''
    return np.array(((x-self.xo) / self.s, (self.yo-y) / self.s))

  def x(self, p):                        # 点のスクリーン上での x座標計算メソッド
    '''
    p - 世界座標系での点データ
    対応するスクリーン上での x座標値を返す
    '''
    return self.s*p[0] + self.xo         # スクリーン上での x座標

  def y(self, p):                        # 点のスクリーン上での y座標計算メソッド
    '''
    p - 世界座標系での点データ
    対応するスクリーン上での y座標値を返す
    '''
    return -self.s*p[1] + self.yo        # スクリーン上での y座標

  def inside(self, p):                   # 描画領域内かの判定メソッド
    '''
    p - 世界座標系での点データ
    描画領域内にあるか否かを bool型で返す
    '''
    return 0 <= self.x(p) <= self.w and 0 <= self.y(p) <= self.h

  def clear(self):                       # クリアメソッド
    '''
    背景を白長方形でで描画 (クリア) する
    '''
    self.canvas.create_rectangle((2, 2), (self.w+3, self.h+3),
                                 outline='', fill='white')

  def drawCircle(self, c, r, fill='', outline='black'): # 円の描画メソッド
    '''
    c             - 円の中心
    r             - 円の半径
    fill, outline - 内部の色, 輪郭の色，省略時 なし, 黒
    円の円周を描画する
    '''
    dr = self.s * r                      # スクリーン上での半径
    xc, yc = (self.x(c), self.y(c))      # スクリーン上での中心
    self.canvas.create_oval((xc-dr, yc-dr), (xc+dr+1, yc+dr+1),
                            fill=fill, outline=outline) # 円の描画

  def drawPolyline(self, ps, color='black'): # 折れ線の描画メソッド
    '''
    ps    - 折れ線の点列
    color - 描画色，省略時 黒
    点列を結んだ折れ線 (開いた線) を描画する
    '''
    points = []                          # スクリーン上での点列リストの初期化
    for i in range(len(ps)):             # 点の変換の反復
      points.append((self.x(ps[i]), self.y(ps[i]))) # 変換した点の追加
    self.canvas.create_line(tuple(points), fill=color) # 折れ線の描画

  def drawPolygon(self, ps, fill='gray90', outline='black'): # 多角形の描画メソッド
    '''
    ps            - 多角形の点列
    fill, outline - 内部の色, 輪郭の色，省略時 灰色, 黒
    点列を結んだ多角形 (閉じた線と内部) を描画する
    '''
    points = []                          # スクリーン上での点列リストの初期化
    for i in range(len(ps)):             # 点の変換の反復
      points.append((self.x(ps[i]), self.y(ps[i]))) # 変換した点の追加
    self.canvas.create_polygon(tuple(points), fill=fill, outline=outline)
                                         # 多角形の描画

  def drawMarker(self, p, fill='black', outline=''): # markerの描画メソッド
    '''
    p      - markerの描画位置の点
    fill, outline - 内部の色, 輪郭の色，省略時 黒, なし
    指定された位置にmarkerを描画する
    '''
    x, y = (self.x(p), self.y(p))        # スクリーン上での座標
    self.canvas.create_rectangle((x-self.mr, y-self.mr),
                                 (x+self.mr+1, y+self.mr+1),
                                 fill=fill, outline=outline) # markerの描画
