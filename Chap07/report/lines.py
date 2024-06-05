import sys                               # sysモジュールのimport
from OpenGL.GL import *                  # GLモジュールのimport
from OpenGL.GLU import *                 # GLUモジュールのimport
from OpenGL.GLUT import *                # GLUTモジュールのimport

W, H   = (600, 600)                      # OpenGLウィンドウの幅と高さ
points = ((W/60, H-1), (W/20,  H-1), (W/8,  H-1), (W/4, H-1),
          ( W/2, H-1), ( W-1,  H-1), (W-1,  H/2), (W-1, H/4),
          ( W-1, H/8), ( W-1, H/20), (W-1, H/60)) # 線分の終点，11個

def window(width, height):               # ウィンドウ作成
  '''
  width  - OpenGLウィンドウの幅
  height - OpenGLウィンドウの高さ
  GLUTを初期化して，OpenGLウィンドウを作成する
  '''
  glutInit(sys.argv)                     # GLUTの初期化
  glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE) # 表示モードの指定
  glutInitWindowSize(width, height)      # ウィンドウサイズの指定
  glutInitWindowPosition(0, 0)           # ウィンドウ位置の指定
  glutCreateWindow(b'OpenGL')            # ウィンドウの作成

def init():                              # OpenGLの初期化
  '''
  OpenGLを初期化する
  '''
  glClearColor(1, 1, 1, 1)               # 背景色の設定 (白) 
 
def reshape(width, height):              # ウィンドウのサイズ変更に伴うコールバック関数
  '''
  width  - 変更後のOpenGLウィンドウの幅
  height - 変更後のOpenGLウィンドウの高さ
  ウィンドウサイズ変更に伴う処理を行う
  '''
  glViewport(0, 0, width, height)        # ビューポートの設定
  glMatrixMode(GL_PROJECTION)            # 投影変換行列の設定開始
  glLoadIdentity()                       # 恒等行列での初期化
  gluOrtho2D(0, width-1, 0, height-1)    # 2次元ワールド座標系との対応
  glMatrixMode(GL_MODELVIEW)             # モデル変換行列の設定開始
  glLoadIdentity()                       # 恒等行列での初期化

def display():                           # 描画要求に伴うコールバック関数
  '''
  描画要求に伴う処理を行う (放射状の線を描画する)
  '''
  origin = (0, 0)                        # 線分の始点 (左下隅)
  glClear(GL_COLOR_BUFFER_BIT)           # 背景の消去
  glBegin(GL_LINES)                      # 線分描画の開始
  glColor3d(0, 0, 0)                     # 描画色の設定 (黒)
  for i in range(len(points)):           # 線分描画の反復 (終点の個数分)
    glVertex2dv(origin)                  # 線分の始点
    glVertex2dv(points[i])               # 線分の終点
  glEnd()                                # 線分描画の終了
  glFlush()                              # 描画命令の送信

def loop():                              # コールバック関数の設定とループ起動
  '''
  reshape と displayコールバック関数を設定し，ループを起動する
  '''
  glutReshapeFunc(reshape)               # reshapeコールバック関数の登録
  glutDisplayFunc(display)               # displayコールバック関数の登録
  glutMainLoop()                         # GLUTのメインループ起動

def main():                              # main関数
  window(W, H)                           # ウィンドウの作成
  init()                                 # OpenGLの初期化
  loop()                                 # コールバック関数の設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
