from myCanvas import MyCanvas
from vectorMatrix import norm
import numpy as np
import myCircle


def pressed(event):
    global start
    start = canvas.point(event.x, event.y)


def dragged(event):
    global canvas, start
    canvas.clear()
    cursor = canvas.point(event.x, event.y)
    r = norm(start - cursor)
    myCircle.display(canvas, myCircle.circle(start, r))


def main():
    global canvas
    canvas = MyCanvas()
    canvas.bind("<Button-1>", pressed)
    canvas.bind("<B1-Motion>", dragged)
    canvas.mainloop()


if __name__ == "__main__":
    main()
