import math
import numpy as np
from Chap06.report.vectorMatrix import scaleMatrix, rotMatrix
from Chap06.report.myCanvas import MyCanvas
from Chap06.report.fractal import Fractal


class Pentagon(Fractal):
    def __init__(self, canvas):
        center = np.array((0, -1))
        rotation_angle = -(3/2)*math.pi/5
        base = [np.array((0,0))] # index0
        base.append(np.array(rotMatrix(rotation_angle).dot(center - base[0])) + base[0]) # index1
        base.append(np.array(rotMatrix(rotation_angle).dot(center - base[1])) + base[1]) # index2
        base.append(np.array(rotMatrix(rotation_angle).dot(center - base[2])) + base[2]) # index3
        base.append(np.array(rotMatrix(rotation_angle).dot(center - base[3])) + base[3]) # index4
        si = (1 + 5**(1/2))/2
        mats = [scaleMatrix(1/(si**2))]
        mats.append(scaleMatrix(1/si**2))
        mats.append(scaleMatrix(1/si**2))
        mats.append(scaleMatrix(1/si**2))
        mats.append(scaleMatrix(1/si**2))
        vecs = [base[0]] # index0
        vecs.append(mats[0].dot(base[1]) + vecs[0]) # index1
        vecs.append(mats[1].dot(base[2]) + vecs[0]) # index2
        vecs.append(mats[2].dot(base[3]) + vecs[0]) # index3
        vecs.append(mats[3].dot(base[4]) + vecs[0]) # index4
        super().__init__(canvas, base, mats, vecs)

    def drawObject(self, pnts):
        self.canvas.drawPolygon(pnts)


def main():
    canvas = MyCanvas(yo=50, r=2.4)
    Pentagon(canvas).drawFractal()
    canvas.mainloop()


if __name__ == '__main__':
    main()
