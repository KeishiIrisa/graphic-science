import numpy as np

from myGLCanvas import MyGLCanvas
from fractal import Fractal, getArgs
from cube import Cube


class MengerSponge(Fractal):
    def __init__(self, times):
        cube = Cube()
        nv = len(cube.vertices)
        ne = len(cube.edges)
        SCL = 1/3
        vecs = []
        for i in range(nv):
            vecs.append(np.array(cube.vertices[i]) * (1-SCL))

        for i in range(ne):
            mid = (np.array(cube.vertices[cube.edges[i][0]]) +
                   np.array(cube.vertices[cube.edges[i][1]])) / 2
            vecs.append(mid * (1-SCL))

        super().__init__(cube, SCL, vecs, times)


def main():
    times, args = getArgs()
    canvas = MyGLCanvas()
    dispObj = MengerSponge(times)
    canvas.init(dispObj)
    canvas.argsInit(args)
    canvas.loop()


if __name__ == "__main__":
    main()
