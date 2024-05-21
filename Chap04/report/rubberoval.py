from tkinter import *

W, H = (400, 400)


def pressed(event):
    global startX, startY
    startX, startY = (event.x, event.y)


def dragged(event):
    global canvas, startX, startY
    canvas.create_rectangle((2, 2), (W+3, H+3), outline="", fill="#ffffff")
    x, y = (event.x, event.y)
    r = ((x - startX)**2 + (y - startY)**2)**0.5
    canvas.create_oval((startX-r, startY-r), (startX+r, startY+r), outline="black", width=1)


def main():
    global canvas
    root = Tk()
    canvas = Canvas(root, width=W, height=H, bg="#ffffff")
    canvas.pack()
    canvas.bind("<Button-1>", pressed)
    canvas.bind("<B1-Motion>", dragged)
    root.mainloop()


if __name__ == "__main__":
    main()
