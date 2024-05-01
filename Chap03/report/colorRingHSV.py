from tkinter import *
import circle
import colorsys


def f2hex(x):
    return '{:02X}'.format(int(x*0xff))


def string(r, g, b):
    return '#' + f2hex(r) + f2hex(g) + f2hex(b)


def color(n, i):
    hue = i / n
    saturation = 1.0
    value = 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
    return string(r, g, b)


def display(canvas, points):
    for i in range(len(points)):
        j = (i+1) % len(points)
        canvas.create_line(points[i], points[j], fill=color(len(points), i))


def main():
    root = Tk()
    canvas = Canvas(root, width=circle.W, height=circle.H, bg='black')
    canvas.pack()
    points = circle.circle()
    display(canvas, points)
    root.mainloop()


if __name__ == '__main__':
    main()
