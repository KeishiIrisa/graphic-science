import numpy as np

from myGLCanvas3 import MyGLCanvas
from fractal import Fractal, getArgs
from tetrahedron import Tetrahedron


class SierpinskiTetrahedron(Fractal):
    def __init__(self, times):
        tetra = Tetrahedron()
        nv = len(tetra.vertices)
        # ne = len(tetra.edges)
        SCL = 1/2
        vecs = []
        for i in range(nv):
            vecs.append(np.array(tetra.vertices[i]) * (1-SCL))

        # for i in range(ne):
        #     mid = (np.array(tetra.vertices[tetra.edges[i][0]]) +
        #            np.array(tetra.vertices[tetra.edges[i][1]])) / 2
        #     vecs.append(mid * (1-SCL))

        super().__init__(tetra, SCL, vecs, times)


def main():
    times, args = getArgs()
    canvas = MyGLCanvas()
    dispObj = SierpinskiTetrahedron(times)
    canvas.init(dispObj)
    canvas.argsInit(args)
    canvas.loop()


if __name__ == "__main__":
    main()
