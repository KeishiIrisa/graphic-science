from tkinter import *


def pressed_black(event):
    global oldX, oldY
    oldX, oldY = (event.x, event.y)


def dragged_black(event):
    global canvas, oldX, oldY
    x, y = (event.x, event.y)
    canvas.create_line((oldX, oldY), (x, y), fill="black")
    oldX, oldY = (x, y)


def pressed_red(event):
    global oldX, oldY
    oldX, oldY = (event.x, event.y)


def dragged_red(event):
    global canvas, oldX, oldY
    x, y = (event.x, event.y)
    canvas.create_line((oldX, oldY), (x, y), fill="red")
    oldX, oldY = (x, y)


def pressed_erase(event):
    global oldX, oldY
    oldX, oldY = (event.x, event.y)


def dragged_erase(event):
    global canvas, oldX, oldY
    x, y = (event.x, event.y)
    canvas.create_rectangle((oldX, oldY), (x, y), fill="white")
    oldX, oldY = (x, y)


def main():
    global canvas
    W, H = (400, 400)
    root = Tk()
    canvas = Canvas(root, width=W, height=H, bg="#ffffff")
    canvas.pack()
    canvas.bind("<Button-1>", pressed_black)
    canvas.bind("<B1-Motion>", dragged_black)
    canvas.bind("<Button-2>", pressed_red)
    canvas.bind("<B2-Motion>", dragged_red)
    canvas.bind("<Shift-Button-1>", pressed_erase)
    canvas.bind("<Shift-B1-Motion>", dragged_erase)
    root.mainloop()


if __name__ == "__main__":
    main()
