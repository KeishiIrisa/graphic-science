import numpy as np
import math
import sys
from myCanvas import MyCanvas
from myCircle import circle, display
import vectorMatrix as vm


def draw_nephroid(canvas, center, r):
    points = []
    for t in np.linspace(0, 2*np.pi, 100):
        x = center[0] + r * (1 - 0.5 * np.cos(t)) * np.cos(t)
        y = center[1] + r * (1 - 0.5 * np.cos(t)) * np.sin(t)
        points.append(np.array([x, y]))
    canvas.drawPolyline(points, color='red')


def main():
    canvas = MyCanvas(width=500, height=500)
    center = np.array([0, 0])
    r = 0.5
    draw_nephroid(canvas, center, r)
    canvas.mainloop()


if __name__ == '__main__':
    main()
