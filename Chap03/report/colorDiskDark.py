from tkinter import *
import math
import colorsys
import circle
from colorRingRGB import string

"""
・色相(Hue) ・彩度(Saturation) ・明度(Value)
例題3では内側に向かって彩度(S)が落ちていき、中心で白色になっていたのに対して、本プログラムでは、内側に向かって明度(V)が落ちていき、中心で黒色になるプログラムに変更する。
"""


def display(canvas):
    center = (circle.W // 2, circle.H // 2)
    radius = circle.R

    for y in range(circle.H):
        for x in range(circle.W):
            dx = x - center[0]
            dy = y - center[1]

            # 原点からの角度をラジアンで表し、それを2πで割り、0から1の範囲で色相を表す。
            h = math.atan2(dy, dx) / (2 * math.pi)
            h = h if h >= 0.0 else h + 1.0

            v = (dx**2 + dy**2)**0.5 / radius
            s = 0.0 if v > 1.0 else 1.0
            v = 0.0 if v > 1.0 else v

            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            color = string(r, g, b)

            canvas.create_rectangle((x, y), (x + 1, y + 1), outline='', fill=color)


def main():
    root = Tk()
    canvas = Canvas(root, width=circle.W, height=circle.H, bg='black')
    canvas.pack()
    display(canvas)
    root.mainloop()


if __name__ == '__main__':
    main()
