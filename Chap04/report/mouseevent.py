from tkinter import *

W, H = (200, 200)


def pressed(event):
    global canvas
    canvas.create_rectangle((2, 2), (W+3, H+3), outline='', fill='#ff0000')


def released(event):
    global canvas
    canvas.create_rectangle((2, 2), (W+3, H+3), outline='', fill='#00ff00')


def entered(event):
    global canvas
    canvas.create_rectangle((2, 2), (W+3, H+3), outline='', fill='#0000ff')


def left(event):
    global canvas
    canvas.create_rectangle((2, 2), (W+3, H+3), outline='', fill='#ffff00')


def main():
    global canvas
    root = Tk()
    canvas = Canvas(root, width=W, height=H, bg='#ffffff')
    canvas.pack()
    canvas.bind('<Button-1>', pressed)
    canvas.bind('<ButtonRelease-1>', released)
    canvas.bind('<Enter>', entered)
    canvas.bind('<Leave>', left)
    root.mainloop()


if __name__ == '__main__':
    main()
