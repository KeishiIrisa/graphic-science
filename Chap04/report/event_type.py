from tkinter import *                    # tkinterモジュールのimport

W, H = (200, 200)                        # canvasの幅と高さ


def pressed(event):                      # Button1 pressed コールバック関数
    global canvas
    canvas.create_rectangle((2, 2), (W+3, H+3), outline='', fill='#ff0000')
    canvas.create_text(W/2, H/2, text='Event Type: ' + event.type, fill='white')


def released(event):                     # Button1 released コールバック関数 
    global canvas
    canvas.create_rectangle((2, 2), (W+3, H+3), outline='', fill='#00ff00')
    canvas.create_text(W/2, H/2, text='Event Type: ' + event.type, fill='white')


def main():                              # main関数
    global canvas                          # 大域変数 canvas
    root = Tk()                            # ルートフレームの作成
    canvas = Canvas(root, width = W, height = H, bg='#00ff00') # canvasの作成
    canvas.pack()                          # canvasの配置確定
    canvas.bind('<Button-1>', pressed)     # Button1 pressed コールバック関数
    canvas.bind('<ButtonRelease-1>', released) # Button1 released コールバック関数
    root.mainloop()                        # ルートフレームの実行ループ開始


if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
    main()                                 # main関数の呼出
