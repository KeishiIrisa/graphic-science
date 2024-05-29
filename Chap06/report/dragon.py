import math
import numpy as np
from Chap06.report.vectorMatrix import rotMatrix, scaleMatrix
from Chap06.report.myCanvas import MyCanvas
from Chap06.report.fractal import Fractal


class Dragon(Fractal):
    def __init__(self, canvas):
        base = [np.array((0, 0)), np.array((1, 0))]
        mats = [
            scaleMatrix(1/math.sqrt(2)).dot(rotMatrix(math.pi/4)),
            scaleMatrix(1/math.sqrt(2)).dot(rotMatrix(-math.pi/4))
        ]
        vecs = [base[0]] # index0
        vecs.append(mats[0].dot(base[1]) + vecs[0]) # index1
        super().__init__(canvas, base, mats, vecs)

    def drawObject(self, pnts):
        self.canvas.drawPolyline(pnts)

    def drawFractal(self, iterations=-1, mat=np.array(((1, 0), (0, 1))), vec=np.array((0, 0))):
        if iterations < 0:
            iterations = self.times
        if iterations > 0:
            if iterations == self.times:
                # ループを1回だけ回す
                i = 0
                self.drawFractal(iterations - 1, mat.dot(self.mats[i]), mat.dot(self.vecs[i]) + vec)
                # ベクトル行列を入れ替えてもう一度ループを回すことで、90度回転した図形が得られると考えて
                new_mats = [
                    scaleMatrix(1/math.sqrt(2)).dot(rotMatrix(-math.pi/4)),
                    scaleMatrix(1/math.sqrt(2)).dot(rotMatrix(math.pi/4))
                ]
                new_vecs = []
                new_vecs.append(np.array((0, 0)))
                new_vecs.append(new_mats[0].dot(np.array((1, 0))) + new_vecs[0])
                self.mats = new_mats
                self.vecs = new_vecs
                self.drawFractal(iterations - 1, mat.dot(self.mats[0]), mat.dot(self.vecs[0]) + vec)
            else:
                for i in range(len(self.mats)):
                    self.drawFractal(iterations - 1, mat.dot(self.mats[i]), mat.dot(self.vecs[i]) + vec)
        else:
            points = []
            for i in range(len(self.base)):
                points.append(mat.dot(self.base[i]) + vec)
            self.drawObject(points)

            

def main():
    canvas = MyCanvas(xo=50, r=1.2)
    Dragon(canvas).drawFractal()
    canvas.mainloop()


if __name__ == '__main__':
    main()
