import sys
import numpy as np
from Chap06.report.myCanvas import MyCanvas


class Fractal(object):
    def __init__(self, canvas, base, mats, vecs):
        if len(sys.argv) > 1:
            num = sys.argv[1]
        else:
            num = input("# of iterations -> ")
        self.times = int(num)
        self.canvas = canvas
        self.base, self.mats, self.vecs = (base, mats, vecs)

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
