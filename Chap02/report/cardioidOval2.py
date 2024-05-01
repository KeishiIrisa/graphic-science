from tkinter import *
import Chap02.report.circle as circle
import sys


def display(canvas, points):
    
    if len(sys.argv) > 2:
        x = float(sys.argv[2])
    else:
        x = float(input("> float"))

    for i in range(1, len(points)):
        r = (((points[i][0] - points[0][0])**2 + (points[i][1] - points[0][1])**2)**0.5)

        # x軸方向にx倍伸びたカージオイドを作成する
        ul = (points[i][0] - x*r, points[i][1] - r)
        lr = (points[i][0] + x*r, points[i][1] + r)
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
