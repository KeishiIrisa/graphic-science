from myCanvas import MyCanvas
from vectorMatrix import norm
import myCircle


def display(canvas, points):
    for i in range(len(points)):
        j = (3*i) % len(points)
        canvas.drawPolyline((points[i], points[j]))


def main():
    canvas = MyCanvas()
    points = myCircle.circle((0, 0), 0.8)
    myCircle.display(canvas, points)
    display(canvas, points)
    canvas.mainloop()


if __name__ == '__main__':
    main()
