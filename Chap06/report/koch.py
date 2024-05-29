import math
import numpy as np
from Chap06.report.vectorMatrix import rotMatrix, scaleMatrix
from Chap06.report.myCanvas import MyCanvas
from Chap06.report.fractal import Fractal


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

    # drawFractalをオーバーライド
    def drawFractal(self, iterations=-1, mat=np.array(((1, 0), (0, 1))), vec=np.array((0, 0))):
        if iterations < 0:
            iterations = self.times
        if iterations > 0:
            # ここにfor文があるから、i番目にdrawFractalが始まると、その中で、drawFractalが複数回始まる。そしてそれぞれのdrawFractalのiterationsが0になれば三角形の描画を始める。
            for i in range(len(self.mats)):
                # mat.dot(self.vecs[i]+vec)は次の反復して描く図形の頂点へのベクトル
                self.drawFractal(iterations-1, mat.dot(self.mats[i]), mat.dot(self.vecs[i])+vec)
        else:
            points = []
            # それぞれのパーツで描画する点の数
            for i in range(len(self.base)):
                points.append(mat.dot(self.base[i])+vec)
            self.drawObject(points)


def main():
    canvas = MyCanvas(xo=50, r=1.2)
    Koch(canvas).drawFractal()
    canvas.mainloop()


if __name__ == '__main__':
    main()
