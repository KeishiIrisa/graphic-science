from myCanvas import MyCanvas
from vectorMatrix import norm
import myCircle


def display(canvas, points):
    n = len(points)

    # 全ての対角線を描く
    for i in range(n):
        for j in range(i+1, n):
            canvas.drawPolyline((points[i], points[j]))


def main():
    canvas = MyCanvas()
    points = myCircle.circle((0, 0), 0.8)
    display(canvas, points)
    canvas.mainloop()


if __name__ == '__main__':
    main()
