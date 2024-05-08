from tkinter import *


def pressed(event):
    global oldX, oldY
    oldX, oldY = (event.x, event.y)


def dragged(event):
    global canvas, oldX, oldY
    x, y = (event.x, event.y)
    canvas.create_line((oldX, oldY), (x, y), fill="black")
    oldX, oldY = (x, y)


def main():
    global canvas
    W, H = (400, 400)
    root = Tk()
    canvas = Canvas(root, width=W, height=H, bg="#ffffff")
    canvas.pack()
    canvas.bind("<Button-1>", pressed)
    canvas.bind("<B1-Motion>", dragged)
    root.mainloop()


if __name__ == "__main__":
    main()
