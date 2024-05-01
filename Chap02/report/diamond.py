from tkinter import *
import Chap02.report.circle as circle

W, H = (600, 600)


def display(canvas, points):
    n = len(points)

    # 全ての対角線を描く
    for i in range(n):
        for j in range(i+1, n):
            canvas.create_line(points[i], points[j])


def main():
    root = Tk()
    canvas = Canvas(root, width=W, height=H)
    canvas.pack()
    points = circle.circle()
    display(canvas, points)
    root.mainloop()


if __name__ == '__main__':
    main()
