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
    original_r = norm(start - cursor)
    one_second_r = 0.5*original_r
    three_second_r = 1.5*original_r
    myCircle.display(canvas, myCircle.circle(start, original_r))
    myCircle.display(canvas, myCircle.circle(start, one_second_r))
    myCircle.display(canvas, myCircle.circle(start, three_second_r))


def main():
    global canvas
    canvas = MyCanvas()
    canvas.bind("<Button-1>", pressed)
    canvas.bind("<B1-Motion>", dragged)
    canvas.mainloop()


if __name__ == "__main__":
    main()
