import numpy as np

from myGLCanvas import MyGLCanvas
from fractal import Fractal, getArgs
from octahedron import Octahedron


class OctahedronFragment(Fractal):
    def __init__(self, times):
        octa = Octahedron()
        nv = len(octa.vertices)
        SCL = 1/2
        vecs = []
        for i in range(nv):
            vecs.append(np.array(octa.vertices[i]) * (1-SCL))

        super().__init__(octa, SCL, vecs, times)


def main():
    times, args = getArgs()
    canvas = MyGLCanvas()
    dispObj = OctahedronFragment(times)
    canvas.init(dispObj)
    canvas.argsInit(args)
    canvas.loop()


if __name__ == "__main__":
    main()
