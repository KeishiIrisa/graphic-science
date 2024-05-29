import math
import numpy as np
from Chap06.report.vectorMatrix import scaleMatrix
from Chap06.report.myCanvas import MyCanvas
from Chap06.report.fractal import Fractal


class Pascal3(Fractal):
    def __init__(self, canvas):
        base = [np.array((0, 0)), np.array((-1, -3**0.5)), np.array((1, -3**0.5))]
        mats = [scaleMatrix(1/3)]
        mats.append(scaleMatrix(1/3))
        mats.append(scaleMatrix(1/3))
        mats.append(scaleMatrix(1/3))
        mats.append(scaleMatrix(1/3))
        mats.append(scaleMatrix(1/3))
        vecs = [base[0]]  # index0
        vecs.append(mats[0].dot(base[1]) + vecs[0]) # index1
        vecs.append(mats[1].dot(base[2]) + vecs[0]) # index2
        vecs.append(mats[2].dot(base[1]) + vecs[1]) # index3
        vecs.append(mats[3].dot(base[2]) + vecs[1]) # index4
        vecs.append(mats[4].dot(base[2]) + vecs[2]) # index5
        super().__init__(canvas, base, mats, vecs)

    def drawObject(self, pnts):
        self.canvas.drawPolygon(pnts)


def main():
    canvas = MyCanvas(yo=84, r=2.4)
    Pascal3(canvas).drawFractal()
    canvas.mainloop()


if __name__ == '__main__':
    main()
