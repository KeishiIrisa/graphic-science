from tkinter import *
import math
import colorsys
import circle
from colorRingRGB import string


def display(canvas):
    center = (circle.W // 2, circle.H // 2)
    radius = circle.R

    for y in range(circle.H):
        for x in range(circle.W):
            dx = x - center[0]
            dy = y - center[1]

            h = math.atan2(dy, dx) / (2 * math.pi)
            h = h if h >= 0.0 else h + 1.0

            s = (dx**2 + dy**2)**0.5 / radius
            v = 0.0 if s > 1.0 else 1.0
            s = 0.0 if s > 1.0 else s

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
