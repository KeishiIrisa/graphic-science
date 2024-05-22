import numpy as np
import sys
import math
from myCanvas import MyCanvas


def circle(cen=(0, -0.5), r=0.5):
    if len(sys.argv) > 1:
        num = sys.argv[1]
    else:
        num = input('# of points -> ')
    n = int(num)
    p = []
    for i in range(n):
        t = 2 * math.pi * i / n
        p.append(np.array((r * math.cos(t) + cen[0], r * math.sin(t) + cen[1])))
    return tuple(p)


def display(canvas, points):
    canvas.drawPolygon(points, fill='')


# 格子点を描く関数
def draw_grid(canvas, interval):
    x_range, y_range = 2.0, 2.0

    num_x_lines = int(x_range / interval) + 1
    num_y_lines = int(y_range / interval) + 1

    # 垂直の格子線
    for i in range(-num_x_lines, num_x_lines + 1):
        x = i * interval
        canvas.drawPolyline(((x, -y_range), (x, y_range)))

    # 水平の格子線
    for i in range(-num_y_lines, num_y_lines + 1):
        y = i * interval
        canvas.drawPolyline(((-x_range, y), (x_range, y)))


def main():
    canvas = MyCanvas()
    draw_grid(canvas, 0.5)
    points = circle()
    display(canvas, points)
    canvas.mainloop()


if __name__ == '__main__':
    main()
