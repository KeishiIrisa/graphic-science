import math
import numpy as np
from vectorMatrix import scaleMatrix
from myCanvas import MyCanvas
from fractal import Fractal


class Sierpinski(Fractal):
    def __init__(self, canvas):
        base = [np.array((0, 0)), np.array((-1, -3**0.5)), np.array((1, -3**0.5))]
        mats = [scaleMatrix(1/2)]
        mats.append(scaleMatrix(1/2))
        mats.append(scaleMatrix(1/2))
        vecs = [base[0]]
        vecs.append(mats[0].dot(base[1]) + vecs[0])
        vecs.append(mats[1].dot(base[2]) + vecs[0])
        super().__init__(canvas, base, mats, vecs)

    def drawObject(self, pnts):
        self.canvas.drawPolygon(pnts)


def main():
    canvas = MyCanvas(yo=84, r=2.4)
    Sierpinski(canvas).drawFractal()
    canvas.mainloop()


if __name__ == '__main__':
    main()
