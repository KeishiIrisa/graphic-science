from tkinter import *                    # tkinterモジュールのimport
import random                            # randomモジュールのimport
import time                              # timeモジュールのimport

W, H  = (400, 400)                       # canvasの幅と高さ
R     = 5                                # 正方形 (marker) の半径 (1辺の半分)
TIMES = 10                               # 試行回数


def display():                           # 正方形 (marker) の描画関数
    global canvas, error, x, y             # 大域変数 canvas, error, x, y
    x = random.randint(2+R, W+2-R)         # 正方形 (marker) の x座標
    y = random.randint(2+R, H+2-R)         # 正方形 (marker) の y座標
    canvas.create_rectangle((2, 2), (W+3, H+3), outline='', fill='#ffffff')
                                          # 背景の白長方形での描画 (クリア)
    if error:                              # ミスした場合 - 赤で描画
        canvas.create_rectangle((x-R, y-R), (x+R, y+R), outline='', fill='#ff0000')
    else:                                  # ヒットした場合 - 黒で描画
        canvas.create_rectangle((x-R, y-R), (x+R, y+R), outline='', fill='#000000')


def pressed1(event):                     # Button1 pressed コールバック関数
    global x, y, error, count, ttime, fastest  # 大域変数 x, y, error など
    if count > 0:                          # カウント (残り回数) が正 = 実行中
        xc, yc = (event.x, event.y)          # press時の座標
        if x - R <= xc <= x + R and y - R <= yc <= y + R:  # 正方形 (marker) との位置
            error = False                      # 正方形 (marker) の外部 - ミス
            count = count - 1                  # カウント (残り回数) の減少
        else:
            error = True                       # 正方形 (marker) の内部 - ヒット
            count = count + 1                  # カウント (残り回数) の増加
        if count > 0:                        # カウント (残り回数) が正 = 継続
            print(count, 'more!!')             # カウント (残り回数) の表示
            display()                          # 正方形 (marker) の描画
        else:                                # カウント (残り回数) が 0 = 終了
            ttime = time.time() - ttime        # 作業時間の測定
            if fastest < 0 or ttime < fastest:  # 最速時間の場合
                fastest = ttime                  # 最速時間の更新
            print('Finished in', ttime, 'secs. Fastest time:', fastest, 'secs.')
                                             # 最速時間の表示
    else:                                  # カウント (残り回数) が 0 = 実行前
        if fastest < 0:                      # (最速時間の)記録なしの場合
            print('Click right button to start.')  # 開始方法のメッセージ表示
        else:                                # (最速時間の)記録ありの場合
            print('Click right button to start. Fastest time:', fastest, 'secs.')
                                           # 開始方法のメッセージと最速時間記録の表示
                                         
                                         
def released2(event):                    # Button2 released コールバック関数
    global error, count, ttime             # 大域変数 error, count, ttime
    error = False                          # ヒット／ミスの初期化 - ヒット
    count = TIMES                          # カウント (残り回数) の初期化
    print('Start clicking ...', count, 'more!!') # 開始とカウント (残り回数) の表示
    ttime = time.time()                    # 開始時刻の記録
    display()                              # 正方形 (marker) の描画


def main():                              # main関数
    global canvas, count, fastest          # 大域変数 canvas, count, fastest
    count, fastest = (0, -1)               # カウント (残り回数)と最速時間の初期化
    root = Tk()                            # ルートフレームの作成
    canvas = Canvas(root, width = W, height = H, bg='#ffffff') # canvasの作成
    canvas.pack()                          # canvasの配置確定
    canvas.bind('<Button-1>', pressed1)    # Button1 pressed コールバック関数
    canvas.bind('<ButtonRelease-2>', released2) # Button2 released コールバック関数
    root.mainloop()                        # ルートフレームの実行ループ開始


if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
    main()                                 # main関数の呼出
    
