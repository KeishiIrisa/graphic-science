import math                              # mathモジュールのimport

class Quaternion(object):                # Quaternionクラスの定義
  def __init__(self, s, x, y, z):        # 初期化メソッド
    '''
    s, x, y, z - 四元数の成分
    四元数を初期化する
    '''
    self.s, self.x, self.y, self.z = (s, x, y, z) # 四元数の成分を格納する

  def multiply(self, o):                 # 四元数の積メソッド
    '''
    o - 四元数
    自分自身と oとの積を計算して新たな四元数を返す
    '''
    ns = self.s*o.s - self.x*o.x - self.y*o.y - self.z*o.z
    nx = self.s*o.x + self.x*o.s + self.y*o.z - self.z*o.y
    ny = self.s*o.y + self.y*o.s + self.z*o.x - self.x*o.z
    nz = self.s*o.z + self.z*o.s + self.x*o.y - self.y*o.x
    return Quaternion(ns, nx, ny, nz)    # 四元数の積を返す

  def setMatrix(self, offset):           # OpenGL変換行列の生成メソッド
    '''
    offset - 平行移動ベクトル
    自分自身とoffsetを組合せたアフィン変換行列をOpenGLの配列に格納する
    '''
    s, x, y, z = (self.s, self.x, self.y, self.z) # 自分自身の四元数の成分
    d = s*s + x*x + y*y + z*z            # 自分自身の大きさの計算
    return (1-2*(y*y+z*z)/d,   2*(x*y+s*z)/d,   2*(x*z-s*y)/d, 0,
              2*(x*y-s*z)/d, 1-2*(x*x+z*z)/d,   2*(y*z+s*x)/d, 0,
              2*(x*z+s*y)/d,   2*(y*z-s*x)/d, 1-2*(x*x+y*y)/d, 0,
                  offset[0],       offset[1],       offset[2], 1)
                        # 自分自身を回転行列に変換し，offsetと組合せて，長さ16の配列で返す

  def rotAroundAxis(self, angle, x, y, z): # 回転メソッド
    '''
    angle   - 回転角度 (単位: degree)
    x, y, z - 回転軸のx,y,z成分
    自分自身の四元数(=姿勢)を回転した新しい四元数(=姿勢)を計算して返す
    '''
    d = (x*x + y*y + z*z)**0.5           # 回転軸ベクトルのノルム
    if d == 0:                           # 回転軸ベクトルが零ベクトルの場合
      return self.multiply(Quaternion.identity()) # 自分自身と同じ四元数を返す
    else:                                # 回転軸ベクトルが零ベクトルでない場合
      angle = angle * math.pi / 180      # 回転角度をradian単位に変換
      r = math.sin(angle/2) / d          # 四元数のベクトル成分の係数
      return self.multiply(Quaternion(math.cos(angle/2), r*x, r*y, r*z))
                                         # 自分自身と回転行列の積を返す
  @classmethod                           # クラスメソッド
  def identity(cls):                     # 単位元(恒等四元数)の生成メソッド
    '''
    恒等四元数を作り，単位元として返す
    '''
    return Quaternion(1, 0, 0, 0)        # 単位元を返す
