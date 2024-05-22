from myCanvas import MyCanvas
from vectorMatrix import norm
import numpy as np
import myCircle


def display(canvas, points):
    for i in range(1, len(points)):
        vector = np.array(points[i]) - np.array(points[0])
        y_component_vector = np.array((0, vector[1]))
        r = norm(y_component_vector)
        myCircle.display(canvas, myCircle.circle((points[i]), r))


def main():
    canvas = MyCanvas()
    points = myCircle.circle((0, 0), 0.4)
    myCircle.display(canvas, points)
    display(canvas, points)
    canvas.mainloop()


if __name__ == '__main__':
    main()
