import math
import numpy as np
from Chap06.report.vectorMatrix import rotMatrix, scaleMatrix
from Chap06.report.myCanvas import MyCanvas
from Chap06.report.fractal import Fractal


def get_rotate_coordinate(x, y, Cx, Cy, theta=math.pi/2):
    newx = x * math.cos(theta) - y * math.sin(theta) + Cx - Cx * math.cos(theta) + Cy * math.sin(theta)
    newy = x * math.sin(theta) + y * math.cos(theta) + Cy - Cx * math.sin(theta) - Cy * math.cos(theta)
    return newx, newy


class Dragon(Fractal):
    def __init__(self, canvas):
        base = [np.array((0, 0)), np.array((1, 0))]
        mats = [
            scaleMatrix(1/math.sqrt(2)).dot(rotMatrix(math.pi/4)),
            scaleMatrix(1/math.sqrt(2)).dot(rotMatrix(-math.pi/4)),
        ]
        vecs = [base[0]] # index0
        vecs.append(mats[0].dot(base[1]) + vecs[0]) # index1
        super().__init__(canvas, base, mats, vecs)
        self.vecs_swapped = False

    def drawObject(self, pnts):
        self.canvas.drawPolyline(pnts)

    def drawFractal(self, iterations=-1, mat=np.array(((1, 0), (0, 1))), vec=np.array((0, 0))):
        if iterations < 0:
            iterations = self.times

        xs = [0, 1]
        ys = [0, 0]

        for depth in range(iterations):
            for k in range(2 ** depth):
                newx, newy = get_rotate_coordinate(xs[2 ** depth - k - 1], ys[2 ** depth - k - 1], Cx=xs[2 ** depth], Cy=ys[2 ** depth])
                xs.append(newx)
                ys.append(newy)

        points = [np.array((xs[i], ys[i])) for i in range(len(xs))]
        self.drawObject(points)
            

def main():
    canvas = MyCanvas(xo=50, r=1.2)
    Dragon(canvas).drawFractal(iterations=10)  # 適当な深度を設定
    canvas.mainloop()

if __name__ == '__main__':
    main()
