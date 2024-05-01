from tkinter import *                    # tkinterモジュールのimport

W, H = (600, 600)                        # canvasの幅と高さ

def display(canvas):                     # 描画関数
  '''
  canvas - 描画するcanvas
  11本の放射上の線分を描画する
  '''
  points = ((W/60, H-1), (W/20,  H-1), (W/8,  H-1), (W/4, H-1),
            (W/2, H-1), (W-1,  H-1), (W-1,  H/2), (W-1, H/4),
            (W-1, H/8), (W-1, H/20), (W-1, H/60)) # 線分の終点，11個
  origin = (0, 0)                        # 線分の始点 (左上隅)
  for i in range(len(points)):           # 線分描画の反復 (終点の個数分)
    canvas.create_line(origin, points[i]) # 線分の描画

def main():                              # main関数
  root = Tk()                            # ルートフレームの作成
  canvas = Canvas(root, width = W, height = H, highlightthickness=0)
                                         # canvasの作成
  canvas.pack()                          # canvasの配置確定
  display(canvas)                        # 描画関数 (display) の呼出
  root.mainloop()                        # ルートフレームの実行ループ開始

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
