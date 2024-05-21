import numpy as np
import math
from myCanvas import MyCanvas
from myCircle import circle, display
import vectorMatrix as vm


def draw_circles(canvas, center, radius):
    for scale in [0.5, 1.0, 1.5]:
        scaled_radius = radius * scale
        canvas.drawCircle(center, scaled_radius, outline='black')


def main():
    def pressed(event):
        global start
        start = canvas.point(event.x, event.y)

    def released(event):
        global start
        end = canvas.point(event.x, event.y)
        radius = vm.norm(np.array(end) - np.array(start))
        draw_circles(canvas, np.array(start), radius)

    global canvas, start
    canvas = MyCanvas(width=500, height=500)
    canvas.bind('<Button-1>', pressed)
    canvas.bind('<ButtonRelease-1>', released)
    canvas.mainloop()


if __name__ == '__main__':
    main()
