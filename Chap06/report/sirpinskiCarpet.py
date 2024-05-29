import math
import numpy as np
from Chap06.report.vectorMatrix import scaleMatrix
from Chap06.report.myCanvas import MyCanvas
from Chap06.report.fractal import Fractal


class SirpinskiCarpet(Fractal):
    def __init__(self, canvas):
        base = [np.array((0, 0)), np.array((1, 0)), np.array((1, -1)), np.array((0, -1))]
        mats = [scaleMatrix(1/3)]
        mats.append(scaleMatrix(1/3))
        mats.append(scaleMatrix(1/3))
        mats.append(scaleMatrix(1/3))
        mats.append(scaleMatrix(1/3))
        mats.append(scaleMatrix(1/3))
        mats.append(scaleMatrix(1/3))
        mats.append(scaleMatrix(1/3))
        vecs = [base[0]] # index0
        vecs.append(mats[0].dot(base[1]) + vecs[0]) # index1
        vecs.append(mats[1].dot(base[1]) + vecs[1]) # index2
        vecs.append(mats[2].dot(base[3]) + vecs[0]) # index3
        vecs.append(mats[3].dot(base[3]) + vecs[2]) # index4
        vecs.append(mats[4].dot(base[3]) + vecs[3]) # index5
        vecs.append(mats[5].dot(base[1]) + vecs[5]) # index6
        vecs.append(mats[6].dot(base[1]) + vecs[6]) # index7
        super().__init__(canvas, base, mats, vecs)

    def drawObject(self, pnts):
        self.canvas.drawPolygon(pnts)


def main():
    canvas = MyCanvas(xo=150, yo=150)
    SirpinskiCarpet(canvas).drawFractal()
    canvas.mainloop()


if __name__ == '__main__':
    main()
