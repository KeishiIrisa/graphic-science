from tkinter import *
import Chap02.report.circle as circle


def display(canvas, points):
    for i in range(1, len(points)):
        r = abs(points[i][1] - points[0][1])
        ul = (points[i][0] - r, points[i][1] - r)
        lr = (points[i][0] + r, points[i][1] + r)
        canvas.create_oval(ul, lr)


def main():
    root = Tk()
    canvas = Canvas(root, width=circle.W, height=circle.H)
    canvas.pack()
    points = circle.circle((circle.W/2+70, circle.H/2), 100)
    circle.display(canvas, points)
    display(canvas, points)
    root.mainloop()


if __name__ == '__main__':
    main()
