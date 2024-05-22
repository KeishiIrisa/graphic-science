from myCanvas import MyCanvas
import myCircle


def display(canvas, points):
    for i in range(len(points)):
        j = (2*i) % len(points)
        canvas.drawPolyline((points[i], points[j]))


def main():
    canvas = MyCanvas()
    points = myCircle.circle((0.25, 0), 0.33)
    myCircle.display(canvas, points)
    display(canvas, points)
    canvas.mainloop()


if __name__ == "__main__":
    main()
