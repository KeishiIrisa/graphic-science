from tkinter import *

W, H = (600, 600)

"""
色のRGB表現とCMY表現
| 色 | Color | (R G B) | (C M Y) |
| 赤 | Red   | (1 0 0) | (0 1 1) |
...

のように、(R G B) = (1 1 1) - (C M Y) の関係式で表される。
"""
def display(canvas):

    radius2 = 180**2
    centers = ((300.0, 225.0), (213.4, 375.0), (386.6, 375))

    for y in range(H):
        for x in range(W):
            color = '#'
            for i in range(3):
                dist2 = (x-centers[i][0])**2 + (y-centers[i][1])**2
                # CMY表現の場合はffと00を逆に設定すれば、変換できる
                color += "ff" if dist2 > radius2 else "00"
            canvas.create_rectangle((x, y), (x+1, y+1), outline='', fill=color)


def main():
    root = Tk()
    canvas = Canvas(root, width =W, height=H, bg="black")
    canvas.pack()
    display(canvas)
    root.mainloop()


if __name__ == '__main__':
    main()
