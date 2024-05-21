from myCanvas import MyCanvas
from vectorMatrix import norm
import myCircle


def display(canvas, points):
    for i in range(1, len(points)):
        r = norm(points[i] - points[0])
        canvas.drawCircle(points[i], r)


def main():
    canvas = MyCanvas()
    points = myCircle.circle((0.25, 0), 0.33)
    myCircle.display(canvas, points)
    display(canvas, points)
    canvas.mainloop()


if __name__ == "__main__":
    main()
