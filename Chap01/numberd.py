     1	from tkinter import *                    # tkinterモジュールのimport
     2	#from tkinter import Tk, Canvas           # tkinterモジュールからTk,Canvasのimport
     3	import sys                               # sysモジュールのimport
     4	
     5	W, H = (400, 300)                        # canvasの幅と高さ
     6	
     7	def display(canvas, msg):                # 描画関数
     8	  '''
     9	  canvas - 描画するcanvas
    10	  2本の線分と文字列を描画する
    11	  '''
    12	  canvas.create_line((0, 0), (W-1, H-1), fill = 'blue') # 線分の描画 (左上→右下)
    13	  canvas.create_line((0, H-1), (W-1, 0), fill = 'green') # 線分の描画 (左下→右上)
    14	  canvas.create_text((W/2, H/2), text=msg) # 文字列の描画 (canvas中央)
    15	
    16	def main():                              # main関数
    17	  if len(sys.argv) > 1:                  # シェル引数がある場合
    18	    msg = sys.argv[1]                    # 第1引数を頂点数の文字列
    19	  else:                                  # シェル引数がない場合
    20	    msg = input('message -> ')           # 描画する文字列を入力
    21	  root = Tk()                            # ルートフレームの作成
    22	  canvas = Canvas(root, width = W, height = H, bg = 'red', highlightthickness=0)
    23	                                         # canvasの作成
    24	  canvas.pack()                          # canvasの配置確定
    25	  display(canvas, msg)                   # 描画関数 (display) の呼出
    26	  root.mainloop()                        # ルートフレームの実行ループ開始
    27	
    28	if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
    29	  main()                                 # main関数の呼出
