from tkinter import *
import Chap02.report.circle as circle


def display(canvas, points):
    for i in range(len(points)):
        j = (3*i) % len(points)
        canvas.create_line(points[i], points[j])


def main():
    root = Tk()
    canvas = Canvas(root, width=circle.W, height=circle.H)
    canvas.pack()
    points = circle.circle()
    circle.display(canvas, points)
    display(canvas, points)
    root.mainloop()


if __name__ == '__main__':
    main()
