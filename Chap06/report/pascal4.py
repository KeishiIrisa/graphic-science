import math
import numpy as np
from Chap06.report.vectorMatrix import scaleMatrix
from Chap06.report.myCanvas import MyCanvas
from Chap06.report.fractal import Fractal


class Pascal4(Fractal):
    def __init__(self, canvas):
        base = [np.array((0, 0)), np.array((-1, -3**0.5)), np.array((1, -3**0.5))]
        mats = [scaleMatrix(1/4)]
        mats.append(scaleMatrix(1/4))
        mats.append(scaleMatrix(1/4))
        mats.append(scaleMatrix(1/4))
        mats.append(scaleMatrix(1/4))
        mats.append(scaleMatrix(1/4))
        mats.append(scaleMatrix(1/4))
        mats.append(scaleMatrix(1/4))
        mats.append(scaleMatrix(1/4))
        mats.append(scaleMatrix(1/4))
        vecs = [base[0]]  # index0
        vecs.append(mats[0].dot(base[1]) + vecs[0]) # index1
        vecs.append(mats[1].dot(base[2]) + vecs[0]) # index2
        vecs.append(mats[2].dot(base[1]) + vecs[1]) # index3
        vecs.append(mats[3].dot(base[2]) + vecs[1]) # index4
        vecs.append(mats[4].dot(base[2]) + vecs[2]) # index5
        vecs.append(mats[5].dot(base[1]) + vecs[3]) # index6
        vecs.append(mats[6].dot(base[2]) + vecs[3]) # index7
        vecs.append(mats[7].dot(base[2]) + vecs[4]) # index8
        vecs.append(mats[8].dot(base[2]) + vecs[5]) # index9
        super().__init__(canvas, base, mats, vecs)

    def drawObject(self, pnts):
        self.canvas.drawPolygon(pnts)


def main():
    canvas = MyCanvas(yo=84, r=2.4)
    Pascal4(canvas).drawFractal()
    canvas.mainloop()


if __name__ == '__main__':
    main()
