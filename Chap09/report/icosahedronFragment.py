import numpy as np

from myGLCanvas import MyGLCanvas
from fractal import Fractal, getArgs
from icosahedron import Icosahedron


class IcosahedronFragment(Fractal):
    def __init__(self, times):
        icosa = Icosahedron()
        nv = len(icosa.vertices)
        phi = (1 + 5**0.5) / 2
        SCL = 1/(1+phi)
        vecs = []
        for i in range(nv):
            vecs.append(np.array(icosa.vertices[i]) * (1-SCL))

        super().__init__(icosa, SCL, vecs, times)


def main():
    times, args = getArgs()
    canvas = MyGLCanvas()
    dispObj = IcosahedronFragment(times)
    canvas.init(dispObj)
    canvas.argsInit(args)
    canvas.loop()


if __name__ == "__main__":
    main()
