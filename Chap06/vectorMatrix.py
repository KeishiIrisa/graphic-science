import math
import numpy as np


def norm(v):
    v = np.array(v)
    return (v.dot(v))**0.5


def rotMatrix(t):
    return np.array(((math.cos(t), -math.sin(t)), (math.sin(t), math.cos(t))))


def scaleMatrix(s):
    return np.array(((s, 0), (0, s)))


def main():
    vec1 = np.array((1, -1))
    vec2 = np.array((3, 4))
    rot = rotMatrix(math.pi/2.0)
    inv = rotMatrix(-math.pi/2.0)
    scl = scaleMatrix(2.0)
    print("|", vec2, "| =", norm(vec2)) 
    print(vec1, '+', vec2, '=', vec1+vec2)
    print(vec2, '-', vec1, '=', vec2-vec1)
    print(vec2, "* 2 =", vec2*2)
    print(vec1, '*', vec2, '=', vec1*vec2)
    print(vec1, '.', vec2, '=', vec1.dot(vec2))
    print('rotate (', vec2, ') =', rot.dot(vec2))
    print('scale&rot(', vec2, ') =', scl.dot(rot).dot(vec2))

    print("inv&rot (", vec2, ") =", inv.dot(rot).dot(vec2))


if __name__ == "__main__":
    main()
