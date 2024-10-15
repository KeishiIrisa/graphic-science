import numpy as np

from myGLCanvas import MyGLCanvas
from fractal import Fractal, getArgs
from dodecahedron import Dodecahedron


class DodecahedronFragment(Fractal):
    def __init__(self, times):
        dodeca = Dodecahedron()
        nv = len(dodeca.vertices)
        phi = (1 + 5**0.5) / 2
        SCL = 1/(2+phi)
        vecs = []
        for i in range(nv):
            vecs.append(np.array(dodeca.vertices[i]) * (1-SCL))

        super().__init__(dodeca, SCL, vecs, times)


def main():
    times, args = getArgs()
    canvas = MyGLCanvas()
    dispObj = DodecahedronFragment(times)
    canvas.init(dispObj)
    canvas.argsInit(args)
    canvas.loop()


if __name__ == "__main__":
    main()
