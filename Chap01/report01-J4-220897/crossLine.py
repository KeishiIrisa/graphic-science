from tkinter import *                    # tkinterモジュールのimport
#from tkinter import Tk, Canvas           # tkinterモジュールからTk,Canvasのimport
import sys                               # sysモジュールのimport

W, H = (400, 300)                        # canvasの幅と高さ

def display(canvas, msg):                # 描画関数
  '''
  canvas - 描画するcanvas
  2本の線分と文字列を描画する
  '''
  canvas.create_line((0, 0), (W-1, H-1), fill = 'blue') # 線分の描画 (左上→右下)
  canvas.create_line((0, H-1), (W-1, 0), fill = 'green') # 線分の描画 (左下→右上)
  canvas.create_text((W/2, H/2), text=msg) # 文字列の描画 (canvas中央)

def main():                              # main関数
  if len(sys.argv) > 1:                  # シェル引数がある場合
    msg = sys.argv[1]                    # 第1引数を頂点数の文字列
  else:                                  # シェル引数がない場合
    msg = input('message -> ')           # 描画する文字列を入力
  root = Tk()                            # ルートフレームの作成
  canvas = Canvas(root, width = W, height = H, bg = 'red', highlightthickness=0)
                                         # canvasの作成
  canvas.pack()                          # canvasの配置確定
  display(canvas, msg)                   # 描画関数 (display) の呼出
  root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
