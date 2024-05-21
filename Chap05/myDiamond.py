import numpy as np
import math
import sys
from myCanvas import MyCanvas
from myCircle import circle, display
import vectorMatrix as vm


def draw_diamond_pattern(canvas, center, size, num):
    angle = 2 * np.pi / num
    points = []
    for i in range(num):
        x = center[0] + size * np.cos(i * angle)
        y = center[1] + size * np.sin(i * angle)
        points.append(np.array([x, y]))
    points.append(points[0])
    canvas.drawPolyline(points, color='blue')


def main():
    canvas = MyCanvas(width=500, height=500)
    center = np.array([0, 0])
    size = 0.5
    num = 4
    draw_diamond_pattern(canvas, center, size, num)
    canvas.mainloop()


if __name__ == '__main__':
    main()
