from tkinter import *
from myCanvas import MyCanvas


def pressed_black(event):
    global canvas, old
    old = canvas.point(event.x, event.y)


def dragged_black(event):
    global canvas, old
    canvas.drawPolyline((old, canvas.point(event.x, event.y)), color="black")
    old = canvas.point(event.x, event.y)


def pressed_red(event):
    global canvas, old
    old = canvas.point(event.x, event.y)


def dragged_red(event):
    global canvas, old
    canvas.drawPolyline((old, canvas.point(event.x, event.y)), color="red")
    old = canvas.point(event.x, event.y)


def pressed_erase(event):
    global canvas, old
    old = canvas.point(event.x, event.y)


def dragged_erase(event):
    global canvas, old
    canvas.drawMarker(old, fill="white")
    old = canvas.point(event.x, event.y)


def main():
    global canvas
    canvas = MyCanvas(width=400, height=400)
    canvas.bind("<Button-1>", pressed_black)
    canvas.bind("<B1-Motion>", dragged_black)
    canvas.bind("<Button-2>", pressed_red)
    canvas.bind("<B2-Motion>", dragged_red)
    canvas.bind("<Shift-Button-1>", pressed_erase)
    canvas.bind("<Shift-B1-Motion>", dragged_erase)
    canvas.mainloop()


if __name__ == "__main__":
    main()
