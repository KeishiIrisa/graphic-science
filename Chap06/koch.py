import math
import numpy as np
from vectorMatrix import rotMatrix, scaleMatrix
from myCanvas import MyCanvas
from fractal import Fractal


class Koch(Fractal):
    def __init__(self, canvas):
        base = [np.array((0, 0)), np.array((1, 0))]
        mats = [scaleMatrix(1/3)]
        mats.append(scaleMatrix(1/3).dot(rotMatrix(math.pi/3)))
        mats.append(scaleMatrix(1/3).dot(rotMatrix(-math.pi/3)))
        mats.append(scaleMatrix(1/3))
        vecs = [base[0]]
        vecs.append(mats[0].dot(base[1]) + vecs[0])
        vecs.append(mats[1].dot(base[1]) + vecs[1])
        vecs.append(mats[2].dot(base[1]) + vecs[2])
        super().__init__(canvas, base, mats, vecs)

    def drawObject(self, pnts):
        self.canvas.drawPolyline(pnts)


def main():
    canvas = MyCanvas(xo=50, r=1.2)
    Koch(canvas).drawFractal()
    canvas.mainloop()


if __name__ == '__main__':
    main()
